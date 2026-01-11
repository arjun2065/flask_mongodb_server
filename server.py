from flask import request,Flask,jsonify
import os
from pymongo import MongoClient
app=Flask(__name__)
from dotenv import load_dotenv
load_dotenv()
mongo=os.getenv("mongo_url")
client=MongoClient(os.getenv("mongo_url"))
database=client["class"]
collection=database["student"]

@app.route('/add_student',methods=["POST"])
def add_student():
    try:
        data=request.json
        student={
            "id":data.get("id"),
            "name":data.get("name"),
            "roll_no":data.get("roll_no"),
            "cgpa":data.get("cgpa")
        }

        collection.insert_one(student)
        return jsonify("successfull !")
    except :
        return jsonify("Enter a valid input"),400
@app.route('/get_student/<id>',methods=["GET"])
def get_student(id):
    try:
        student=collection.find_one({"id":id})
        if not student:
            return jsonify("something went wrong")
        return jsonify(student)
    except:
        return jsonify("Enter a valid Id"),404
@app.route('/delete_student/<id>',methods=["DELETE"])
def delete_student(id):
    try:
        collection.delete_one({"id":id})
        return jsonify("done !")
    except :
        return jsonify("Enter a valid id"),404
@app.route('/update/<id>',methods=["PUT"])
def update_student(id):
    try:
        data=request.json
        collection.update_one({"id":id},{data})
        return jsonify("done !")
    except :
        return jsonify("Enter a valid id"),404
if __name__=='__main__':
    app.run(debug=True)

