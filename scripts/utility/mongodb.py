#scripts/utility/mondodb
from pymongo import MongoClient
from scripts.schema import StudentDatabase

client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
db = client['interns_b2_23']
collection = db['Syed_Faraz']


class Mongodb:
    def add_data(self, student: StudentDatabase):
        try:
            collection.insert_one(student.dict())
            return {"message": "data added"}
        except Exception as e:
            return {"Error": e}

    def del_data(self, student_name: str):
        try:
            result = collection.delete_one({"name": student_name})
            if result.deleted_count > 0:
                return {"message": "data is deleted successfully"}
            return {"error": "data not found"}
        except Exception as e:
            return {"Error": e}


    #
    # def add_new_data(self, query_data: dict):
    #     try:
    #         collection.insert_one(query_data)
    #         return {"message": "data added"}
    #     except Exception as e:
    #         return {"Error": e}

    def get_data(self):
        try:
            all_data = list(collection.find({}, {"_id": False}))
            return all_data
        except Exception as e:
            return {"Error": e}

    def get_data_name(self, name: str):
        try:
            data = list(collection.find({"name": name}))
            return data
        except Exception as e:
            return {"Error": e}
# Aggerigation
    def aggregate(self):
        try:
            avg_age = collection.aggregate([
                {
                    '$group': {
                        '_id': None,
                        'avg_age': {
                            '$avg': '$age'
                        }
                    }
                }, {
                    '$project': {
                        '_id': 0
                    }
                }
            ])
            avg_age = list(avg_age)
            return avg_age[0]["avg_age"]
        except Exception as e:
            return {"Error": e}