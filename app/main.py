from typing import AbstractSet
from flask import Flask,redirect,request
import mysql.connector as mysql
import json



About_App = "API CREATED BY <h2>ZEESHAN AKBAR</h2> <i>KHARKIV</i><br><b>EUROPE</b>"
app = Flask(__name__)


@app.route('/')
def main():
    return About_App

@app.route("/items")
def items():
    db = mysql.connect(
  	host="mysql-50168-0.cloudclusters.net",
  	user="admin",
	  port ="18972",
  	password="TEM2JKQv",
  	database="products"
		)	
    cursor = db.cursor()
    query = "SELECT * FROM items order by serialNo"
    cursor.execute(query)
    records = cursor.fetchall()
    if len(records):
        res = []
        for i in records:
            r = {
                "_id":i[0],
                "product":i[1],
                "category":i[2],
                "price":i[3]
            }
            res.append(r)
        db.close()
        return json.dumps(res,separators=(',', ':'))

    else:
        return "NA"

@app.route('/update-item',methods = ["GET"])
def updateItem():
    try:
        db = mysql.connect(
        host="mysql-50168-0.cloudclusters.net",
        user="admin",
        port ="18972",
        password="TEM2JKQv",
        database="products"
            )	
        cursor = db.cursor()
        _id = request.args.get("id")
        product = request.args.get("product")
        category = request.args.get("category")
        price = request.args.get("price")
        SQL = "UPDATE `items` SET `product`='"+product+"',`category`='"+category+"',`price`='"+price+"' WHERE `serialNo`='"+_id+"'"
        cursor.execute(SQL)
        db.commit()
        db.close()
        return "200"
    except:
        return "NA"

@app.route('/query',methods=["GET"])
def query():
    try:
        db = mysql.connect(
        host="mysql-50168-0.cloudclusters.net",
        user="admin",
        port ="18972",
        password="TEM2JKQv",
        database="products"
            )	
        cursor = db.cursor()
        q = request.args.get("q").lower()
        SQL = "SELECT * from items where product LIKE '%"+q+"%' or category LIKE '%"+q+"%' order by serialNo"
        cursor.execute(SQL)
        records = cursor.fetchall()
        if len(records):
            res = []
            for i in records:
                r = {
                    "_id":i[0],
                    "product":i[1],
                    "category":i[2],
                    "price":i[3]
                }
                res.append(r)
            db.close()
            return json.dumps(res,separators=(',', ':'))
        return "NA~"
    except Exception as e:
        print(e)
        return "NA"

@app.route('/delete-item',methods = ["GET"])
def delItem():
    try:
        db = mysql.connect(
        host="mysql-50168-0.cloudclusters.net",
        user="admin",
        port ="18972",
        password="TEM2JKQv",
        database="products"
            )	
        cursor = db.cursor()
        _id = request.args.get("id")
        SQL = "DELETE FROM items where serialNo = '"+_id+"'"
        cursor.execute(SQL)     
        print(SQL)
        db.commit()
        db.close()
        return "200"
    except Exception as e:
        print(e)
        return "NA"


@app.route("/new-item",methods=["GET"])
def newItem():
    try:
        db = mysql.connect(
        host="mysql-50168-0.cloudclusters.net",
        user="admin",
        port ="18972",
        password="TEM2JKQv",
        database="products"
            )	
        cursor = db.cursor()
        _id = request.args.get("id").lower()
        product = request.args.get("product").lower()
        category = request.args.get("category").lower()
        price = request.args.get("price").lower()
        SQL = "INSERT INTO items VALUES('"+_id+"','"+product+"','"+category+"','"+price+"')"
        cursor.execute(SQL)     
        print(SQL)
        db.commit()
        redirect('/items')
        db.close()
        return "200"
    except Exception as e: 
        print("E94",e)
        return "NA"    
app.run(debug=False)
