"""
Instance variables of a class are those variables, one copy of which is created and saved to heap memory when we create an instance of that class.

Note - 
1) copy of an instance variable will be different for different objects of a class.
2) We use 'self' keyword to access an instance variable inside a class, but to access an instance variable outside of a class, we use the name of the object.
3) We can assign values to Instance variables through creating a constructor method.

"""

import random
import string

class Employee:
  empID = ''          # <-- instance variable
  empName = ''
  empGender = ''
  empDob = ''
  empLastQlf = ''
  empAddress = ''
  empPhone = ''
  empEmail = ''

  def __init__(self, name, gend, dob, qlf, add, phn, eml):
    self.empID = self.genEmpID()
    self.empName = name
    self.empGender = gend
    self.empDob = dob
    self.empLastQlf = qlf
    self.empAddress = add
    self.empPhone = phn
    self.empEmail = eml

  def genEmpID(self):
    capLets = string.ascii_uppercase
    digits = string.digits
    capDigtList = list(capLets + digits)
    random.shuffle(capDigtList)
    id = ''.join(capDigtList)[0:10]
    return id
  
  def saveEmpInfo(self):
    try:
      f = open('employee_details.txt', 'a')
      try:
        empDetails = f'\nID: {self.empID}\nName: {self.empName}\nGender: {self.empGender}\nDate of birth: {self.empDob}\nLast Qualification: {self.empLastQlf}\nAddress: {self.empAddress}\nPhone no.: {self.empPhone}\nEmail ID: {self.empEmail}\n'
        
        status = f.write(empDetails)
        if status:
          return '\nSuccess: writing to the file is successful!'
      except:
        return '\nError: unable to write into the file!'
      finally:
        f.close()
    except:
      return '\nError: unable to open the file!'
    

while True:
  getEmpName = input('Enter employee\'s name:\n')
  getEmpGend = input('Enter employee\'s gender (M/F):\n')
  getEmpDob = input('Enter employee\'s date of birth:\n')
  getEmpQlf = input('Enter employee\'s last qualification:\n')
  getEmpAdd = input('Enter employee\'s address:\n')
  getEmpPhn = input('Enter employee\'s phone no.:\n')
  getEmpEml = input('Enter employee\'s email ID:\n')

  empObj = Employee(getEmpName, getEmpGend, getEmpDob, getEmpQlf, getEmpAdd, getEmpPhn, getEmpEml)

  print(empObj.saveEmpInfo())

  cont = input('\nEnter "q" to quit or "any other key" to continue:\n')

  if cont == 'q':
    print()
    break
  else:
    print()
    continue

print('***please visit the "employee_details.txt" file for more details about employees!')