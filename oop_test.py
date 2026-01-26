class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def calculate_average(self):
            average=sum(self.marks)/len(self.marks)
            return average
    def get_status(self,average):
            if average>=50:
                return "pass"
            else:
                return "fail"
    def create_report(self):
        average=self.calculate_average()
        status=self.get_status(average)
        return {
            "name":self.name,
            "marks":self.marks,
            "average":average,
            "status":status
        }
    def add_mark(self,mark):
         self.marks.append(mark)
         
if __name__=="__main__":
    rahul=Student("Rahul",[55,65,75])
    rahul.add_mark(95)
    print(rahul.create_report())
