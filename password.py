password = 'a12345'
i = 3
while i > 0: 
    i = i - 1
    pwd = input('please enter your password : ')
    if pwd == password:
        print('logging successfully')
        break
    else:
        print('wrong password')
        if i == 2:
            print(i, 'times remaining')
        if i == 1:
            print('last chance')
        if i == 0:
            print('goodbye')
            break
        


