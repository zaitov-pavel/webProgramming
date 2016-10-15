from wsgiref import simple_server

class Middleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        top = "<div class='top'>Middleware TOP</div>\n"
        bottom = "<div class='botton'>Middleware BOTTOM</div\n"

        page = self.app(environ, start_response)
        if page == 'File not found!':
            return [page.encode("utf-8")]

        page = page.decode("utf-8")
        result = ""
        result += page[:page.rfind("<body>")]
        result += top
        result += page[page.rfind("<body>"):page.find("</body>")]
        result += bottom
        result += page[page.find("</body>"):]
        return [result.encode("utf-8")]

def simple_app(environ, start_response):
    result = ""
    path = environ['PATH_INFO']
    if path == "/index.html" or path == "/" or path == "/about/aboutme.html":
        start_response("200 OK", [('Content-Type', 'text/html')])
        if path == "/":
            path = "/index.html"
        result = open(path[1:]).read().encode('utf-8')
    else:
        start_response("404 Not Found", [('Content-Type', 'text/html')])
        result = 'File not found!'
    return result

def main():
	server = simple_server.WSGIServer(
	            ('localhost', 8080),
	            simple_server.WSGIRequestHandler,
	        )
	app = Middleware(simple_app)
	server.set_app(app)
	server.serve_forever()

if __name__ == "__main__":
	main()