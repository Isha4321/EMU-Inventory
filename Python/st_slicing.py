name = "ishagupta"
print(name[4:-1])
num= input("Enter a number:")
match num:
    case 0:
        print("Entered number is",num)
    case 1:
        print("Entered number is",1)
    case _:
        print(num)       