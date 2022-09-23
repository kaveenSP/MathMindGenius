import random
print("Welcome To The Magic Game")
start=input("Are you ready ?(yes/no)\n")
if start.lower()=="yes":
    print("Guess a number")
    input("Press Enter")
    var1=random.randint(1,25)
    print(f"Add {var1}")
    input("Press Enter")
    var2=random.randint(1,25)
    print(f"Now add {var2} again")
    input("Press Enter")
    var3 = random.randint(1, 25)
    print(f"Now subtract {var3}")
    input("Press Enter")
    print("Now multiply by 2")
    input("Press Enter")
    varx = (var1 + var2 - var3)*2
    var4 = random.randint(1, 25)
    print(f"Now add {var4}")
    input("Press Enter")
    var5 = random.randint(1, 25)
    print(f"Now subtract {var5}")
    input("Press Enter")
    print("Now subtract the number you guessed before")
    input("Press Enter")
    var6 = random.randint(1, 25)
    print(f"Now add {var6}")
    input("Press Enter")
    print("Now again subtract the number you guessed before")
    input("Press Enter")
    var7 = random.randint(1, 25)
    print(f"Now subtract {var7}")
    input("Press Enter")
    varx1 = varx + var4 - var5 + var6 - var7
    if(varx1%2==0):
        print("Now divide by 2")
        input("Press Enter")
        varx1=varx1/2
        var8 = random.randint(1, 25)
        print(f"Now subtract {var8}")
        input("Press Enter")
        varx2 = varx1 - var8
        if(varx2<0):
            while varx2<0:
                var9 = random.randint(1, 25)
                print(f"Add {var9}")
                input("Press Enter")
                varx2 = varx2 + var9
            var10 = random.randint(1, 25)
            print(f"Finally ! Add another {var10}")
            input("Press Enter")
            var10 = varx2 + var10
            print(f"Your answer is {var10}")
        else :
            var10 = random.randint(1, 25)
            print(f"Finally ! Add another {var10}")
            input("Press Enter")
            var10 = varx2 + var10
            print(f"Your answer is {var10}")
    else :
        print("Now add 1")
        input("Press Enter")
        varx1 = varx1 + 1
        print("Now divide by 2")
        input("Press Enter")
        varx1 = varx1 / 2
        var8 = random.randint(1, 25)
        print(f"Now subtract {var8}")
        input("Press Enter")
        varx2 = varx1 - var8
        if (varx2 < 0):
            while varx2 < 0:
                var9 = random.randint(1, 25)
                print(f"Add {var9}")
                input("Press Enter")
                varx2 = varx2 + var9

            var10 = random.randint(1, 25)
            print(f"Finally ! Add another {var10}")
            input("Press Enter")
            var10 = varx2 + var10
            print(f"Your answer is {var10}")
        else:
            var10 = random.randint(1, 25)
            print(f"Finally ! Add another {var10}")
            input("Press Enter")
            var10 = varx2 + var10
            print(f"Your answer is {var10}")
else:
    print("Ooops ! You lost the fun")
