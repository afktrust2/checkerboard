from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("checkerboard.html",row=8,col=8)

@app.route('/<int:x>')
def row(x):
    return render_template("checkerboard.html",row=x,col=8)

@app.route('/<int:x>/<int:y>')
def row_col(x,y):
    return render_template("checkerboard.html",row=x,col=y)

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def four(x,y,color1,color2):
    return render_template("checkerboard.html",row=x,col=y,color1=color1,color2=color2)


if __name__=="__main__":
    app.run(debug=True, host='localhost', port=8000)