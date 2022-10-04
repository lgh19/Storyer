
import sys

students = []

# range of how many students should be in each group
minGroupSize = 3
maxGroupSize = 5

"""
Java class

public class Student(int id){
    int id;
    int[] preferences;
    public Student(int id){
        this.id = id;
        this.preferences = new Array[]
      }
}
"""

# integer ID identifier and an ordered list of student's preferred groups
class Student:
    def __init__(self, id):
        self.ID = id
        self.prefers = []
    
    # for reading in a test file that already provides preferences
    def __init__(self, id, prefers):
        self.ID = id
        self.prefers = prefers

# if a test file was included in the command line, use this to get the data
if len(sys.argv) > 1:
    # get filename from first argument
    fName = sys.argv[1]

    f = open(fName, 'r')
    # reads first line for 'course info', use strip to remove tailing '\n'
    currLine = f.readline().strip()
    # split by delimiter
    myNums = currLine.split(';', 1)

    print(myNums)

    # start getting the students from the file
    for line in f:
        #print(line.strip())
        currStudent = line.strip().split(';', 4)
        students.append(Student())

    f.close()

    groups = ["A", "B", "C"]

# otherwise if no file was included just use a default arrangement
else:
    groups = ["A", "B", "C"]

    # number of students for generating in this test program
    numStudents = 6

    # Generates some students with a basic integer ID and single group preference
    #in java: for(int i = 0; i < numStudents; i++)
    for i in range(numStudents):
        # create new student with ID i
        student = Student(i)
        # add this student to whole list of student
        students.append(student)
        # place student preferences
        for g in range(len(groups)):
            students[i].prefers.append(groups[(i+g) % len(groups)])

        # debug printing
        print(student.ID)
        print(student.prefers)
        print()

# a dictionary to hold the students in their preferred groups
setGroups = {
    "A": [],
    "B": [],
    "C": []
}

# places students into the above dict based on their primary preference
for student in students:
    for group in groups:
        if student.prefers[0] == group:
            # for now just adds student ID for a nice dict print
            # would ideally store the student's key from database instead
            setGroups[group].append(student.ID)

print()
print(setGroups)
