# did you know while else loop?
secret_number = 9
i = 0
while i<3:
    num=input("guess the number ")

    if int(num)==secret_number:
        print("You win")
        break

    i=i+1

else:
    print("you lose")

