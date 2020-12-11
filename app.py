from flask import Flask 

app = Flask(__name__) 

@app.route('/') 
def index(): 
    return "<h1>Hello World!</h1>" 

@app.route('/mamae') 
@app.route('/alo')
def alo(): 
    return "<h1>Alô Mamãe!</h1>" 

if __name__ == '__main__': 
    app.run() 