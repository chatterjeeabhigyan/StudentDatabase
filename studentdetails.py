import os

db = []

# Student class
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.marks = None
    def update(self, newname, newroll):
        self.name = newname
        self.roll = newroll
    def setMarks(self, marks):
        if self.marks != None:
            return False
        else:
            self.marks = marks
            return True
    def getMarks(self, subject):
        if self.marks == None:
            return False
        else:
            if subject == "all":
                return self.marks
            else:
                for mark in self.marks:
                    if subject in list(mark.keys()):
                        return mark[subject]
                else: 
                    return False
                
# utility functions
def getStudent():
    roll = int(input("Enter the roll number of the student : "))
    student = None
    for i in db:
        if i.roll == roll:
            student = i
    if student == None:
        print(f"No student was found roll number {roll}!")
        return getStudent()
    else:
        return student
def calculatepercentage(student: Student):
    marks = []
    for i in student.getMarks("all"):
        marks.append(list(i.items())[0][1])
    s = 0
    for j in marks:
        s+=j
    return ((s/(100*len(marks)))*100)

# functions for setting info
def addStudent():
    name = input("Enter the name of the student : ")
    roll = int(input("Enter the roll number of the student : "))
    newstudent = Student(name, roll)
    db.append(newstudent)
    print(f"{newstudent.name} was added as a new student!")

def deleteStudent():
    student = getStudent()
    print(f"deleted {student.name} from the database.")
    db.pop(db.index(student))
    del student

def updateStudent():
    print("What do you want to update ?")
    print("(a) - Update only name.")
    print("(b) - Update only roll number.")
    print("(c) - Update both name and roll number.")
    print("*Note: to update any of the following category, you need to provide the previous roll number of the particular student*")
    category = input("Enter the category you want to update : ")
    os.system("cls")
    prevroll = int(input("Enter the previous roll number of the student : "))
    student = None
    for i in db:
        if i.roll == prevroll:
            student = i
    if student != None:
        match category:
            case "a":
                newname = input("Enter the new name of the student : ")
                student.update(newname, student.roll)
                print("Student details updated!")
            case "b":
                newroll = int(input("Enter the new roll number of the student : "))
                student.update(student.name, newroll)
                print("Student details updated!")
            case "c":
                newroll = int(input("Enter the new roll number of the student : "))
                newname = input("Enter the new name of the student : ")
                student.update(newname, newroll)
                print("Student details updated!")
            case _:
                print(f"{category} is not a category mentioned above!")
    else:
        print("No student was found with that roll number!")

def setStudentMarks():
    student = getStudent()
    subjects = ["physics", "chemistry", "biology", "geography", "history", "english", "bengali", "computer", "mathematics"]
    marks = []
    for sub in subjects:
        mark = int(input(f"Enter the marks in {sub} : "))
        marks.append({ sub : mark })
    result = student.setMarks(marks)
    if result == True:
        print(f"All the marks has been set to {student.name}!")
    else:
        os.system("cls")
        print(f"The marks are already set to {student.name}! Cannot add marks after setting once!")

# functions for retrieving info
def showCurrentStudents():
    print("Students who are present in the database currently are : ")
    for i in db:
        print(f"Name: {i.name}, Roll number: {i.roll}")

def getPercentage():
    student = getStudent()
    percentage = calculatepercentage(student)
    print(f"Percentage of {student.name} is {percentage}%")

def scholarshipStatus():
    student = getStudent()
    percentage = calculatepercentage(student)
    if percentage >= 90:
        print(f"{student.name} has got 80% scolarship!")
    elif percentage >= 80 and percentage < 90:
        print(f"{student.name} has got 40% scholarship!")
    else:
        print(f"unfortunately, {student.name} did not get a scholarship.")

def getStudentMarks():
    student = getStudent()
    print("What marks do you want to get?")
    print("(a) - Marks of all subjects.")
    print("(b) - Marks of a single subject. - physics, chemistry, biology, geography, history, english, bengali, computer, mathematics")
    category = input("Enter the category you want to get marks : ")
    match category:
        case "a":
            marks = student.getMarks("all")
            for i in marks:
                sub = list(i.keys())[0]
                mark = i[sub]
                print(f"Marks in {sub} : {mark}")
        case "b":
            sub = input("Enter the subject whose marks you want to retrieve (the list of subjects is mentioned above) : ")
            mark = student.getMarks(sub)
            if mark != False:
                print(f"Marks in {sub} : {mark}")
            else: 
                print("*The Subject you mentioned above is not in the list* or *The marks are not yet set to the student's profile*.")
        case _:
            print(f"{category} is not a category mentioned above!")
def getFinalReport():
    student = getStudent()
    marks = student.getMarks("all")
    percentage = calculatepercentage(student)
    scholarship = None
    if percentage >= 90:
        scholarship = "80% scholarship"
    elif percentage >= 80 and percentage < 90:
        scholarship = "40% scholarship"
    print(f"Name of the student : {student.name}")
    print(f"Roll number of the student: {student.roll}")
    print("#################")
    for i in marks:
        sub = list(i.keys())[0]
        mark = i[sub]
        print(f"Marks in {sub} : {mark}")
    print("#################")
    print(f"Final percentage: {percentage}%")
    print(f"Scholarship Status: {scholarship}")
# main function
def main():
    try:
        print("What do you want to do?")
        print("(a) - Add Student.")
        print("(b) - Update Student.")
        print("(c) - Delete Student.")
        print("(d) - Set Student Marks.")
        print("(e) - Show current students in database.")
        print("(f) - Get Student Marks.")
        print("(g) - Get Student percentage.")
        print("(h) - Check Scholarship status.")
        print("(i) - Get Final report.")
        category = input("Enter the category : ")
        os.system("cls")
        match category:
            case "a":
                addStudent()
            case "b":
                updateStudent()
            case "c":
                deleteStudent()
            case "d":
                setStudentMarks()
            case "e":
                showCurrentStudents()
            case "f":
                getStudentMarks()
            case "g":
                getPercentage()
            case "h":
                scholarshipStatus()
            case "i":
                getFinalReport()
            case _:
                print(f"{category} is not a category mentioned above!")
        
        c = input("Do you want to go back to the home menu ? (y/n) : ")
        if c=="y" or c=="Y":
            os.system("cls")
            main()
    except Exception as e:
        print(f"An unexpected exception happend : {str(e)}")


main()