from flask import Flask

#Creating Flask app
app = Flask(__name__)

books = [
    { 'name':'python','author':"Author1",'price':240},
    { 'name':'java','author':"Author2",'price':300},
    { 'name':'C','author':"Author3",'price':500}
]

@app.route('/')

def home():
    return "<hl>Home Page</h1>"

@app.route('/books')
def get_books():
    global books
    return {'books':books}

@app.route('/books/<name>')

def get_book(name):
    global books
    output_book = []
    for book in books:
        if name== book['name'].lower():
            output_book.append(book)
    return {'result':output_book}


if __name__=="__main__":
    app.run(debug=True)

