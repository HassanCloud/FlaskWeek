from flask import Flask, render_template

app = Flask(__name__)

@app.route('/ben')
def ben():
    return render_template('ben.html')

@app.route('/harry')
def harry():
    return render_template('harry.html')

@app.route('/users')
def users():
    return render_template('users.html', users=["en", "harry", "bob", "jay", "matt", "bill"])    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

