while True:
    inc = int(input("Enter Addition Cipher Key Value: "))
    data = input("Enter Data: ")
    ans = []
    print('''Enter a choice:
        1: For encryption
        2: For decryption''')
    choice = int(input())
    if choice==1:
        for i in data:
            ans.append(chr((ord(i)+inc)%128))
    elif choice==2:
        for i in data:
            ans.append(chr((ord(i)+128-inc)%128))
    else:
        print("Enter a valid choice")
    print(''.join(ans))

'''
Output:-
Enter Addition Cipher Key Value: 3
Enter Data: hello
Enter a choice:
        1: For encryption
        2: For decryption
1
khoor
Enter Addition Cipher Key Value: 3
Enter Data: khoor
Enter a choice:
        1: For encryption
        2: For decryption
2
hello
'''
