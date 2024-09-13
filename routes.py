from flask import Flask , render_template  

app = Flask()


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

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