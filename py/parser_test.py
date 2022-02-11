from .parser import NervousHTMLParser

p = NervousHTMLParser()

html = '''
    <html>
    <head>
    </head>
    <body>
    <div> hey </div>
    <img src="bla"/>
    <p>bla
    <span>haha</span>
    </body>
    </html>
'''

p.feed(html)

print(p.data)
