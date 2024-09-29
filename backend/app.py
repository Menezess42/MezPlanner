from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"


@app.route("/hello")
def hello():
    return "hello world"


# url processors (urls variables). You can use this to handle diferent routes
# in the same function
@app.route('/greet/<name>')
def greet(name):
    if name == "ariel":
        return f"Hello {name} hard balls"
    else:
        return f"hello {name}, u pish of shit"


# url processors (urls variables)> Can also be strong type, so in this exemple
# i saying that number1 and 2 is a int
# if I pass anything other than int, the return will be "NOT FOUND"
@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f'{number1}+{number2}=={number1+number2}'


@app.route('/handle_url_params')
def handle_params():
    # return str(request.args)
    # if I return the string version of request.args without paramters u se
    # that is a empty imutable dictionary.
    # But if I pass a paramter like /handle_url_params?name=mike&greeting=Hello
    # than u get ImmutableMultiDict([('name', 'mike'), ('greeting', 'hello')])

    # You can use this request.args to .get information from URL and return
    # formated like
    greeting = request.args.get('greeting')
    name = request.args.get('name')
    #### return f'{greeting} Sr. {name}'

    # but if one of this args go missing, we get a bad request so is important
    # to check if is not missing, like
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        return f'{greeting} Sr. {name}'
    else:
        return "Missing paramters !!!"

# By default all the routes is GET, to use other types of routes you have to
# specify.
@app.route('/hello', methods=['POST'])
def hello():
    return "Hello POST"


if __name__ == '__main__':
    app.run(debug=True)
