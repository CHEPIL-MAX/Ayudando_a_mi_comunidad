from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contenido")
def contenido():
    return render_template("contenido.html")


@app.route("/registro")
def registro():
    return render_template("registro.html")


@app.route("/intereses")
def intereses():
    return render_template("intereses.html")


@app.route("/contacto")
def contacto():
    return render_template("contacto.html")


if __name__ == "__main__":
    app.run(debug=True)