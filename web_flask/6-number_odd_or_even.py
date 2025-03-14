
""" This script starts a Flask web application.
     Routes: / - display “Hello HBNB!”
     Port 5000
     listening on 0.0.0.0
 """

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Display “Hello HBNB!” """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display “HBNB” """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Display “C” followed by the value of the text variable """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """ Display “Python” followed by the value of the text variable """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Display “n is a number” only if n is an integer """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def var_num_template(n):
        """
            function to display number in html page
        """
        return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def var_num_even_odd(n):
        """
            function to display even or odd number
        """
        return render_template("6-number_odd_or_even.html", n=n)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
