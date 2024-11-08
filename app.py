
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route to display the login form
@app.route('/')
def home():
    return render_template('login.html')

# Route to handle the form submission
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username == 'admin' and password == 'password':
        return redirect(url_for('success'))
    else:
        return 'Invalid credentials, please try again.'

# Route for successful login
@app.route('/success')
def success():
    return 'You are logged in successfully!'

if __name__ == '__main__':
    # Running the app on port 6000
    app.run(debug=True, host='0.0.0.0', port=6000)

