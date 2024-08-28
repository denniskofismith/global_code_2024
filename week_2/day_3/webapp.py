from flask import Flask , render_template


app = Flask(__name__)

@app.route('/')
def index():
    #return '<p>Hello World!</p> <p> 17th May </p> <p>Watch Chelsea Play</p>'
    return render_template('index.html')

@app.route('/whereami')
def whereami():
    return 'Ghana!'

@app.route('/foo/<name>')

def foo(name):
    print(name)
    return render_template('index2.html',to=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

