# 导入requests库
import requests
# 输入一个url
url = "http://www.baidu.com"
# 向网页发送请求
r = requests.get(url)
# 为防止出现乱码，手动设置编码格式
r.encoding = "utf8"
# 打印str类型数据
print(r.text)
# 打印bytes类型的响应源码
print(r.content)
# 可以进行decode操作，操作后返回结果与r.text相同
print(r.content.decode())
