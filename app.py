from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/api', methods=['POST'])
def api():
    data1 = request.form['name']
    data2 = request.form['email']
    alldata = [data1, data2]
    print(alldata)
    return render_template('index.html', data=alldata)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
