import requests
import json

class YunPian(object):
    def __init__(self, api_key):
        self.api_key = api_key
        # 云片网的接口地址
        self.single_send_url = 'https://sms.yunpian.com/v2/sms/single_send.json'

    def send_sms(self, code, mobile):
        parmas = {
            'apikey': self.api_key,
            'mobile': mobile,
            'text': '【生鲜网】您的验证码是{code}'.format(code=code),   # 云片网审核的模板内容
        }

        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        return re_dict

if __name__ == '__main__':
    yun_pian = YunPian("45464f646848sfdsf")
    yun_pian.send_sms("2018", "151********")