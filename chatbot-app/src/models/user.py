users = [
    {
        "id": 1,
        "username": "manager1",
        "password": "managerpass",
        "role": "manager",
        "mobile_number": "9999990001"
    },
    {
        "id": 2,
        "username": "employee1",
        "password": "employeepass1",
        "role": "employee",
        "mobile_number": "9999990002"
    },
    {
        "id": 3,
        "username": "employee2",
        "password": "employeepass2",
        "role": "employee",
        "mobile_number": "9999990003"
    },
    {
        "id": 4,
        "username": "employee3",
        "password": "employeepass3",
        "role": "employee",
        "mobile_number": "9999990004"
    },
    {
        "id": 5,
        "username": "employee4",
        "password": "employeepass4",
        "role": "employee",
        "mobile_number": "9999990005"
    },
    {
        "id": 6,
        "username": "employee5",
        "password": "employeepass5",
        "role": "employee",
        "mobile_number": "9999990006"
    }
]

def get_user_by_username(username):
    for user in users:
        if user["username"] == username:
            return user
    return None