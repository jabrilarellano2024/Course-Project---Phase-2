#Jessica Arellano#
#CIS261 - Course Project Phase 4#

from datetime import datetime

def CreateUsers():
    print('Create users, passwords, and roles')
    UserFile = open("Users.txt", "a+")
    while True:
        username = GetUserName()
        if (username.upper() == "END"):
            break
        userpwd = GetUserPassword()
        userrole = GetUserRole()
        
        UserDetail = username + "|" + userpwd + "|" + userrole + "\n"
        UserFile.write(UserDetail)
        
    UserFile.close()
    printuserinfo()
    
def GetUserName():
    username = input("Enter user name or 'End' to quit: ")
    return username

def GetUserPassword():
    pwd = input("Enter password: ")
    return pwd

def GetUserRole():
    userrole = input("Enter role (Admin or User): ")
    while True:
        if (userrole.upper() == "ADMIN" or userrole.upper() == "USER"):
            return userrole
        else:
            userrole = input("Enter role (Admin or User): ")
            
def printuserinfor():
    UserFile = open("Users.txt", "r")
    while True:
        UserDetail = UserFile.readline()
        if not UserDetail:
            break
        UserDetail = UserDetail.replace("\n", "")
        UserList = UserDetail.split("|")
        username = UserList[0]
        userpassword = UserList[1]
        userrole = UserList[2]
        print("User Name: ", username, "Password: ", userpassword, "Role: ", userrole)
        
def Login():
    UserFile = open("Users.txt", "r")
    UserList = []
    UserName = input("Enter User Name: ")
    UserPwd = input("Enter Password: ")
    UserRole = "None"
    while True:
        UserDetail = UserFile.readline()
        if not UserDetail:
            return UserRole, UserName, UserPwd
        UserDetail = UserDetail.replace("\n", "")
        
        UserList = UserDetail.split("|")
        if UserName == UserList[0] and UserPwd == UserList[1]:
            UserRole = UserList[2] 
            return UserRole, UserName
    return UserRole, UserName
    
def getDatesWorked():
    fromDate = input("Please enter start date in the following format MM/DD/YYYY: ")
    endDate = input("Please enter end date in the following format MM/DD/YYYY: ")
    return fromDate, endDate


def getEmpName():
    empName = input("Enter employee name: ")
    return empName

def getHoursWorked():
    hours = float(input("Enter Hours: "))
    return hours

def getHourlyRate():
    hourlyRate = float(input("Enter Hourly Rate: "))
    return hourlyRate

def getTaxRate():
    taxRate = float(input("Enter Tax Rate: "))
    taxRate = taxRate / 100
    return taxRate

def CalcTaxAndNetPay(hours, hourlyRate, taxRate):
    gPay = hours * hourlyRate
    incomeTax = gPay * taxRate
    netPay = gPay - incomeTax
    return gPay, incomeTax, netPay

def printInfo(empDetailList):
    totalEmployees = 0
    totalHours = 0.00
    totalGrossPay = 0.00
    totalTax = 0.00
    totalNetPay = 0.00
    EmpFile = open("Employees.txt", "r")
    while True:
        rundate = input("Enter start date for report (MM/DD/YYYY) or All for all data in file: ")
        if (rundate.upper() == "ALL"):
            break
        try:
            rundate = datetime.strptime(rundate, "%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date format. Try again.")
            print()
            continue
    while True:
        EmpDetail = EmpFile.readline()
        if not EmpDetail:
            break
        EmpDetail = EmpDetailList.replace("\n", "")
        
        EmpList = EmpDetail.split("|")
        fromDate = empList[0]
        if (str(rundate).upper() != "ALL"):
            checkdate = datetime.strptime(fromdate, "%m/%d/%Y")
            if (checkdate < rundate):
                continue
        todate = empList[1]
        empName = empList[2]
        hours = float(empList[3])
        hourlyRate = float(empList[4])
        taxRate = float(empList[5])
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyRate, taxRate)
        print(fromDate, endDate, empName, f"{hours:,.2f}", f"{hourlyRate:,.2f}", f"{grosspay:,.2f}", f"{taxRate:,.1%}", f"{incometax:,.2f}", f"{netpay:,.2f}")
        totalEmployees += 1
        totalHours += hours
        totalGrossPay +=grosspay
        totalTax += incometax
        totalNetPay += netpay
        empTotals["totEmp"] = totalEmployees
        empTotals["totHours"] = totalHours
        empTotals["totGross"] = totalGrossPay
        empTotals["totTax"] = totalTax
        empTotals["totNet"] = totalNetPay
        DetailsPrinted = True
    if (DetailsPrinted):
        PrintTotals(empTotals)
    else:
        print("No detail information to print")
    
        
def printTotals(empTotals):
    print()
    print(f"Total Number of Employees:  {empTotals['totEmp']}")
    print(f"Total Hours of Employees:   {empTotals['totHours']}")
    print(f"Total Gross Pay of Employees:   {empTotals['totGross']:,.2f}")
    print(f"Total Tax of Employees: {empTotals['totTax']:,.2f}")
    print(f"Total Net Pay of Employees: {empTotals['totNet']:,.2f}")
    
if __name__ == "__main__":

    CreateUsers()
    print()
    print("Data Entry")
    UserRole, UserName = Login()
    DetailsPrinted = False
    empTotals = {}
    if (UserRole.upper() == "NONE"):
        print(UserName, " is invalid.")
    else:
   
        if (UserRole.upper() == "ADMIN"):
            EmpFile = open("Employees.txt", "a+")
            while True:
                empname = getEmpName()
                if (empname.upper() == "END"):
                    break
                fromdate, todate = getDatesWorked()
                hours = getHoursWorked()
                hourlyrate = getHourlyRate()
                taxrate = getTaxRate()
                EmpDetail = fromdate + "|" + todate + "|" + empname + "|" + str(hours) + "|" + str(hourlyrate) + "|" + str(taxrate) + "\n"
                EmpFile.write(EmpDetail)
                
            EmpFile.close()
        printinfo(DetailsPrinted)
    


    
         
    
        
        
       
        
       
        
   
    
       
        
    

