import csv, os, datetime, time
from termcolor import colored
from prettytable import from_csv, PrettyTable

#fontcolors using termcolor
class fontcolor():
	def green(string):
		return colored(string, "green", attrs=['bold'])
	def white(string):
		return colored(string, "white", attrs=['bold'])
	def yellow(string):
		return colored(string, "yellow", attrs=['bold'])
	def cyan(string):
		return colored(string, "cyan", attrs=['bold'])
	def red(string):
		return colored(string, "red", attrs=['bold'])
	def blue(string):
		return colored(string, "blue", attrs=['bold'])

#smb ==> symbols
class smb:
	WARN = fontcolor.red(" [-] ")
	DONE = fontcolor.green(" [+] ")
	INPUT = fontcolor.cyan(" [»] ")
	INFO = fontcolor.yellow(" [!] ")
	ARROW = fontcolor.cyan(" > ")

banr = '''
             ╔═╗   ╦   ╔═╗     STUDENT
             ╚═╗   ║   ╚═╗     INFORMATION
             ╚═╝   ╩   ╚═╝     SYSTEM
          '''

def banner():
	print(fontcolor.cyan(banr))

class num:
	one = fontcolor.yellow("[1] ")
	two = fontcolor.yellow("[2] ")
	three = fontcolor.yellow("[3] ")
	four = fontcolor.yellow("[4] ")
	five = fontcolor.yellow("[5] ")
	six = fontcolor.yellow("[6] ")
	seven = fontcolor.yellow("[7] ")

def border_msg(msg):
    row = len(msg)
    m = ''.join(['        +'] + ['-' *row] + ['+'])
    h = fontcolor.cyan(m)
    result= h + '\n' + fontcolor.cyan("        |") + fontcolor.white(msg) + fontcolor.cyan("|") + '\n' + h
    print((result))

choice_one = fontcolor.white("Add New Student")
choice_two = fontcolor.white("View Students")
choice_three = fontcolor.white("Search Student")
choice_four = fontcolor.white("Update Student")
choice_five = fontcolor.white("Delete Student")
choice_six = fontcolor.white("Project Development Team")
choice_seven = fontcolor.white("Quit")

#choice menu 
def display_menu():
	banner()
	border_msg(" Welcome To Student Information System ! ")
	print("\n" + smb.ARROW + fontcolor.cyan("CHOOSE AN OPTION :") + "\n")
	print(smb.ARROW + num.one + choice_one)
	print(smb.ARROW + num.two + choice_two)
	print(smb.ARROW + num.three + choice_three)
	print(smb.ARROW + num.four + choice_four)
	print(smb.ARROW + num.five + choice_five)
	print(smb.ARROW + num.six + choice_six)
	print(smb.ARROW + num.seven + choice_seven)

raw_database = 'raw_data.csv'
student_database = 'students.csv'

#function for clearing screen
def clr_scr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

#press enter to continue message
def continue_msg():
	input("\n" + smb.ARROW + fontcolor.cyan("Press Enter To Continue : "))
	clr_scr()

##### validation functions #####
def validate_name(name):
	if name.replace(" ", "").isalpha():
		pass
	else:
		print("\n" + smb.WARN + fontcolor.red("Name Is Invalid ! It Should Not Have Digits !"))
		quit()

def validate_class(value):
	valid_classes = ('1','2','3','4','5','6','7','8,','9','10','11','12')
	if value in valid_classes:
		pass
	else:
		print("\n" + smb.WARN + fontcolor.red("Invalid Class !"))
		quit()

def validate_rollnum(rollnum):
	try:
		roll = int(rollnum)
	except ValueError:
		print("\n" + smb.WARN + fontcolor.red("Roll Number Must Be A Number !"))
		quit()

def validate_dob(dob):
	try:
		date_of_birth = datetime.datetime.strptime(dob, "%d/%m/%Y")
	except:
		print("\n" + smb.WARN + fontcolor.red("Incorrect date ! Valid Format Is (DD/MM/YYYY)"))
		quit()

def validate_sex(sex):
	valid_sexes = set('mftMFT')
	if sex in valid_sexes:
		pass
	else:
		print("\n" + smb.WARN + fontcolor.red("Invalid Gender !"))
		quit()

def validate_phonenum(phonenum):
	if len(phonenum) == 10:
		try:
			phone = int(phonenum)
		except ValueError:
			print("\n" + smb.WARN + fontcolor.red("Phone Number Must Not Contains Letters !"))
			quit()
	else:
		print("\n" + smb.WARN + fontcolor.red("It Must Contain 10 Digits !"))
		quit()

