from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def touchscreen():
    if request.method == 'POST':
        if request.form.get('input') == 'VALUE1':
            # pomp functie komt hier
            pass  # unknown
        elif request.form.get('input') == 'VALUE2':
            # pomp functie komt hier
            pass
        elif request.form.get('input') == 'VALUE3':
            # pomp functie komt hier
            pass
        elif request.form.get('input') == 'VALUE4':
            # pomp functie komt hier
            pass
        return render_template('home.html')

    elif request.method == 'GET':
        return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
