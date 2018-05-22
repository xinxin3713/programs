from PIL import Image
import pytesseract
import requests
from io import BytesIO


# 过程
# 1 获取并解析验证码
# 2 获取表单所需要的参数，提交表单，进行登录。

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
# 创建Session会话，用来维护Cookie信息。
session = requests.session()



def get_captcha():
    """
    获取并返回验证码
    """
    captcha_url = "http://www.pss-system.gov.cn/sipopublicsearch/portal/login-showPic.shtml"
    response = session.get(captcha_url, headers=headers)
    image = Image.open(BytesIO(response.content))
    image = image.convert("L")

    image = image.point(lambda x: 0 if x < 125 else 255)
    scale = 3
    # 重新设置图片的大小。
    # 参数是一个元组，元组含有两个元素。第1个元素：图像的宽度。第2个元素：图像的高度
    image = image.resize((round(image.size[0] * scale), round(image.size[1] * scale)))
    pytesseract.pytesseract.tesseract_cmd = r'G:\Program Files\Tesseract-OCR\tesseract'
    text = pytesseract.image_to_string(image, config="--psm 7")

    try:
        text = text[:text.index("=")]
        return eval(text)
    except:
        return None

def log_in(captcha):
    """
    进行登录。
    """
    log_in_url = "http://www.pss-system.gov.cn/sipopublicsearch/wee/platform/wee_security_check"
    data = {"j_loginsuccess_url":"", "j_validation_code": captcha, "j_username": "bHN5aDE5ODQ=", "j_password":"YWJjMTIz"}
    response = session.post(log_in_url, headers=headers, data=data,)
    print(response.text)


def main():
    captcha = get_captcha()
    if captcha:
        log_in(captcha)


if __name__ == "__main__":
    main()