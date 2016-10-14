from models import ARTICLES


class BaseBlog(object):

    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response


class BaseArticle(BaseBlog):

    def __init__(self, *args):
        super(BaseArticle, self).__init__(*args)
        article_id = self.environ['wsgiorg.routing_args'][1]['id']
        (self.index,
         self.article) = next(((i, art) for i, art in enumerate(ARTICLES)
                               if art['id'] == int(article_id)),
                              (None, None))


class BlogIndex(BaseBlog):

    def __iter__(self):
        self.start('200 OK', [('Content-Type', 'text/html')])
        yield b'<h1>Simple Blog</h1>'
        yield b'<a href="/article/add">Add article</a>'
        yield b'<br />'
        yield b'<br />'
        for article in ARTICLES:
            yield str.encode(
                '''
                {0} - (<a href="/article/{0}/delete">delete</a> |
                <a href="/article/{0}/edit">edit</a>)
                <a href="/article/{0}">{1}</a><br />
                '''.format(
                    article['id'],
                    article['title']
                )
            )


class BlogCreate(BaseBlog):

    def __iter__(self):
        if self.environ['REQUEST_METHOD'].upper() == 'POST':
            from urllib.parse import parse_qs
            values = parse_qs(self.environ['wsgi.input'].read())
            max_id = max([art['id'] for art in ARTICLES])
            ARTICLES.append(
                {'id': max_id+1,
                 'title': values[b'title'].pop().decode(),
                 'content': values[b'content'].pop().decode()
                 }
            )
            self.start('302 Found',
                       [('Content-Type', 'text/html'),
                        ('Location', '/')])
            return

        self.start('200 OK', [('Content-Type', 'text/html')])
        yield b'<h1><a href="/">Simple Blog</a> -> CREATE</h1>'
        yield b'''
            <form action="" method="POST">
                Title:<br>
                <input type="text" name="title"><br>
                Content:<br>
                <textarea name="content"></textarea><br><br>
                <input type="submit" value="Submit">
            </form>
            '''


class BlogRead(BaseArticle):

    def __iter__(self):
        if not self.article:
            self.start('404 Not Found', [('content-type', 'text/plain')])
            yield b'not found'
            return

        self.start('200 OK', [('Content-Type', 'text/html')])
        yield b'<h1><a href="/">Simple Blog</a> -> READ</h1>'
        yield str.encode(
            '<h2>{}</h2>'.format(self.article['title'])
        )
        yield str.encode(self.article['content'])


class BlogUpdate(BaseArticle):

    def __iter__(self):
        if self.environ['REQUEST_METHOD'].upper() == 'POST':
            from urllib.parse import parse_qs
            values = parse_qs(self.environ['wsgi.input'].read())
            self.article['title'] = values[b'title'].pop().decode()
            self.article['content'] = values[b'content'].pop().decode()
            self.start('302 Found',
                       [('Content-Type', 'text/html'),
                        ('Location', '/')])
            return
        self.start('200 OK', [('Content-Type', 'text/html')])
        yield b'<h1><a href="/">Simple Blog</a> -> UPDATE</h1>'
        yield str.encode(
            '''
            <form action="" method="POST">
                Title:<br>
                <input type="text" name="title" value="{0}"><br>
                Content:<br>
                <textarea name="content">{1}</textarea><br><br>
                <input type="submit" value="Submit">
            </form>
            '''.format(
                self.article['title'],
                self.article['content']
            )
        )


class BlogDelete(BaseArticle):

    def __iter__(self):
        self.start('302 Found',  # '301 Moved Permanently',
                   [('Content-Type', 'text/html'),
                    ('Location', '/')])
        ARTICLES.pop(self.index)
        yield b''
