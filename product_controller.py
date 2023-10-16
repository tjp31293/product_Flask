from model import *
from flask import request,render_template

@app.route('/product/home')
def home_html():
    return render_template('home.html')

@app.route('/product/add',methods=['GET','POST'])
def product_add():
    message=""
    if request.method =='POST':
        formdata = request.form

        if formdata:
            pid = formdata.get('prid')
            if pid:
                prodrecord = Product.query.filter_by(prodid=pid).first()

                if prodrecord:
                    prodrecord.prodid   =  pid
                    prodrecord.prodname = formdata.get('prname')
                    prodrecord.prodven  = formdata.get('prvendor')
                    prodrecord.prodcat  = formdata.get('prcat')
                    prodrecord.proddesc = formdata.get('prdesc')
                    prodrecord.prodqty  = formdata.get('prqty')
                    prodrecord.prodbarcode = formdata.get('prbcode')
                    prodrecord.prodprice   = formdata.get('prprice')
                    db.session.commit()  # update

                    message = "Update Successfully"

                    return render_template('adddproduct.html', product=Product(prodid=0, prodname='', prodven='',
                                                                               prodcat='', proddesc='', prodqty='',
                                                                               prodbarcode='', prodprice=''),message=message)
        #ADd Product
        prodid = formdata.get('prodid')
        prodname = formdata.get('prname')
        prodven = formdata.get('prvendor')
        prodcat = formdata.get('prcat')
        proddesc = formdata.get('prdesc')
        prodqty = formdata.get('prqty')
        prodbarcode = formdata.get('prbcode')
        prodprice = formdata.get('prprice')

        prod = Product(prodid=prodid,prodname=prodname,prodven=prodven,prodcat=prodcat,proddesc=proddesc,
                       prodqty=prodqty,prodbarcode=prodbarcode,prodprice=prodprice)
        db.session.add(prod)
        db.session.commit()
        message='Add Product Succcessfully'

    return render_template('adddproduct.html', product=Product(prodid=0,prodname='',prodven='',
                                            prodcat='',proddesc='',prodqty='',
                                            prodbarcode='',prodprice=''),message=message)


@app.route('/product/list',methods=['GET'])
def product_list():
    product = Product.query.all()
    return render_template('product_list.html',prod_list=product)

@app.route('/product/search',methods=['GET','POST'])
def product_search():
    product = []

    if request.method == 'POST':
        formdata = request.form
        searchby = formdata.get('searchBy')
        data = formdata.get('data')

        if searchby=='ID':
            product = Product.query.filter_by(prodid=data).all()
        elif searchby=='VENDER':
            product = Product.query.filter(Product.prodven==data).all()
        elif searchby=='CATEGORY':
            product = Product.query.filter(Product.prodcat==data).all()
        elif searchby == 'NAME':
            product = Product.query.filter(Product.prodname==data).all()


    return render_template('search_product.html',products = product)

@app.route('/product/sort',methods=['GET','POST'])
def product_sortby():
    products=[]
    if request.method == 'POST':
        formdata = request.form
        sortBy =formdata.get('sortBy')
        order1 = formdata.get('order')
        products = Product.query.all()
        isAsc = True
        if order1 == 'ASC':
            isAsc = False

        if sortBy == "ID":
            products.sort(key=lambda prod: prod.prodid, reverse=isAsc)
        elif sortBy == "NAME":
            products.sort(key=lambda prod: prod.prodname, reverse=isAsc)
        elif sortBy == "PRICE":
            products.sort(key=lambda prod: prod.prodprice, reverse=isAsc)
        elif sortBy == "VENDOR":
            products.sort(key=lambda prod: prod.prodven, reverse=isAsc)
    return render_template('sortproducts.html', products=products)

@app.route('/product/delete/<int:pid>',methods=['GET','POST'])
def product_delete(pid):
    productrecprd = Product.query.filter_by(prodid=pid).first()
    if productrecprd:
        db.session.delete(productrecprd)
        db.session.commit()
        product = Product.query.all()
        return render_template('product_list.html', prod_list=product)



@app.route('/product/update/<int:pid>',methods=['GET','POST'])
def product_update(pid):
    productrecprd  = Product.query.filter_by(prodid=pid).first()

    return render_template('adddproduct.html', product=productrecprd)