# main-function-1
#function to add students in database
def add_student():
	print("\n")
	border_msg(" Add A New Student's Information To Database ")
	print("\n")
	stu_name = input(smb.DONE + fontcolor.green("Student's Name : "))
	validate_name(stu_name)
	stu_father = input(smb.DONE + fontcolor.green("Father's Name : "))
	validate_name(stu_father)
	stu_class = input(smb.DONE + fontcolor.green("Class (1-12) : "))
	validate_class(stu_class)
	roll_num = input(smb.DONE + fontcolor.green("Roll No : "))
	validate_rollnum(roll_num)
	stu_dob = input(smb.DONE + fontcolor.green("DOB (DD/MM/YYYY) : "))
	validate_dob(stu_dob)
	stu_sex = input(smb.DONE + fontcolor.green("Sex (M/F/T) : "))
	validate_sex(stu_sex)
	phone_num = input(smb.DONE + fontcolor.green("Phone No (+91) : "))
	validate_phonenum(phone_num)
	
	student_data = []
	student_data.append(stu_name)
	student_data.append(stu_father)
	student_data.append(stu_class)
	student_data.append(roll_num)
	student_data.append(stu_dob)
	student_data.append(stu_sex)
	student_data.append(phone_num)

	header = ['Student','Father','Class','Roll No','DOB','Sex(M/F/T)','Phone']
	with open(raw_database, 'a') as f:
		writer = csv.writer(f)
		writer.writerow(i for i in header)
		writer.writerows([student_data])
		f.close()
	
    #removing duplicate headers and writing new file 'students.csv'
	inFile = open(raw_database, 'r')
	outFile = open(student_database, 'w')
	listLines = []
	for line in inFile:
		if line in listLines:
			continue
		else:
			outFile.write(line)
			listLines.append(line)
	outFile.close()
	inFile.close()
	
	try:
		x = PrettyTable()
		x.field_names = header
		x.add_row([student_data[0],student_data[1],student_data[2],student_data[3],student_data[4],student_data[5],student_data[6]])
		print("\n" + smb.DONE + fontcolor.green("Quick Overview :"))
		print(fontcolor.white(x))
		print("\n" + smb.DONE + fontcolor.green("Data Saved Successfully !"))
	except Exception:
		print("\n" + smb.WARN + fontcolor.red("Something Went Wrong ! Check Your Code !"))
	finally:
		continue_msg()

# main-function-2
#function to view the list of students in database
def view_students():
	print("\n")
	border_msg(" Student's Record In Our Information System ")
	try:
		fp = open(student_database, "r")
		file = from_csv(fp)
		fp.close()
		print(file)
	except (csv.Error, FileNotFoundError):
		print("\n" + smb.WARN + fontcolor.red("Something Went Wrong ! Check 'students.csv' File !"))
	finally:
		continue_msg()

# main-function-3
#function to search student with roll num
def search_student():
	print("\n")
	border_msg(" Search For A Student Inside Database ")
	roll = input("\n" + smb.DONE + fontcolor.green("Enter Roll No. To Search : "))
	try:
		fd = open(student_database, "r", encoding="utf-8")
		reader = csv.reader(fd)
		for row in reader:
			if len(row) > 0:
				if roll == row[3]:
					print("\n")
					print(fontcolor.green("\t----- STUDENT FOUND -----") + "\n")
					print(smb.DONE + fontcolor.green("Student's Name : ") + row[0])
					print(smb.DONE + fontcolor.green("Father's Name : ") + row[1])
					print(smb.DONE + fontcolor.green("Class : ") + row[2])
					print(smb.DONE + fontcolor.green("Roll No : ") + row[3])
					print(smb.DONE + fontcolor.green("DOB (DD/MM/YYYY) : ") + row[4])
					print(smb.DONE + fontcolor.green("Sex (M/F/T) : ") + row[5])
					print(smb.DONE + fontcolor.green("Phone No : ") + row[6])
					break
		else:
			print("\n" + smb.WARN + fontcolor.red("Student Not Found In Our Database !!!"))
		
	except FileNotFoundError:
		print("\n" + smb.WARN + fontcolor.red("No Records To Search !"))
	finally:
		continue_msg()

