totalBonus = 0
infile = open("employees.txt", 'r')
nextLine = infile.readline()
while not nextLine == '':
    lastName = nextLine
    nextLine = infile.readline()
    salary = float(nextLine)
    nextLine = infile.readline()
    if salary >= 100000:
        bonusRate = 0.2
    else:
        if salary >= 50000:
            bonusRate = 0.15
        else:
            bonusRate = 0.1
    bonus = salary * bonusRate
    totalBonus = totalBonus + bonus
    print(lastName + " " + str(salary) + " " + str(bonus))
infile.close()
print("Total bonus paid: $" + str(totalBonus))
