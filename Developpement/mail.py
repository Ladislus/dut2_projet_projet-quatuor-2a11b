# from flask import Flask
# from flask_mail import Mail
#
# app = Flask(__name__)
# mail = Mail(app)
#
# from flask_mail import Message
#
# @app.route("/send/")
# def send():
#
#     msg = Message("Hello",
#                   sender="liam.demarest@orange.fr",
#                   recipients=["alexis.chauvette1654@gmail.com"])
#
#     msg.body = "testing"
#     msg.html = "<b>testing</b>"
#     mail.send(msg)
