import statistics
def calculate_average(all_marks):
    flat_list=[]
    for student_list in all_marks:
        for mark in student_list:
            flat_list.append(mark)
    return statistics.mean(flat_list)
student_data={}
while True:
    name=input("enter students name: ")
    if name=="exit":
        break
    try:
        student_marks=[]
        for i in range(3):
            marks=float(input("enter student marks: "))
            student_marks.append(marks)
        student_data[name]=student_marks    
    except ValueError:
        print("thats not a number")
all_marks=student_data.values()
if len(all_marks)>0:
    print(f"average marks is {calculate_average(all_marks)}") 
else:
    print("no data entered")

