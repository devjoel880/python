def greet(student_info):
    print("Hello, " + student_info["name"] + "! You are " + str(student_info["age"]) + " years old")
    
student_info = {"name": "Alice", "age": 21}

greet(student_info)