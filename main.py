from flask import Flask, render_template, request
from smtplib import SMTP

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

USER = "demoinfo4841@gmail.com"
PASSWORD = "wizeynjsmcctahwd"
RECEIVER = "kazeemrasheed3063@gmail.com"


@app.route('/', methods=['GET', 'POST'])
def home():
    sent = False
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    description = request.form.get('desc')
    if request.method == 'POST':
        with SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=USER, password=PASSWORD)
            connection.sendmail(from_addr=USER, to_addrs=RECEIVER, msg=f'Subject: {subject.upper()}\n\n'
                                                                       f'<b>You have a new message!<b>'
                                                                       f'Client-Name: {name.title()}\n'
                                                                       f'Client-Email: {email}\n'
                                                                       f'Description: {description}\n')
        sent = True
    return render_template('index.html', message_sent=sent)


if __name__ == '__main__':
    app.run(debug=True)