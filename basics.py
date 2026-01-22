import statistics
def calculate_average(all_marks):
    return statistics.mean(all_marks)
student_data={}
while True:
    name=input("enter students name: ")
    if name=="exit":
        break
    try:
        marks=float(input("enter student marks: "))
        student_data[name]=marks    
    except ValueError:
        print("thats not a number")
all_marks=student_data.values()
if len(all_marks)>0:
    print(f"average marks is {calculate_average(all_marks)}") 
else:
    print("no data entered")

