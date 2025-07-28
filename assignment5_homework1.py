name=input("Enter the student's name: ")
dict={'Sam':27,'Ben':83,'Max':39,'Lucy':64,'Mia':68}

try:
    dict[name]
    print(name+("'s"),"marks are: ",dict[name])
except:
    print("Student not found.")


