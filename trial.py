from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/sphere-volume', methods = ['POST'])
def greet():
    # rad = request.args.get('radius', default=0, type=int)
    rad = request.form['radius']
    print(rad)
    print(type(rad))
    print(request.get_data())
    rad = int(rad)

    if rad == 0:
        return "Nope"

    pi = 3.1415926535

    volume = (4/3) * pi * (rad ** 3)

    return render_template("result.html", rad=rad, volume=volume, pi=pi)

if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="localhost", debug=True)
