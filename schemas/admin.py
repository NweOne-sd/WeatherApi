"""
def adminEntity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "name":item["name"],
        "email":item["email"],
        "phone":item["phone"],
        "city":item["city"],
      #  "temp":item["temp"],
      #  "humidity":item["humidity"],
      #  "description":item["description"]

    }

def adminsEntity(entity) -> list:
    return [adminEntity(item) for item in entity]

"""