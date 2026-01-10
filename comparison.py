
trials=0
while trials < 3:
    password=input('Please enter password to login:')
    if password=='rosevase':
        print('logging in')
        break
    else:
        trials+=1
        print(f're-enter password again {3-trials} trys left')
if trials == 3:
    print('account blocked')   