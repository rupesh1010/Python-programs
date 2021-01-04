s=0
n=121
x=n
while(n>0):
    r=n % 10
    s=s * 10 + r
    n=n / 10
if s==x:
    print('this is palindrome number')
else:
    print('this is not')
