#employee1 = 40000 + 100
#employee2 = 40000 +200
#employee3 = 40000 +0
def showMessage(message):
    print (message)


def calculateSalary(bonus, deduction=0):
    return 40000 + bonus - deduction


employee1 = calculateSalary(100, 100)
employee2 = calculateSalary(200)


print (employee1,employee2)
showMessage ("your salary")
