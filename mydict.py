class Dict(dict):
    def __init__(self, **kw):
        super().__init__(kw)
    def __getattr__(sef,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attritbute '%s'" % key)
        def __setattr__(self,key,value):
            self[key]=value
from datetime import datetime
now=datetime.now()
print(now)
from collections import namedtuple
point=namedtuple('point',['x','y'])
p=point(1,2)
p.x
p.y
import hashlib
md5=hashlib.md5()
md5.update('wwed'.encode('utf-8'))
print(md5.hexdigest())
import hmac
message=b'Hello,world!'
key=b'secret'
h=hmac.new(key,message,digestmod='MD5')
h.hexdigest()
""" import itertools
natuals=itertools.count(1)
for n in natuals:
    print(n)

ns=itertools.repeat('A',3)
natuals_new=itertools.count(1)
ns=itertools.takewhile(lambda x:x<=10,natuals)
list(ns) """
from urllib import request,parse
import ssl
try:
    context=ssl._create_unverified_context()
#   with request.urlopen('https://www.costco.ca/Elizabeth-Arden-Ceramide-Advanced-Time-Complex-Capsules.product.100296958.html',context=context) as f:
    with request.urlopen('https://api.douban.com/v2/book/2129650',context=context) as f:
        data=f.read()
        print('Status:',f.status,f.reason)
        for k,v in f.getheaders():
            print('%s:%s' % (k,v))
        print ('Data',data.decode('utf-8'))
except Exception as EX:
    print('Error',EX)
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req,context=context) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8'),context=context) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
