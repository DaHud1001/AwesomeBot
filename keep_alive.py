#code to connect uptimerobot.com to this repl to refresh it every 5 mins to keep it online
import flask
import threading
from flask import Flask
from threading import Thread
import random
app = Flask('')

@app.route('/')
def home():
	return 'awesomebot do be smart doe'

def run():
  app.run(
		host='0.0.0.0',
		port=random.randint(2000,9000)
	)

def keep_alive():
	'''
	Creates and starts new thread that runs the function run.
	'''
	t = Thread(target=run)
	t.start()
'''
app = Flask("")

@app.route("/")
def home():
    return "awesomebot do be smart doe"

def run():
    app.run(host = "0.0.0.0", port = 8080)

def keep_alive():
    t = Thread(target = run)
    t.start()
'''