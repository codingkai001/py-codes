from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import string
import math
from datetime import datetime
import os

"""中文+字母+数字字符生成验证码"""
ASCII = 0
CHN_ASCII = 1
RVS_UNICODE = 2
CHR_WIDTH = 60
SAVE_DIR = "E:\代码\Python\LearnPython\scripts/"
FONT_PATH = "C:\Windows\Fonts\FZSTK.TTF"


def front_color():
    """随机生成深色前景"""
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


def background_color():
    """随机生成浅色背景"""
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


def random_chr(mode=ASCII):
    if mode == ASCII:
        chars = string.ascii_letters + string.digits
        i = random.randint(0, len(chars) - 1)
        return chars[i]
    elif mode == CHN_ASCII or mode == RVS_UNICODE:
        return chr(random.randint(0X4E00, 0X9FA5))
    else:
        return None


class VrfCode:

    def __init__(self, chr_cnt=4, mode=ASCII, path=SAVE_DIR):
        """
        初始化验证码的字符数和模式
        :param chr_cnt: 验证码组成的字符数
        :param mode: 0代表ASCII字符（字母和数字）、1代表中文字符和ASCII字符（字母和数字）、2代表1的部分字符倒置
        """
        self.chr_cnt = chr_cnt
        self.mode = mode
        self.path = os.path.join(path, datetime.now().strftime("%Y%m%d%H%M%S%f") + '.jpg')
        self.width = CHR_WIDTH * chr_cnt
        self.height = CHR_WIDTH
        self.font = ImageFont.truetype(FONT_PATH, 45)
        self.image = Image.new("RGB", (self.width, self.height), (255, 255, 255))
        self.draw = ImageDraw.Draw(self.image)

    def draw_background(self):
        """
        绘制浅色RGB背景图层
        :return:
        """
        for x in range(self.width):
            for y in range(self.height):
                self.draw.point((x, y), fill=(background_color()))

    def draw_char(self):
        """
        绘制深色验证字符
        :return:
        """
        if self.mode == ASCII:
            "绘制字母和数字字符"
            for i in range(self.chr_cnt):
                self.draw.text((CHR_WIDTH * i + 10, 0), random_chr(mode=ASCII), font=self.font, fill=(front_color()))
            self.image = self.image.filter(ImageFilter.BoxBlur(2))
        elif self.mode == CHN_ASCII:
            "绘制中文、字母和数字字符"
            for i in range(self.chr_cnt):
                self.draw.text((CHR_WIDTH * i + 10, 0), random_chr(mode=CHN_ASCII), font=self.font,
                               fill=(front_color()))

        elif self.mode == RVS_UNICODE:
            "绘制中文、字母和数字字符，部分字符倒置"

        else:
            "异常处理"
            pass

    def save(self):
        self.image.save(self.path)


if __name__ == '__main__':
    c = VrfCode(mode=CHN_ASCII)
    c.draw_background()
    c.draw_char()
    c.save()
    # for i in range(5):
    #     print(random_chr(mode=CHN_ASCII))
