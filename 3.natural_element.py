#first natural element
mylist=[1,2,3,5,6.5,8]
index=1
for item in mylist:
  if item == index:
    index=index+1
  else:
    exit
print(index)
