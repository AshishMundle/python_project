# reading data from a file 

f=open("covid.txt","r")
print(f.read())
print(f.read(5))
print(f.readline())
print(f.readlines())
f.close()