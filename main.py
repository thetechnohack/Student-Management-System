#import essential libraries
from cfonts import render
from prettytable import from_csv,PrettyTable
import csv
import time
import datetime

# Define global variables
student_fields = ['Name','Fathers Name','Class','Roll No','DOB','Sex(M/F/T)','Phone']
student_database = 'students.csv'

#banner artwork
banner = render("s.i.s", colors=['yellow', 'green'], align='center')
print(banner)

#ending banner
end_banner = render("Thank You", colors=['green', 'yellow'], align='center')

#colours used in program
GREEN = '\x1b[1;32;40m'
RED = '\x1b[1;31;40m'
GREEN_WHITE = '\x1b[0;30;42m' 
PURPLE = '\x1b[1;36;40m'
U_YELLOW = '\x1b[4;33;40m' 
WHITE = '\x1b[1;37;40m'
YELLOW = '\x1b[1;33;40m'
END = '\x1b[0m'

#symbol used in program
arrow_left = PURPLE  + '>>>' + END
arrow_right = PURPLE + '<<<' + END
block = '|'
space =' '
arrow = PURPLE + ' ##>' + END
arrow_m = PURPLE + ' »' + END
tick = GREEN + '✓✓ ' + END
box = GREEN +' ['+END+YELLOW+'*'+END+GREEN +'] ' +END 

#msg box variables 
welcome_msg = GREEN + 'Welcome To Student Information System !' + END
info_1 = GREEN + '\tAdd Student Information' + END
info_2 = GREEN + '\tStudents Record !' +END
info_3 = GREEN + '\tSearch Student !' +END
info_4 = GREEN +'\tUpdate Student Information !'+END
info_5 = RED +'\tDelete Student Record !'+END
info_6 = YELLOW+'\tProject Development Team !'+END

#stylish numbers
one = YELLOW+' ['+END+'1'+YELLOW+']'+END
two = YELLOW+' ['+END+'2'+YELLOW+']'+END
three = YELLOW+' ['+END+'3'+YELLOW+']'+END
four = YELLOW+' ['+END+'4'+YELLOW+']'+END
five = YELLOW+' ['+END+'5'+YELLOW+']'+END
six = YELLOW+' ['+END+'6'+YELLOW+']'+END
seven = YELLOW+' ['+END+'7'+YELLOW+']'+END


#choices
w_one = WHITE + ' Add New Student' + END
w_two = WHITE + ' View Students' + END
w_three = WHITE + ' Search Student' + END
w_four = WHITE + ' Update Student' + END
w_five = WHITE + ' Delete Student' + END
w_six = WHITE + ' Project Development Team'+END
w_seven = WHITE + ' Quit' + END

#input field colour
w_input = WHITE + ' Enter Your Choice : ' + END

#welcome msg_box
l = ''.join(['+'] + ['-' *48] + ['+'])
wlc_msg = l + '\n'+block+space+arrow_left+space+welcome_msg+space+arrow_right+space+block+'\n' + l

#add student msg_box
m = ''.join(['+'] + ['-' *40] + ['+'])
result_1 = m + '\n' +info_1 + '\n' + m

#view student msg_box
n = ''.join(['+'] + ['-' *30] + ['+'])
result_2 = n + '\n' + info_2 + '\n' + n

#search student msg_box
p = ''.join(['+'] + ['-' *30] + ['+'])
result_3 = p + '\n' + info_3 + '\n' + p

#update student msg_box
q = ''.join(['+'] + ['-' *40] + ['+'])
result_4 = q + '\n' + info_4 + '\n' + q

#delete student recode msg_box
r = ''.join(['+'] + ['-' *35] + ['+'])
result_5 = r + '\n' + info_5 + '\n' + r

#about us msg_box
s = ''.join(['+'] + ['-'*40] + ['+'])
result_6 = s + '\n' + info_6 + '\n' + s

#press enter to continue msg
def continue_msg():
	       	print('\n')
	       	input(arrow + YELLOW + " Press Enter To Continue : " + END)
	       	print('\n')

	
#choice menu 
def display_menu():
	print(wlc_msg)
	print(arrow+one+w_one)
	print(arrow+two+w_two)
	print(arrow+three+w_three)
	print(arrow+four+w_four)
	print(arrow+five+w_five)
	print(arrow+six+w_six)
	print(arrow+seven+w_seven)
	print('\n')

