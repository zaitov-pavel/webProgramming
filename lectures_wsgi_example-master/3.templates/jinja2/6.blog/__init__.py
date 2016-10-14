from views import BlogRead, BlogIndex, BlogCreate, BlogDelete, BlogUpdate
from wsgi_basic_auth import BasicAuth

# third-party
import selector


def make_wsgi_app():
    passwd = {
        'admin': '123'
    }
    # BasicAuth applications
    create = BasicAuth(BlogCreate, 'www', passwd)
    update = BasicAuth(BlogUpdate, 'www', passwd)
    delete = BasicAuth(BlogDelete, 'www', passwd)

    # URL dispatching middleware
    dispatch = selector.Selector()
    dispatch.add('/', GET=BlogIndex)
    dispatch.prefix = '/article'
    dispatch.add('/add', GET=create, POST=create)
    dispatch.add('/{id:digits}', GET=BlogRead)
    dispatch.add('/{id:digits}/edit', GET=update, POST=update)
    dispatch.add('/{id:digits}/delete', GET=delete)
    return dispatch

if __name__ == '__main__':
    from paste.httpserver import serve
    app = make_wsgi_app()
    serve(app, host='0.0.0.0', port=8000)
