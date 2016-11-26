from wsgiref.simple_server import make_server
from pyramid.response import Response
from pyramid.config import Configurator
from jinja2 import Environment, FileSystemLoader


def index(request):
    env = Environment(loader=FileSystemLoader('C:\\Users\Admin\Desktop\webProgramming'))
    templ = env.get_template("/index.jinja")
    return Response(templ.render(infoString = "You see 'index.jinja' file!",
                                finalLine = "Unfortunately, 'index.jinja' file is ended:( Link to a file about me:"))

def about(request):
    env = Environment(loader=FileSystemLoader('C:\\Users\Admin\Desktop\webProgramming'))
    templ = env.get_template("about/aboutme.jinja")
    return Response(templ.render(infoString = "There should be information about me...",
                                finalLine = "But information is absent. Come back to the file 'index.jinja':"))

def main():
    config = Configurator() #создаем конфиг приложения

    config.add_route('index', '/index.jinja')
    config.add_route('about', '/about/aboutme.jinja')

    config.add_view(index, route_name='index')
    config.add_view(about, route_name='about')
    
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8000, app)
    server.serve_forever()

if __name__ == "__main__":
    main()