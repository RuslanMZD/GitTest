class Student:
    def __init__(self,first_name, last_name,group,academic_performance_list):
        self.first_name = first_name
        self.last_name = last_name
        self.group=group
        self.academic_performance_list = academic_performance_list


student1= Student("student1","student1","1",[5,4,3,4,5])
student2= Student("student2","student2","1",[5,4,5,5,5])
student3= Student("student3","student3","1",[5,2,3,2,5])
student4= Student("student4","student4","1",[5,4,3,2,5])
student5= Student("student5","student5","1",[5,2,3,3,5])
student6= Student("student6","student6","1",[5,2,3,2,2])
student7= Student("student7","student7","1",[5,2,5,2,5])
student8= Student("student8","student8","1",[5,2,3,5,5])
student9= Student("student9","student9","1",[5,2,5,2,5])
student10= Student("student10","student10","1",[5,5,3,2,5])
students = [student1,student2,student3,student4,student5,student6,student7,student8,student9,student10]


for student in students:
    sum_perfomance = sum(student.academic_performance_list)
    student.average = sum_perfomance/len(student.academic_performance_list)



tmp = sorted(students,key=lambda x: x.average)

for x in tmp:
    print(x.average)



