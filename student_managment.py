import json 
print("1. new student")
print("2. update marks")
print("3. remove student record")
# print("4. ")
Menu = int(input("Enter your task no:"))
if Menu==1:
 dict={}
 def new_student():
     student_id= int(input("Enetr id: "))
     student_name = input("Enter Student Name: ")
     student_course = input("Enter course:")
     student_age = int(input("Enter age:"))
     dict["id"]=student_id
     dict["name"]=student_name
     dict["course"]=student_course
     dict["age"]=student_age
     with open("student.json","w") as f:
         json.dump(dict,f)
 new_student()
 print("student added succesfully")
elif Menu==2:


 student_id = int(input("Enter your id : "))

 def load_data(filename):
     with open(filename,"r") as f:
         data=json.load(f)
         return data
 data = load_data("student.json")

 def update_marks(data,student_id):
      for i in data:
          if i["id"] == student_id:
              new_marks=int(input("enter new marks:"))
              i.update({"marks": new_marks})
              with open("student.json","w") as f: 
                  json.dump(data,f)
 update_marks(data,student_id)

elif Menu==3:
    def load_data(filename):
     with open(filename,"r") as f:
         data=json.load(f)
         return data
    data = load_data("student.json")

    student_id = int(input("Enter your id : "))
    def remove_record(data):
        for i in data:
          if i["id"] == student_id:
             data.remove(i)
             with open("student.json","w") as f:
                json.dump(data,f)

    remove_record(data)
    print("record removed successfully")
    
    
    #    print("thnaks for vsit!")

else:
   print("This task updated soon!")










