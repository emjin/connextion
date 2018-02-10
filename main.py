from flask import Flask
app = Flask(__name__)

@app.route('/')
def run_file():
  f=open("index.html",'r')
  f_read = f.read()
  f.close()
  return f_read

if __name__ == '__main__':
  app.run()
