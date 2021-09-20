#palindrome
mywordarray=[]
myreversedarray=[]
word = input("enter your string: ")

for char in word:
  mywordarray.append(char)          # append the characters in the end of array ( like queue)
  myreversedarray.insert(0,char)    # add the characters at beginning  of another(like stack)

if mywordarray==myreversedarray:    # compare the two arrays elements
  print("its palindrome")
else :
  print("its not palindrome")
