# import random
# secret_number=random.randint(1,10)
# attempts=0

# while attempts < 5:
#     guess=int(input('guess a number between 1-10:'))

#     print(secret_number)
#     if guess <1 or guess>10:
#         print('number cannot be less than one or greater than 10')
#         continue
#     attempts += 1
#     if guess == secret_number:
#         print(f'You guessed right in {attempts} attempts')
#         break
#     else:
#         if guess < secret_number:
#             print('too low')   
#         elif guess > secret_number:
#             print('too high')    
marks=[]
while True:
    print('Markdown')
    print('1.Enter marks')
    print('2.Show marks')
    print('3.Exit')
    choice=int(input('Choose 1-3:'))
    if choice == 1:
        Maths=int(input('Enter maths mark:'))
        english=int(input('Enter English mark:'))
        Kisw=int(input('Enter kisw mark:'))
        Sci=int(input('Enter science mark:'))
        Cre=int(input('Enter cre mark:'))
        marks.append(Maths)
        marks.append(english)
        marks.append(Kisw)
        marks.append(Sci)
        marks.append(Cre)
        print(sum(marks))
       




