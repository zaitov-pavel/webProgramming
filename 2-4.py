from webob import Request

requests = []

request21 = Request({
	'REQUEST_METHOD':'GET',
	'PATH_INFO': '/страница',
	'HTTP_HOST': 'ru.wikipedia.org',
	'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9b5) Gecko/2008050509\nFirefox/3.0b5',
	'Accept': 'text/html',
	'Connection': 'close',
	'wsgi.url_scheme': 'http'})
requests.append(request21)

request31 = Request({
	'REQUEST_METHOD':'GET',
	'PATH_INFO': '/ip',
	'HTTP_HOST': 'httpbin.org',
	'Accept': '*/*',
	'wsgi.url_scheme': 'http'})
requests.append(request31)

request32 = Request({
	'REQUEST_METHOD': 'GET',
	'PATH_INFO': '/get',
	'HTTP_HOST': 'httpbin.org', 
	'Accept': '/',
	'QUERY_STRING': 'foo=bar&1=2&2/0&error=True',
	'wsgi.url_scheme': 'http'})
requests.append(request32)

request33 = ({
	'REQUEST_METHOD': 'POST',
	'PATH_INFO': '/post',
	'HTTP_HOST': 'httpbin.org',
	'Accept': '/',
	'QUERY_STRING':'foo=bar&1=2&2%2F0=&error=True',
	'Content - Length': '35',
	'Content - Type': 'application / x - www - form - urlencoded',
	'wsgi.url_scheme': 'http'})
requests.append(request33)

request34 = ({
	'REQUEST_METHOD':'GET',
	'PATH_INFO': '/cookies/set',
	'HTTP_HOST': 'httpbin.org',
	'Accept': '/',
	'QUERY_STRING': 'country=Ru',
	'wsgi.url_scheme': 'http'})
requests.append(request34)

request35 = ({
	'REQUEST_METHOD': 'GET',
	'PATH_INFO': '/cookies',
	'HTTP_HOST': 'httpbin.org',
	'Accept': '/',
	'wsgi.url_scheme': 'http'})
requests.append(request35)

request36 = ({
	'REQUEST_METHOD': 'GET',
	'PATH_INFO': '/redirect/4',
	'HTTP_HOST': 'httpbin.org',
	'Accept': '/',
	'wsgi.url_scheme': 'http'})
requests.append(request36)

request4 = ({
	'REQUEST_METHOD': 'POST',
	'PATH_INFO': 'post',
	'HTTP_HOST': 'httpbin.org',
	'Accept': 'application/x-www-form-urlencoded',
	'QUERY_STRING': 'firstname=Pavel&lastname=Zaitov&group=FO340001&message=HelloWorld',
	'wsgi.url_scheme': 'http'})
requests.append(request4)

for req in requests:
	response = req.get_response()
	response.content_type = 'text/plain'
	response.charset = 'utf-8'
	print(response)
	print("=====================")
	print()