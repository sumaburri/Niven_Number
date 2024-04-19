number=int(input('Enter a Number : '))
copy=number
add=0
while(number!=0):
    rem=number%10
    add=add+rem
    number=number//10
if copy%add==0:
    print('Niven Number')
else:
    print('Not A Niven Number')
    
    
