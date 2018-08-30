from flask import Flask

app = Flask (__name__) 
@app.route('/url')
def homepage():
    return 'welcome to king'

if  __name__ == "__main__":
    app.run(debug=True)
