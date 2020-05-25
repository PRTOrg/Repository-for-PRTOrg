from aip import AipOcr
import pyperclip.copy
import tkinter.messagebox
from PIL import ImageGrab
import time.sleep

def save():
    try:
        # 读取剪切板图片
        image = ImageGrab.grabclipboard()
        time.sleep(0.5) # 防止获取到的是上一次的图片
        image.save('t.png')
    except:
        tkinter.messagebox.showinfo('Picture content is empty!')

    
def discriminate():
    with open('t.png','rb') as f:
        ima = f.read()
    app_id = '19705657'
    api_key = 'kor82Eq9OeExbll1bTV9rmtC'
    secret_key = 'WqQRMYYrGnBPLE6BjC9vxYwT7PCm2BjN'
    
    ''' 调用百度ai精准文字识别'''
    
    client = AipOcr(app_id, api_key, secret_key)
    data = client.basicAccurate(ima)
    # print(data['words_result'])
    result = ""
    for words in data['words_result']:
        result = result+" "+words['words']
    pyperclip.copy(result)