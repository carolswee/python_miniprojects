# from datetime import datetime
# saved_username='rosevase'
# attempts=0
# with open('attempts.txt','a') as file:
#     while attempts <= 2:
#         username=input('type username:')
#         if username != saved_username:
#            attempts += 1
#            file.write(f'{attempts}: {username} at {datetime.now()}\n')
#            print('incorrect username')
#         else:
#              print('correct username')

with open ('attempts.txt','r') as file:
    content=file.readlines()
    print(content)
