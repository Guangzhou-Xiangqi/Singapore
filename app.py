from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Set a secret key for session management


@app.route('/')
def index():
    authenticated = session.get('authenticated', False)
    return render_template('index.html', authenticated=authenticated)


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Check username and password
    if username == 'admin' and password == 'password':
        session['authenticated'] = True
        return render_template('index.html', authenticated=True)
    else:
        return render_template('index.html', authenticated=False, error=True)


@app.route('/logout')
def logout():
    session.pop('authenticated', None)
    return render_template('index.html', authenticated=False)


if __name__ == '__main__':
    app.run()
