# import urllib.request
# request = urllib.request.Request("http://www.baidu.com")
# response = urllib.request.urlopen(request)
# print(response.read())
import urllib
from urllib import request
from urllib import parse
from urllib.request import urlopen
values = {'username':'605165087@qq.com','password':'XXXX'}
data = parse.urlencode(values).encode('utf-8')
url = 'http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
request = request.Request(url,data)
response = urlopen(request)
print(response.read().decode())




