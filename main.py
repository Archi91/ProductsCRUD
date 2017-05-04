from model.product import Product
from flask import Flask, render_template, redirect, url_for, request, flash

app = Flask(__name__)

@app.route('/')
@app.route('/products/')
def index():
    products = Product.get_all_products()
    return render_template('index.html', products=products)

@app.route('/products/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        description = request.form['description']
        if request_validate(name, price, description):
            Product.add_product(name, price, description)
            return redirect(url_for('index'))

    return render_template('add_product.html')

@app.route('/products/:<id>/delete/')
def delete_product(id):
    Product.delete_product(id)
    return redirect(url_for('index'))


def request_validate(name, price, description):
    validator = True
    if not name:
        validator = False
    if not price or float(price) < 0:
        validator = False
    if not description:
        validator = False
    return validator



if __name__ == '__main__':
    app.secret_key = "SECRET_KEY"
    app.run(debug=True, host='0.0.0.0')