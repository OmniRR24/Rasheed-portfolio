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
    # subject = None
    # message = None
    # if request.method == 'POST':
    #     name = request.form.get('name')
    #     email = request.form.get('email')
    #     subject = request.form.get('subject').upper()
    #     description = request.form.get('desc')
    #     with SMTP('smtp.gmail.com', 587) as connection:
    #         connection.starttls()
    #         connection.login(user=USER, password=PASSWORD)
    #         connection.sendmail(from_addr=USER, to_addrs=RECEIVER, msg=f'Subject: {subject.upper()}\n\n'
    #                                                                    f'You have a new message!'
    #                                                                    f'Client-Name: {name.title()}\n'
    #                                                                    f'Client-Email: {email}\n'
    #                                                                    f'Description: {description}\n')
    #         connection.close()
    #     sent = True
        # return render_template('index.html', message_sent=sent, subject=subject, message=message)
    return render_template('index.html')


@app.route('/contact-me', methods=['GET', 'POST'])
def contact():
    sent = False
    if request.method == 'POST':
        sent = True
    return render_template('contact.html', message_sent=sent)


if __name__ == '__main__':
    app.run(debug=True)