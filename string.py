s="***Preyanshu trivedi is a good boy.***"
print(s)
s=s.lstrip('*')
print(s)
s=s.rstrip('*')
print(s)
s=s.replace(' ','-')
print(s)
s=s.upper()
print(s)
s=s.lower()
print(s)
search=input("Enter string to search:")
print("Result:",s.find(search))
