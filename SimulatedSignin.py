
# �ռ�����
# import urllib
# from urllib import request
# request = urllib.request.Request('https://www.bwedu.com')
# try:
#     urllib.request.urlopen(request)
# except urllib.request.URLError as e:
#     print(e.reason)

# import urllib.parse
# import urllib.request
# from http import cookiejar
# ��ӡcookie
# cookie = cookiejar.CookieJar()
# cookiehandler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(cookiehandler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print('Name =   '+item.name)
#     print('value =  '+item.value)


# ����cookie
# filename = 'C:/Users/Administrator/Desktop/cookie.txt'
# cookie = cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard = True,ignore_expires = True)

# ����ѧУ����ϵͳ
import urllib.request
import urllib.parse
import urllib
from http import cookiejar
import http.cookiejar as cookielib
cookie = cookielib.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
opener.addheaders =[("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")]

postdata = urllib.parse.urlencode({'username':'XXXX','password':'XXXX'}).encode('utf-8')
loginurl = 'http://org.xjtu.edu.cn/openplatform/login.html'
request = urllib.request.Request(loginurl,data = postdata)
response = opener.open(request)
# cookie.save(ignore_discard = True,ignore_expires = True)
gradeurl = 'http://gmis.xjtu.edu.cn/pyxx/pygl/xscjcx/index'
grade = opener.open(gradeurl)
print(grade.read().decode('utf-8'))



