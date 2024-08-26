#EXAMPLE 1
print('hello','world',sep='-',end='!!!\n')
#EXAMPLE 2
with open('output.txt','w')as file:
    print("hello","world",sep="-",end="!!!\n",file=file,flush=True)

