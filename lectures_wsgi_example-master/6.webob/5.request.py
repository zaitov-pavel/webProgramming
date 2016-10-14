from webob import Request
req = Request.blank('/test?check=a&check=b&name=Bob')

# Set POST
req.method = 'POST'
req.body = b'name=Vasya&email=vasya@example.com'

print(req.params)
print(req.params.getall('check'))
print(req.params['email'])
print(req.params['name'])