#main-function-4
#function to update student data
def update_student():
    print("\n")
    border_msg(" Update Student's Record In Database ")
    roll_num = input("\n" + smb.DONE + fontcolor.green("Enter Roll No. To Update : "))
    try:
    	index_student = None
    	updated_data = []
    	fe = open(student_database, "r", encoding="utf-8")
    	reader = csv.reader(fe)
    	counter = 0
    	
    	for row in reader:
    		if len(row) > 0:
    			if roll_num == row[3]:
    				index_student = counter
    				print("\n" + fontcolor.green('\t----- RECORD FOUND -----') + "\n")
    				print(smb.DONE + fontcolor.cyan("Student Found At Index =>"), index_student)
    				print(smb.DONE + fontcolor.cyan("Student's Name =>"), row[0])
    				student_data = []
    				print("\n")
    				
    				new_stu_name = input(smb.DONE + fontcolor.green("Enter Student's New Name : "))
    				validate_name(new_stu_name)
    				new_stu_father = input(smb.DONE + fontcolor.green("Enter Father's New Name : "))
    				validate_name(new_stu_father)
    				new_stu_class = input(smb.DONE + fontcolor.green("Enter New Class (1-12) : "))
    				validate_class(new_stu_class)
    				new_roll_num = input(smb.DONE + fontcolor.green("Enter New Roll No : "))
    				validate_rollnum(new_roll_num)
    				new_stu_dob = input(smb.DONE + fontcolor.green("Enter New DOB (DD/MM/YYYY) : "))
    				validate_dob(new_stu_dob)
    				new_stu_sex = input(smb.DONE + fontcolor.green("Enter New Sex (M/F/T) : "))
    				validate_sex(new_stu_sex)
    				new_phone_num = input(smb.DONE + fontcolor.green("Enter New Phone No (+91) : "))
    				validate_phonenum(new_phone_num)
    				
    				student_data.append(new_stu_name)
    				student_data.append(new_stu_father)
    				student_data.append(new_stu_class)
    				student_data.append(new_roll_num)
    				student_data.append(new_stu_dob)
    				student_data.append(new_stu_sex)
    				student_data.append(new_phone_num)

    				updated_data.append(student_data)
    			
    			else:
    				updated_data.append(row)
    			counter += 1
    
    except FileNotFoundError:
    	print("\n" + smb.WARN + fontcolor.red("No Records To Update !"))

#writing update to csv file
    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
            print("\n" + smb.DONE + fontcolor.green("Data Updated Successfully ! "))
            continue_msg()
    else:
        print("\n" + smb.WARN + fontcolor.red("Student Not Found In Our Database !!!"))
        continue_msg()
        
# main-function-5
#function to delete student record
def delete_student():
    border_msg(" Delete Student's Record From Database ")
    roll = input("\n" + smb.WARN + fontcolor.red("Enter Roll No. To Delete : "))
    
    try:
    	student_found = False
    	updated_data = []
    	ff = open(student_database, "r", encoding="utf-8")
    	reader = csv.reader(ff)
    	counter = 0
    	for row in reader:
    		if len(row) > 0:
    			if roll != row[3]:
    				updated_data.append(row)
    				counter += 1
    			else:
    				student_found = True
    
    except FileNotFoundError:
    	print("\n" + smb.WARN + fontcolor.red("No Records To Delete !"))

    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("\n" + smb.DONE + fontcolor.green("Roll No. Deleted Successfully"))
        continue_msg()
    else:
    	print("\n" + smb.WARN + fontcolor.red("Roll No. Not Found In Our Database !!!"))
    	continue_msg()

#main-function-6
#about us
def about_us():
	print("\n")
	border_msg(" Project Development Team ")
	#print("\n")
	z = PrettyTable()
	field_1 = fontcolor.green("Team Member")
	field_2 = fontcolor.green("Designation")
	field_3 = fontcolor.green("Standard")
	z.field_names = [field_1,field_2,field_3]
	
	z.add_row(['Sumit Patidar', 'hahaha','XII'])
	z.add_row(['Sumit Patidar', 'hahaha','XII'])
	z.add_row(['Sumit Patidar', 'hahaha','XII'])
	z.add_row(['Sumit Patidar', 'hahaha','XII'])

	print(z)
	continue_msg()

#looping the whole program
while True:
    display_menu()
    
    choice = input("\n" + smb.ARROW + fontcolor.cyan("Enter Your Choice : "))
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
    	about_us()
    elif  choice == '7':
    	print("\n" + smb.DONE + fontcolor.green("Thanks For Using Our Student Information System"))
    	print(smb.WARN + fontcolor.red("Quitting...."))
    	time.sleep(2)
    	quit()
    else:
    	   print("\n" + smb.WARN + fontcolor.red("Please, Enter A Valid Input !"))
    	   break