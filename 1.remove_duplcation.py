#remove dulpication
myarray=[]
try:
    while True:
      number = input("enter unique number: ")
      if number in myarray:          
          continue
      else:
        myarray.append(number)

except KeyboardInterrupt:
    print(myarray)