# def welcome_msg():
#     print('welcome to my program')
# welcome_msg()

# def add_two_nums(num1,num2):
#     return num1+num2

# result=add_two_nums(5,5)
# print(result)

# def even_or_odd():
#     num=int(input('please give a number:'))
    
#     if num % 2 == 0:
#         print('this is an even number')
#     else:
#         print('this is an odd num')

# even_or_odd()


def enter_marks():
    marks={}
    subjects=['eng','maths','kisw']
    for subject in subjects:
        mark=int(input(f'what did you get in {subject}:'))
        if mark <= 0 or mark >= 100:
            print('mark must be between 1-99')
            break
        else:
            marks[subject]=mark
    return marks

def calculate_average(marks):
    if not marks:
        return 0
    return sum(marks.values()) / len(marks)

def calculate_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "E"
    
def add_remarks(grade):
    if grade == 'A':
        return 'awesome grade'
    elif grade == 'B':
        return 'amazing grade'


marks=[]  
while True:
    print("\nImproved Student Marks System")
    print("1. Enter Marks")
    print("2. Show Average")
    print("3. Show Grade")
    print("4. Exit")

    choice = input("Choose 1-4: ")
    if choice == '1':
        marks=enter_marks()
        print('marks saved ')
    elif choice == '2':
       if not marks:
            print("❌ Please enter marks first")
       else:
           avg_mark=calculate_average(marks)   
           print(avg_mark)   
    elif choice =='3' :
       if not marks:
            print("❌ Please enter marks first")
       else:
            avg = calculate_average(marks)
            grade = calculate_grade(avg)
            remark=add_remarks(grade)
            print("Grade:", grade,'Remark:',remark)
    elif choice == '4' :
        print('goodbye')
        break        
    else:
        print('invalid input')


    
    



       

   