from flask import Flask, jsonify
import mysql.connector

app=Flask(__name__)

@app.route("/")
def home():
  return "Flask And MYSQl Docker APP"

@app.route("/employees")
def employees():
  connection=mysql.connector.connect(
    host="mysql",
    user="admin",
    password="cnt1231",
    database="Employees"
  )

  cursor=connection.cursor()

  cursor.execute("SELECT * FROM Employees")

  data=cursor.fetchall()

  cursor.close()
  connection.close()

  return jsonify(data)

app.run(host="0.0.0.0",port=5000)