#add student function
def add_student():
	print(result_1)
	
	student_data = []
	def validate_name():
	   if name.replace(" ", "").isalpha():
	   	pass
	   else:
	   	print("Input is invalid")
	   	quit()

	name = input(arrow_m +YELLOW+ " Name of Student : " + END)
	validate_name()
	
	father = input(arrow_m + YELLOW+" Father's Name' :" + END)
	validate_name()
	
	def validate_class():
		try:
			val = int(clas)
		except ValueError:
			print("That's not an !")
			quit()

	clas = input(arrow_m +YELLOW +" Class :"+END)
	validate_class()
	
	def validate_roll():
		try:
			val = int(roll)
		except ValueError:
			print("Sorry Invalid Input!!!")
			quit()	
	
	roll = input(arrow_m + YELLOW +" Roll No. : "+ END)
	validate_roll()
	
	def validate_dob():
		date_format = '%d-%m-%Y'
		try:
			date_obj = datetime.datetime.strptime(dob, date_format)
			print(date_obj)
		except ValueError:
			print("Incorrect data format,It should be YYYY-MM-DD")
	
	dob = input(arrow_m + YELLOW +" Date Of Birth :"+ END)
	validate_dob()
	
	valid_sex = ['F','M','T','t','m','f','other']
	def validate_sex():
		if sex in valid_sex:
			pass
		else:
			print("wrong input")	
	
	sex = input(arrow_m + YELLOW +" Sex(m/f/t):"+ END)
	validate_sex()
	
	def validate_phone():
		try:
			val = int(phone)
		except ValueError:
			print("Incorrect Input!!")
	
	phone = input(arrow_m +YELLOW+" Phone no.:-"+ END)
	validate_phone()
	
	student_data.append(name)
	student_data.append(father)
	student_data.append(clas)
	student_data.append(roll)
	student_data.append(dob)
	student_data.append(sex)
	student_data.append(phone)
	
	with open(student_database, "a", encoding="utf-8") as f:
	       	writer = csv.writer(f)
	       	writer.writerows([student_data])
	       		       	
	       	x = PrettyTable()
	       	
	       	x.field_names = [GREEN+'Name','Fathers Name','Class','Roll No','DOB','Sex(M/F/T)','Phone'+END]
	  
	       	x.add_row([PURPLE+student_data[0],student_data[1],student_data[2],student_data[3],student_data[4],student_data[5],student_data[6]+END])
	       	print('\n')
	       	print(x)
	       	print('\n')
	       	
	       	print(tick+GREEN_WHITE + " Data Saved Successfully ! " + END)
	       	continue_msg()
	       	return

#function view students
def view_students():
	print(result_2)
	print("\n")
	
	
	fp = open("students.csv", "r")
	file = from_csv(fp)
	fp.close()
	print(file)
	continue_msg()
	
#function search student
def search_student():
    print(result_3)
    
    roll = input(arrow_m+ YELLOW + " Enter Roll No. To Search: " + END)
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if roll == row[3]:
                    print('\n')
                    
                    ['Name','Fathers Name','Class','Roll No','DOB','Sex(M/F/T)','Phone']
                    print(GREEN+"\t----- Student Found -----" + END)
                    print(box+YELLOW+"Student Name:"+ END,PURPLE +row[0]+END)
                    print(box+YELLOW+"Father's Name:"+END,PURPLE+row[1]+END)
                    print(box+YELLOW+"Class: "+END,PURPLE+row[2]+END)
                    print(box+YELLOW+"Roll No: "+END,PURPLE+row[3]+END)
                    print(box+YELLOW+"DOB (DD/MM/YYYY): "+END,PURPLE+row[4]+END)
                    print(box+YELLOW+"Sex(M/F/T): "+END,PURPLE+row[5]+END)
                    print(box+YELLOW+"Phone No. : "+END,PURPLE+row[6]+END)
                    continue_msg()
                    break
        else:
            print(box+RED+"ALERT!"+END)
            print(RED+' ×'*20+END)
            print(RED+" Student Not Found In Our Database !!!" +END)
            continue_msg()

#function update student
def update_student():
    print(result_4)
    
    roll = input(arrow_m+ YELLOW + " Enter Roll No. To Update : " + END)
    
    index_student = None
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll == row[3]:
                    index_student = counter
                    print('\n')
                    print(PURPLE+'\t------RECORD FOUND------'+END)
                    print(box+GREEN+"Student Found At Index No "+END,index_student)
                    student_data = []
                    for field in student_fields:
                        value = input(arrow_m +YELLOW+ " Enter New " + field + ": " + END)
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1
 
 # Check if the record is found or not
    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
            print('\n')
            print(tick+GREEN_WHITE + " Data Updated Successfully ! " + END)
            continue_msg()
    else:
        print(box+RED+"ALERT!"+END)
        print(RED+' ×'*20+END)
        print(RED+" Student Not Found In Our Database !!!" +END)
        continue_msg()
        

#function delete students
def delete_student():
    print(result_5)
    
    roll = input(arrow_m+ YELLOW + " Enter Roll No. To Delete : " + END)
    
    student_found = False
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll != row[3]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
            
            print('\n')
        print(tick+GREEN_WHITE+"Roll no.", roll, "Deleted successfully"+END)
        continue_msg()
    else:
    	print(box+RED+"ALERT!"+END)
    	print(RED+' ×'*20+END)
    	print(RED+" Roll No. Not Found In Our Database !!!" +END)
    	continue_msg()

name_1 = 'Vivek Malviya'
name_2 = 'Gopal Kalsiya'
name_3 = 'Deepesh Rathore'
name_4 = 'Naval Barodh'

designation_1 = 'Student'
designation_2 = 'Student'
designation_3 = 'Student'
designation_4 = 'Student'

class_1 = 'XII(PCB)'
class_2 = 'XII(PCM)'
class_3 = 'XII(PCM)'
class_4 = 'XII(PCM)'


#about us wala function
def about_us():
	print(result_6)
	
	z = PrettyTable()
	z.field_names = [PURPLE+"Team member","Designation","class"+END]
	
	z.add_row([name_1, designation_1,class_1])
	z.add_row([name_2, designation_2,class_2])
	z.add_row([name_3, designation_3,class_3])
	z.add_row([name_4, designation_4,class_4])
	
	print(z)
	
	continue_msg()



while True:
    display_menu()

    choice = input(arrow+w_input)
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
    	print('\n')
    	print(box+PURPLE+"Thanks For Using Our Student Management System"+END)
    	
    	print(box+YELLOW+"Quitting...."+END)
    	time.sleep(2)
    	print(end_banner)
    	quit()
    else:
    	   print(box+RED+'Sorry! Enter a valid input !'+END)
    	   break