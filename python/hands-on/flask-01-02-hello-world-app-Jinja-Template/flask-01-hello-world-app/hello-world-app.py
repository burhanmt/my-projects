from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/second')
def second():
    return 'Bize her yer trabzon'

@app.route('/third/subthird')
def third():
    return 'This is the subpage of the thirdpage'

@app.route('/fourth/<string:id>')
def fourth(id):
    return f'ID number of this page is {id}'
if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
