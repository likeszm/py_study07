#文件操作


#编解码
"""
#编码
str1 = "你好"

print(f"str1  ={str1}")
print(f"encode={str1.encode('utf8')}")
print(f"encode={str1.encode('gbk')}")

#解码
print(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode('utf8'))
"""

#unicode转义字符
"""
print("测试".encode('unicode-escape'))
print('\u6d4b\u8bd5')
"""

#ASCII方式
"""
print( b'\xb0\xd7\xd4\xc2\xba\xda\xd3\xf0'.decode('gbk') )

a = b'hello,123'
print(a.hex())
print( bytes.fromhex('68656c6c6f2c313233') )
"""

#文件写入
"""
file = open('C:\ST\新建文本文档.txt','w')
file.write('hello word! 测试成功')
file.close()
"""

#文件读取
"""
file = open('C:\ST\新建文本文档.txt')
temp = file.read()
print(f"type of temp: {type(temp)}")
print(temp)
file.close()
"""

"""
file = open('C:\ST\新建文本文档.txt')
temp = file.read(4)
print('1:' + temp)
temp = file.read(4)
print('2:' + temp)
temp = file.read(4)
print('3:' + temp)
file.close()
"""

"""
file = open('C:\ST\新建文本文档.txt')
list1 = file.readline()
print(list1)
for index,read in enumerate(list1) :
    print(f"第{index}个元素为:{read}")

file.close()

"""


#作业
#获取内容
file = open('0013_a1.txt',encoding = 'utf8')
temp = file.read()
file.close()
print( "读取内容:" + temp)
#去掉换行
list1 = temp.splitlines()
list2 = []
for i in list1 :
    if i != '' :
        list2.append(i)
print( "初次处理", list2)
#获取所需内容
anser = []
for i in list2 :
    list_ = i.split(':')
    name = list_[0].strip()
    age = list_[1].strip()
    if int(age) > 50 :
        anser.append(name)
print( "处理结果:" , anser)
#填入内容
str = ''
for i in anser :
    str += i + ' '
file = open('0013_a1.txt','a',encoding = 'utf8')
print("写入内容:" + str)
file.write("\n\n大于50岁的人有: "+str)
print("操作完成")

