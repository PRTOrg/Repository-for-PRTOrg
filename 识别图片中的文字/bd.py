from aip import AipOcr
#百度云

""" 你的 APPID AK SK """
APP_ID = '19256901'
API_KEY = 's5hu1TTX3sD5CT4M4IzHlfel'
SECRET_KEY = 'H6f9wZgzm3jd9WCdxutDtnzxMn3oR7Lj'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    # r读取  b二进制
    with open(filePath, 'rb') as fp:
        return fp.read() #返回文件读取的内容


def get_content():
    image = get_file_content('screen.png')
    
    """ 调用通用文字识别, 图片参数为本地图片 """
    #低精度版 basicGeneral
    data = client.basicAccurate(image);
    # {'log_id': 8065709510247930404, 'words_result_num': 1, 'words_result': [{'words': '图片到本地'}]} 列表 字典
    # print(data['words_result'])
    image_content = ''
    for words in data['words_result']:
        image_content += words['words']
    # print(image_content)
    return image_content
   
#print(get_content())

""" 如果有可选参数 
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"
"""