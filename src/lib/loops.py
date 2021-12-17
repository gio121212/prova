for i in range(1,10):
  x=i*i
  print(x)
else:
  print('else executed')

for i in range(1,10):
  x=i*i
  
  if x > 60: 
    print('else not executed')
    break
  print(x)
else:
  print('else executed')




print("\nFinchè hai voglia ti converto in binario \nun intero positivo che mi dai.")
while True: 
  a = int(input("Dammi un intero positivo:")) 

  bin_list=[]

  while(a != 0):
    b = a // 2
    bin_list.append(a % 2)
    bin_list.reverse()
    a = b
  
  string = ' '.join(map(str, bin_list))
  
  print("Nel sistema binario il tuo intero è:")
  print(string)

  a = str(input("Vuoi uscire? y/n\n"))
  if a == 'y':
    break
  else:
   continue

