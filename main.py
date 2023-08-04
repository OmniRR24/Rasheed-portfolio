from flask import Flask, render_template, request
from smtplib import SMTP
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

USER = os.environ.get('USER')
PASSWORD = os.environ.get('AUTH')
RECEIVER = os.environ.get('RECIPIENT')


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/contact-me', methods=['GET', 'POST'])
def contact():
    sent = False
    if request.method == 'POST':
        sent = True
    return render_template('contact.html', message_sent=sent)


if __name__ == '__main__':
    app.run(debug=True)