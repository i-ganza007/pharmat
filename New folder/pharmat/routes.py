from flask import Flask , render_template  

app = Flask(__name__)
app.config['SECRET_KEY'] = 'eb7e108c791ecce8e19d'

products = [
    {'name':'Gloves',
     'image':'',
     'descr':'Some quick example text to build on the card title and make up the bulk of the card content.'},
   {'name':'kneepads',
     'image':'',
     'descr':'Some quick example text to build on the card title and make up the bulk of the card content.'},
    {'name':'socks',
     'image':'',
     'descr':'Some quick example text to build on the card title and make up the bulk of the card content.'}
]


# Use Modal if user wants to login without an account to notify them of the change

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',products=products)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/new_products')
def new_products():
    return render_template('new-products.html')

if __name__ == '__main__':
    app.run(debug=True)