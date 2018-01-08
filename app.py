import glob
from flask import Flask, request, render_template, request, url_for, redirect, Markup, Response, send_file, send_from_directory, make_response, jsonify
import csv
import sqlite3 as lite
import requests
app = Flask(__name__)

@app.route('/Jan1/', methods=['GET'])
def Jan1():
	import Jan1
	return render_template("Jan1.html", DATABASE=Jan1.genDatabase(), BUSNUM="4012715")
#This is template for all sites

@app.route('/', methods=['GET'])
def index():
	return render_template("index.html")

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8000)