from flask import Flask, render_template, url_for, request, flash, session, redirect, abort

app = Flask(__name__)
app.config["SECRET_KEY"] = 'rivrbeivbruinvorniwvnioeo23ui4728'

menu = [{"name": 'installing', "url": "install-flask"},
        {"name": "the first app", "url": "first-app"},
        {"name": "feedback", "url": "contact"}]

@app.route("/index")
@app.route("/")
def index():
    print(url_for("index"))
    return render_template('index.html', menu=menu)

@app.route("/about")
def about():
    print(url_for("about"))
    return render_template('about.html', title="About site", menu=menu)

@app.route("/contact", methods=['POST', 'GET'])
def contact():

    if request.method == "POST":
        if len(request.form["username"]) > 2:
            flash("message has been sent", category="success")
        else:
            flash("error", category="error")
        print(request.form)

    return render_template("contact.html", title="feedback", menu=menu)

# proceed 404 error
@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title="page hasn't been found", menu=menu), 404


@app.route("/login", methods=["POST", "GET"])
def login():
    if "userLogged" in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == "POST" and request.form['username'] == 'vladfoxin' and request.form['psw'] == "123":
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title='autorithation', menu=menu)

@app.route('/profile/<username>')
def profile(username):

    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)

    return f"user's profile: {username}"



if __name__ == "__main__":
    app.run(debug=True)