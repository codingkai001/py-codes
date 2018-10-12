from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random
import os
import string

FONT_DIR = 'C:\Windows\Fonts'
FONT_TYPE = 'ITCKRIST.TTF'


def random_char():
    """随机生成验证字符"""
    chars = string.ascii_letters + string.digits
    i = random.randint(0, len(chars) - 1)
    return chars[i]


def background_color():
    """随机生成浅色背景"""
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


def front_color():
    """随机生成深色前景"""
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


def add_line():
    pass


if __name__ == '__main__':
    width, height = 60 * 4, 60

    for k in range(5):
        # 创建图片对象
        image = Image.new('RGB', (width, height), (255, 255, 255))
        # 设置字体及大小
        font = ImageFont.truetype(os.path.join(FONT_DIR, FONT_TYPE), 45)

        draw = ImageDraw.Draw(image)

        # 绘制背景图片
        for x in range(width):
            for y in range(height):
                draw.point((x, y), fill=background_color())

        # 绘制验证字符
        for i in range(4):
            r, g, b = front_color()
            draw.text((60 * i + 10, 0), random_char(), font=font, fill=(r, g, b))
            # 增加干扰线条
            h = random.choice([43, 53, 59])
            for j in range(60 * i, 60 * (i + 1)):
                draw.point((j, j % h), fill=(r, g, b))
                draw.point((j, j % h + 1), fill=(r, g, b))
                draw.point((j, j % h + 2), fill=(r, g, b))

        # 验证字符部分旋转
        # for i in range(4):
        #     box = (i*60+0, 0, i*60+60, 60)
        #     region = image.crop(box).resize((80, 80))
        #     image.paste(region.rotate(random.randint(-60, 60)), (i*60-10, -10, i*60+70, 70))

        # 图片虚化
        image = image.filter(ImageFilter.BoxBlur(1))
        # image.show()
        image.save('code%d.jpg' % k, 'jpeg')
