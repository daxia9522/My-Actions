import requests
import time
#import hmac
#import hashlib
#import base64
import json
import os
#import urllib.parse

class sendNotify:
    # Server酱
    SCKEY = os.environ.get('PUSH_KEY', '')

    @staticmethod
    def serverNotify(text, desp):
        if sendNotify.SCKEY:
            url = f'https://sctapi.ftqq.com/{sendNotify.SCKEY}.send'
            desp = desp.replace("\n", "\n\n") if "\n" in desp else desp
            data = {'text': text, 'desp': desp}
            
            try:
                response = requests.post(url, data=data).json()
                if response['code'] == 0:
                    print('\nServer酱发送通知消息成功\n')
                elif response['code'] == 40001:
                    print('\nPUSH_KEY 错误\n')
                else:
                    print('\n发送通知调用API失败\n')
            except Exception as e:
                print(f'通知发送失败: {e}')
        else:
            print('\n您未提供Server酱的SCKEY，取消微信推送消息通知\n')

    @staticmethod
    def send(**kwargs):
        title = kwargs.get("title", "")
        msg = kwargs.get("msg", "")
        sendNotify.serverNotify(title, msg)

# 如果你需要在本文件中直接测试：
# if __name__ == "__main__":
#     sendNotify.send(title='测试标题', msg='测试消息内容')

