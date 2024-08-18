def userEntity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "name":item["name"],
        "email":item["email"],
        "phone":item["phone"],
        "city":item["city"],
        "temp":item["temp"],
        "humidity":item["humidity"],
        "description":item["description"]

    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]