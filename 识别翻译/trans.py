from tkinter import Button, Text
import pyperclip.paste
import shibie
import tkinter.messagebox
import requests

class MyCapture:
    def __init__(self):
#        设置按钮及其摆放位置
        self.A = Button(window, text ="截图", command = self.create)
        self.A.place(x=70, y=20, width=90, height=30)
        self.B = Button(window, text ="图像识别",command = self.show)
        self.B.place(x=255, y=20, width=90, height=30)
        self.C = Button(window, text ="翻译",command=self.translate_cmd)
        self.C.place(x=440, y=20, width=90, height=30)
        self.D = Button(window, text ="退出", command = window.destroy)
        self.D.place(x=500, y=260, width=90, height=30)
        self.E = Text(window)
        self.E.place(x=50, y=70, width=500, height=180)

#    截图提示窗口
    def create(self):
        tkinter.messagebox.showinfo( "Screenshot tips", "请截图！(可使用QQ截图或win10自带截图方式shift+win+s)")
            
    def get_information(self):
#        text3.discriminate()
#        x = pyperclip.paste()
        y1 = self.E.get(1.0,2.0)
#        print(y1)
        return y1

    def show(self):
        shibie.save()
        shibie.discriminate()
        x1 = pyperclip.paste()
#        y = self.E.get(1.0,2.0)
#        print(len(y))
        y2 = self.get_information()
#        y2 = show2()
        if (len(y2)==1):
            self.E.insert(1.0,x1)
        else:
            self.E.delete(1.0,2.0)
            self.E.insert(1.0,x1)
            
            
    '''爬取有道云翻译'''
    def get_trans_result(self):
        # 获取用户输入的单词 苹果。梨子。
        content = self.get_information()
        content = content.strip()   # 去空格
        if content=="":
            tkinter.messagebox.showinfo('Tips','Please enter the content to be translated')
        else:
            url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    
            data={}
            data['i']=content
            data['from']='AUTO'
            data['to']='AUTO'
            data['smartresult']='dict'
            data['client']='fanyideskweb'
         
            data['doctype']='json'
            data['version']='2.1'
            data['keyfrom']='fanyi.web'
            data['action']='FY_BY_CLICKBUTTION'
            
            # Response [200] 状态码 请求成功 反爬
            result = requests.post(url,data=data).json()  
            trans = ''
            for res in result['translateResult'][0]:
                trans += res['tgt']
            return trans
 
        
    def translate_cmd(self):
        x2=self.get_trans_result()
        y3 = self.get_information()
#        y2 = show2()
        if (len(y3)==1):
            self.E.insert(1.0,x2)
        else:
            self.E.delete(1.0,2.0)
            self.E.insert(1.0,x2)
#        print(x)


if __name__ == '__main__':  
    # 创建主窗口
    window = tkinter.Tk()
    # 命名主窗口
    window.title('截图翻译')
    # 指定主窗口位置与大小
    window.geometry('600x300')
    window.resizable(0, 0)
    c1=MyCapture()
#    a=c1.show()
#    print(a)
    window.mainloop()