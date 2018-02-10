from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def run_file():
  return render_template("index.html")

'''
@app.route("/<file>.<ext>")
def one(file,ext):
    f=open(file+"."+ext,'r')
    f_read=f.read()
    f.close()
    return f_read

@app.route("/vendor/bootstrap/css/<file>.<ext>")
def two(file,ext):
    f=open("/vendor/bootstrap/css/"+file+"."+ext,'r')
    f_read=f.read()
    f.close()
    return f_read

@app.route("/vendor/font-awesome/css/<file>.<ext>")
def three(file,ext):
    f=open(file+"."+ext,'r')
    f_read=f.read()
    f.close()
    return f_read

@app.route("/vendor/simple-line-icons/css/<file>.<ext>")
def four(file,ext):
    f=open(file+"."+ext,'r')
    f_read=f.read()
    f.close()
    return f_read

@app.route("/vendor/jquery/<file>.<ext>")
def five(file,ext):
    f=open(file+"."+ext,'r')
    f_read=f.read()
    f.close()
    return f_read

@app.route("/vendor/bootstrap/js/<file>.<ext>")
def six(file,ext):
    f=open(file+"."+ext,'r')
    f_read=f.read()
    f.close()
    return f_read
'''






if __name__ == '__main__':
  app.run()
