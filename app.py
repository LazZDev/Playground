# Import Flask to allow us to create our app
from flask import Flask, render_template # added render_template!

# Create a new instance of the Flask class called "app"
app = Flask(__name__)

# The "@" decorator associates this route with the function immediately following
@app.route("/play")
def play_one():
    """Render play.html template with default number of boxes."""
    return render_template("play.html",num=3,color="blue")

# The "@" decorator associates this route with the function immediately following
@app.route("/play/<int:num>")
def play_two(num):
    """Render play.html template with specified number of boxes."""
    return render_template("play.html", num=num, color="blue")

# The "@" decorator associates this route with the function immediately following
@app.route("/play/<int:num>/<string:color>")
def play_three(num, color):
    """Render play.html template with specified number of boxes and color."""
    return render_template("play.html", num=num, color=color)

# Run the app in debug mode.
if __name__ == "__main__":
    app.run(debug=True)
