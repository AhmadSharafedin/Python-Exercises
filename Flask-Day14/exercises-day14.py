from flask import Flask, render_template
app = Flask(__name__)

#ex1

@app.route('/')
def HomePage():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return render_template('hello.html')


@app.route('/members')
def members():
    return render_template('members.html')


#ex2

@app.route('/score/<int:marks>')
def marks(marks):
    return render_template('marks.html', marks=marks)



#ex3 

@app.route('/index')
def score():
    return render_template('app.html')



if __name__ == '__main__':
    app.run()



