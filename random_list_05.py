import random
mylist=list("ABCDEFGH")
# random.shuffle(mylist)
# print(mylist)
a = random.choices(mylist,k=3)
print(a)