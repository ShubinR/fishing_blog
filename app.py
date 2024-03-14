from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/start')
def index():
    return render_template("index.html")


@app.route('/about_me')
def about_me():
    return render_template("about_me.html")


@app.route('/services')
def services():
    return render_template("services.html")


@app.route('/events')
def events():
    return render_template("events.html")


@app.route('/calendar')
def calendar():
    return render_template("calendar.html")


@app.route('/gallery')
def gallery():
    return render_template("gallery.html")


@app.route('/video')
def video():
    return render_template("video.html")


@app.route('/contacts')
def contacts():
    return render_template("contacts.html")

if __name__ == "__main__":
    app.run(debug=True)