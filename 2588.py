
a = int(input())
b = int(input())

one = b%10
print( a * one )
ten = int(b/10)%10
print( a * ten )
hundred =int(int(b/10)/10) 
print( a * hundred )

print( a *one + a*ten*10 + a*hundred*100 )
