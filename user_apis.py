import json

import firebase_admin
from firebase_admin import credentials
from flask import Blueprint, request

from configs import database, Keys
from models import Student

userAPI = Blueprint('user', __name__)

userDB = database.collection('user-service-db')


# page1 => data send (json) => process => data send (json) => next render?

@userAPI.post()
def create_user(req):
    # req = request.form
    student_data = Student(firstName=req[Keys.first_name],
                           lastName=req[Keys.last_name],
                           collegeId=req[Keys.college_id],
                           collegeEmailId=req[Keys.college_email_id],
                           dateOfBirth=req[Keys.date_of_birth],
                           phoneNumber=req[Keys.phone_number]).__dict__
    userDB.add(json.dumps(student_data))
    return student_data


@userAPI.get()
def get_user():
    req = request.form
    college_id = req[Keys.college_id]
    response = userDB.where(f"{Keys.college_id} == college_id").get()
    res = response.to_dict()
    if res.len() != 1 or res[Keys.password] != req[Keys.password]:
        "User Not Found"
    return res


def populate_data_into_user_db():
    create_user({
        "firstName": "Gautam",
        "lastName": "Verma",
        "collegeId": "195036",
        "collegeEmailId": "195036@nith.ac.in",
        "dateOfBirth": "18-05-2001",
        "phoneNumber": "8920460627"
    })


if __name__ == '__main__':
    populate_data_into_user_db()
