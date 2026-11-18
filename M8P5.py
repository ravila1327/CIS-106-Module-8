totalTuition = 0
studentCount = 0
infile = open("students.txt", 'r')
nextLine = infile.readline()
while not nextLine == '':
    lastName = nextLine
    nextLine = infile.readline()
    districtCode = nextLine
    nextLine = infile.readline()
    credits = int(nextLine)
    nextLine = infile.readline()
    if districtCode == "I":
        costPerCredit = 250
    else:
        costPerCredit = 500
    tuition = credits * costPerCredit
    totalTuition = totalTuition + tuition
    studentCount = studentCount + 1
    print(lastName + " " + str(credits) + " $" + str(tuition))
infile.close()
print("Total tuition owed: $" + str(totalTuition))
print("Number of students: " + str(studentCount))
