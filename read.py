from datetime import datetime
saved_username='rosevase'
attempts=0
with open('attempts.txt','a') as file:
    while attempts < 3:
        username=input('type username:')
        if username != saved_username:
           attempts += 1
           file.write(f'{attempts}: {username} at {datetime.now()}\n')
           print('incorrect username')
        else:
             print('correct username')
             break

with open ('attempts.txt','r') as file:
     for line in file:
        print(line.strip())
