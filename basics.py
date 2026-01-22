student_data={}
while True:
    name=input("enter students name: ")
    if name=="exit":
        break
    marks=float(input("enter student marks: "))
    student_data[name]=marks    
all_marks=student_data.values()
if len(all_marks)>0:
    average=sum(all_marks)/len(all_marks)
    print(f"average marks is {average}")
else:
    print("no data entered")

