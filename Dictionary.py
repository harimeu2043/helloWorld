class Dictionary:
    student1 = {"name": "Jose", "school": "Computing", "grades": (66, 77, 88)}
    student2 = {"name": "Alice", "school": "Engineering", "grades": (70, 80, 90)}
    student3 = {"name": "Bob", "school": "Mathematics", "grades": (60, 75, 85)}
    @staticmethod
    def average_grade(data):
        grades=data["grades"]
        return sum(grades)/len(grades)
    @staticmethod
    def average_grade_all_students(student_list):
        total=0
        count=0
        for student in student_list:
            total=total+sum(student["grades"])
            count=count+len(student["grades"])
        if count==0:
            return 0
        return total/count

students=[Dictionary.student1, Dictionary.student2, Dictionary.student3]
    
print("Average grade for all students:", Dictionary.average_grade_all_students(students))