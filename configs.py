import firebase_admin
from credentials import credentials
from firebase_admin import firestore


class Formats:
    timestamp_format = "%Y-%m-%d %H:%M:%S"


cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase = firebase_admin.initialize_app(cred)
database = firestore.client()


class Keys:
    first_name = "firstName"
    last_name = "lastName"
    college_id = "collegeId"
    college_email_id = "collegeEmailId"
    date_of_birth = "dateOfBirth"
    phone_number = "phoneNumber"
    student_id = "studentId"
    updated_timestamp = "updatedTimestamp"
    created_timestamp = "createdTimestamp"
    password = "password"
