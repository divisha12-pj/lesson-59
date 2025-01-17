num1=int(input("enter the numbeer"))
num2=int(input("Enter the Number"))
largernum=num1
smallnum=num2


while smallnum:
    num=smallnum
    smallnum=largernum%smallnum
    largernum=num


    lcm=(num1*num2)//largernum
    print("LCM OF {} AND {} IS {}".format(num1,num2,lcm))