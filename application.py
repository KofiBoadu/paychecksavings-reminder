from flask import Flask


application= Flask(__name__)
application.config.from_object(__name__)



application.route('/',methods=["GET"])
def hello():
	return "HELLO THANKS FOR SEEING ME"
