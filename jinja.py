from wsgiref import simple_server
from jinja2 import Environment, FileSystemLoader

# class Middleware:
#     def __init__(self, app):
#         self.app = app

#     def __call__(self, environ, start_response):
#         top = "<div class='top'>Middleware TOP</div>\n"
#         bottom = "<div class='botton'>Middleware BOTTOM</div\n"

#         page = self.app(environ, start_response)
#         print(page)
#         if page == 'File not found!':
#             return [page.encode("utf-8")]

#         page = page.decode("utf-8")
#         result = ""
#         result += page[:page.rfind("<body>")]
#         result += top
#         result += page[page.rfind("<body>"):page.find("</body>")]
#         result += bottom
#         result += page[page.find("</body>"):]
#         return [result.encode("utf-8")]

def simple_app(environ, start_response):
    env = Environment(loader=FileSystemLoader('C:\\Users\\Алена\Desktop\WebZaitov'))
    template = None
    path = environ['PATH_INFO']
    print(path)
    if path == "/index.html" or path == "/":
        start_response("200 OK", [('Content-Type', 'text/html')])
        template = env.get_template('/index.html')
    elif path == "/about/aboutme.html":
        start_response("200 OK", [('Content-Type', 'text/html')])
        template = env.get_template('about/aboutme.html')
    else:
        start_response("404 Not Found", [('Content-Type', 'text/html')])
        return ["404 Not Found".encode("utf-8")]
    print(template)
    return [template.render().encode('utf-8')]

def main():
    server = simple_server.WSGIServer(
                ('localhost', 8000),
                simple_server.WSGIRequestHandler,
            )
    server.set_app(simple_app)
    server.serve_forever()

if __name__ == "__main__":
    main()