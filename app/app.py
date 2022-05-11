from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

@app.route("/")
def root_page():
    return render_template("index.html")

@app.route("/get_user")
def user_page():
    return render_template("user.html")

@app.route("/assets/static/style.css")
def app_stylesheet():
    return redirect(url_for("static", filename="app.css"))

@app.route("/product", methods=['POST','GET'])
def product():
    if request.method == 'POST':
        nama_barang = request.form['produk']
        harga = request.form['harga']
        return "nama produk : {0}\nharga : {1}".format(nama_barang, harga)
    
    if request.method == 'GET':
        pass

@app.route("/user", methods=['GET','POST'])
def user():
    if request.method == 'GET':
        nama = request.args.get('name')
        ID = request.args.get('id')
        
        res = "Halo {0}\nid : {1}\n".format(nama, ID)
        return res, 200, {'Content-Type' : 'text/plain; charset=utf-8'}
 
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
