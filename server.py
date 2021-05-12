"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Home Page</title>
      </head>
      <body>
        <a href="/hello">Let's get started!</a>
      </body>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <p>What's your name? <input type="text" name="person"></p>
         
          Please select a compliment:
          <br>
          <br>
           <input type="radio" name="compliment" value="cool">Cool<br>
           <input type="radio" name="compliment" value="great">Great<br>
           <input type="radio" name="compliment" value="awesome">Awesome<br>
           <input type="radio" name="compliment" value="fire">Fire
          <br>
          <br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet') 
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    player = player.title()

    #compliment = choice(AWESOMENESS)
    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """.format(player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
