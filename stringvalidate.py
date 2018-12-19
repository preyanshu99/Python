s=input()
s=list(s)
d=0
li=['isalnum','isalpha','isdigit','islower','isupper']
for var1 in range(len(li)):
    for var in range(len(s)):
        boo=(s[var].isalnum() if li[var]=='isalnum' else s[var].isalpha() if li[var]=='isalpha' else s[var].isdigit() if li[var]=='isdigit' else s[var].lower() if li[var]=='islower' else s[var].isupper())
        if boo==True:
            print("True")
            break
        d+=1
        if d==len(s):
            print("False")
