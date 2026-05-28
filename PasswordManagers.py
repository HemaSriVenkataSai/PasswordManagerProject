passwords={}

while True:
    print("\nPassword Manager")
    print("1. Add Password")
    print('2. view password')
    print('3. exit')

    choice=input('enter yor choice: ')

    if choice=='1':
        website=input('enter website name: ')
        password=input('enter password: ')

        passwords[website]=password
        print('password saved sucessfully!!!!')

    elif choice=='2':
        if passwords:
            print('\n view password')
            for website,password in passwords.items():
                print(website ,':', password)
        else:
            print('No paswords saved.')


    elif choice=='3':
        print('exiting password manager !!!')
    else:
        print('Invalid choice...Try Again ')

