# 多功能网站

目前功能：照片换底色

## 开发测试环境

1. 环境安装
    - 安装python3.5.4
    - 安装依赖包：`pip install -r requirements.txt`（requirements.txt文件在项目根目录中）
2. 服务启动

    项目根目录下执行：`python manager.py runserver 80`

## 后端接口

进入页面

- 路径：/colorch/或者/（/会301到/colorch/）
- 请求类型：GET/POST
- 参数：无
- 返回：color_ch.html

文件上传并修改底色

- 路径：/colorch/upload/
- 请求类型：POST
- 参数：
    - img：用户选择的原图片文件
    - bg_color：目标底色（值只能为其中一个：white、red、blue）
    - ver_code：用户输入的验证码
- 返回：
    - 请求为GET请求：返回404页面
    - 验证码错误：'{"res": "ver_code wrong"}'
    - 目标底色参数错误：'{"res": "No such color"}'
    - 正常情况：
        - 内容：底色转换后的图片的二进制数据（JPG格式）
        - content_type：image

获取验证码

- 路径：/utils/ver_code/
- 请求类型：GET/POST
- 参数：无
- 返回：
    - 内容：验证码图片二进制数据（PNG格式，图片size后端可控制）
    - content_type：image

## 代码/文件目录说明

测试图片：apps/color_change/test.jpg

前端资源：static/...

- static/html/color_ch.html

    目前注释了3种代码：css、js、django模板代码（其实都是django模板代码）

    css和js的路径都改为了本地路径，方便本地离线调试...

    本地在线调试把注释的代码不注释，把现在的css和js引用的代码注释掉即可