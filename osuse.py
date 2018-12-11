import os
f=open("moduleos.txt","w")
data=os.__doc__
f.write(data)
f.close()
