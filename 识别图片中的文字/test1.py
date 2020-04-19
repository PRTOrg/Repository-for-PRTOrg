import keyboard
from PIL import ImageGrab # pip install pillow
import time
from bd import get_content
'''
1.保存截图图片到本地
2.识别本地图片
'''
def screen():
    # windows截图 shift+win+s
    print('开始截图')
    # 阻塞程序运行
    keyboard.wait(hotkey='shift+win+s')
    # 保存截图
    
    keyboard.wait(hotkey='enter')   
    print('结束截图')
    # 当电脑读取图片速度大于代码运行速度时回读取错误，读取到的是上一次的图片
    time.sleep(0.5)
    # 读取剪切板里的图片
    image = ImageGrab.grabclipboard()
    # print(image)
    # 保存下来
    image.save('screen.png') 
    
# 调用2次
for _ in range(1):
    screen()
    data = get_content()
    print(data)

#将识别的内容写入文件
def save_to_file(file_name, contents):
    fh = open(file_name, 'w')
    fh.write(contents)
    fh.close()

save_to_file('text.txt', data)


