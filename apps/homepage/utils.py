import random

from PIL import Image, ImageDraw, ImageFont, ImageFilter
from io import BytesIO


_letter_cases = "abcdefghjkmnpqrstuvwxy"  # 小写字母，去除可能干扰的i，l，o，z
_upper_cases = _letter_cases.upper()  # 大写字母
_numbers = ''.join(map(str, range(3, 10)))  # 数字
init_chars = ''.join((_letter_cases, _upper_cases, _numbers))

# 随机颜色的生成
def _random_color():
    red=random.randint(0,255)
    green=random.randint(0,255)
    blue=random.randint(0,255) 
    return (red, green, blue)

def create_verification_code(size=(120, 30),
                             chars=init_chars,
                             img_type='PNG',
                             mode='RGB',
                             bg_color=(230, 230, 230),
                             fg_color=(0, 0, 255),
                             font_type='static/fonts/Monaco.ttf',
                             font_size=18,
                             length=4,
                             point_chance=6):
    """
    @todo: 生成验证码图片
    @param size: 图片的大小，格式（宽，高），默认为(120, 30)
    @param chars: 允许的字符集合，格式字符串
    @param img_type: 图片保存的格式，默认为PNG，可选的为GIF，JPEG，TIFF，PNG
    @param mode: 图片模式，默认为RGB
    @param bg_color: 背景颜色，默认为白色
    @param fg_color: 前景色，验证码字符颜色，默认为蓝色#0000FF
    @param font_type: 验证码字体，默认为 ae_AlArabiya.ttf
    @param font_size: 验证码字体大小
    @param length: 验证码字符个数
    @param point_chance: 干扰点出现的概率，大小范围[0, 100]
    @return: [0]: 图片二进制数据
    @return: [1]: 验证码图片中的字符串
    """
    width, height = size
    img = Image.new(mode, size, bg_color)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_type, font_size)

    # 绘制验证码字符
    c_chars = random.sample(chars, length)
    code_str = ' %s ' % ' '.join(c_chars)
    font_width, font_height = font.getsize(code_str)
    draw.text(((width - font_width) / 3, (height - font_height) / 3),
              code_str, font=font, fill=fg_color)
    
    # 绘制干扰线
    begin = (random.randint(0, size[0]), random.randint(0, size[1]))
    end = (random.randint(0, size[0]), random.randint(0, size[1]))
    draw.line([begin, end], fill=_random_color())

    # 绘制干扰点
    chance = min(100, max(0, int(point_chance)))
    for w in range(width):
        for h in range(height):
            tmp = random.randint(0, 100)
            if tmp > 100 - chance:
                draw.point((w, h), fill=(0, 0, 0))
    
    # 图形扭曲
    params = [1 - float(random.randint(1, 2)) / 100,
              0,
              0,
              0,
              1 - float(random.randint(1, 10)) / 100,
              float(random.randint(1, 2)) / 500,
              0.001,
              float(random.randint(1, 2)) / 500
              ]
    img = img.transform(size, Image.PERSPECTIVE, params)  # 创建扭曲
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)  # 滤镜，边界加强（阈值更大）

    code = ''.join(c_chars)
    stream = BytesIO()
    img.save(stream, img_type)
    return stream.getvalue(), code
