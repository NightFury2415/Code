import random
user1=input("enter the name of the first player \n")
user2=input("enter the name of the second player \n")
sum1=0
sum2=0
s=[15,28,31,50,66,78,82,88,94,97,99]
l=[1,19,24,40,56,63,80,85,89]
while sum1!=100 and sum2!=100:
  ch=(input(user1+ " press R to roll the dice\t"))
  if ch=='R':
    dice=random.randint(1,6)
    print("your dice roll is", dice)
    if sum1+dice<=100:
      sum1=sum1+dice
  
      a=random.randint(4,15)
      if sum1 in s:
        print("its a snake bite :( ")
        sum1=sum1-a
      if sum1 in l:
        print("its a ladder :) ")
        sum1=sum1+a
      if sum1<100:
        print("your current position is ", sum1)
        print()
      if sum1>=100:
        print(user1 + "has won the game")
        break
    else:
      print("try again in next turn :) ")
      print()
  ch1=(input(user2+ " press R to roll the dice\t"))
  if ch1=='R':
    dice=random.randint(1,6)
    print("your dice roll is", dice)
    if sum2+dice<=100:

      sum2=sum2+dice
      a=random.randint(4,15)
      if sum2 in s:
        print("its a snake bite :( ")
        sum2=sum2-a
      if sum2 in l:
        print("its a ladder :) ")
        sum2=sum2+a
      if sum2<100:
        print("your current position is ", sum2)
        print()
      if sum2>=100:
        print(user2 + "has won the game")
        print()
        break
    else:
      print("try again in next turn :) ")






