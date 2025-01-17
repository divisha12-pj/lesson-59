num=int(input('enter the input number'))
temp=num
rev=0

while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10

if rev==num:
      print(num,"is palindrome")
else:
      print(num,"is not palindrome")

