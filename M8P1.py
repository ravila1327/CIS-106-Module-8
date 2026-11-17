print("Enter principal amount:")
principal = float(input())
print("Enter inerest rate:")
interestRate = float(input())
beginningBalance = principal
totalInterest = 0
print("Year     Beginning Balance     Ending Balance")
for year in range(1, 5 + 1, 1):
    interest = beginningBalance * interestRate
    endingBalance = beginningBalance + interest
    print(str(year) + "     " + str(beginningBalance) + "     " + str(endingBalance))
    totalInterest = totalInterest + interest
    beginningBalance = endingBalance
print("Total interest earned: $" + str(totalInterest))
