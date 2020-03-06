import json

with open('filename.json','w') as file:#with open()中第一个引号内的内容是存放的路径与文件
    #这里选用工作目录下叫做filename.json的文件，如果不存在将被创建，并将里面所有的内容都清空，重新
    #写入，“w”就是write的缩写
    json.dump('这是存在json文件里面的内容',file)
    
with open('filename.json','r') as file:#第一个引号内是路径，如果不存在将会报错，因为第二个
    #参数是“r”，也就是read的缩写，就是读取文件内容
    content = json.load(file)

print(content)
input()
