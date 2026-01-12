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
@app.route('/')
def welcome():
    return jsonify("welcome") 

@app.route('/add_student',methods=["POST"])
def add_student():
    data=request.json
    student={
        "id":data.get("id"),
        "name":data.get("name"),
        "roll_no":data.get("roll_no"),
        "cgpa":data.get("cgpa")
    }

    collection.insert_one(student)
    return jsonify("successfull !")

@app.route('/get_student/<id>',methods=["GET"])
def get_student(id):
    student=collection.find_one({"id":id},{"_id":0})
    if not student:
        return jsonify("something went wrong")
    return jsonify(student)

@app.route('/delete_student/<id>',methods=["DELETE"])
def delete_student(id):

    collection.delete_one({"id":id})
    return jsonify("done !")

@app.route('/update/<id>',methods=["PUT"])
def update_student(id):
    data=request.json
    collection.update_one({"id":id},{"$set":data})
    return jsonify("done !")

if __name__=='__main__':
    app.run(debug=True)

