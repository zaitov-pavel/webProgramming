from views import BlogRead, BlogIndex, BlogCreate, BlogDelete, BlogUpdate
from wsgi_basic_auth import BasicAuth

# third-party
import selector


def make_wsgi_app():
    adm_group = {
        'adm1': '1',
        'adm2': '2'
    }
    md_group = {
        'md1': '1',
        'md2': '2'
    }
    users_group = {
        'us1': '1',
        'us2': '2'
    }

    create_group = {}
    for user in [adm_group, md_group, users_group]:
        create_group.update(user)

    delete_group = adm_group.update(md_group)

    # BasicAuth applications
    create = BasicAuth(BlogCreate, 'www', create_group)
    update = BasicAuth(BlogUpdate, 'www', md_group)
    delete = BasicAuth(BlogDelete, 'www', delete_group)

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

    app = make_wsgi_app()

    from whitenoise import WhiteNoise
    app = WhiteNoise(app)
    app.add_files('./static/', prefix='static/')

    from paste.httpserver import serve
    serve(app, host='0.0.0.0', port=8000)
