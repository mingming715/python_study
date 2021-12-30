import sys
input = sys.stdin.readline()

sum=0
num, base = map(int, input.split(' '))
num_list = str(num)
num_list_rev = num_list[::-1]
for i in range(len(num_list)):
   sum += int(num_list_rev[i]) * (base**i)
   
print(sum)





# print('hello')
# print('hi')

# class MingBabo:

#    def __init__(self, name):
#       self.Name = name

#    def SayBabo(self, name):
#       for x in range(5):
#             print(name +'babo')
            
# name='ming'
# ming = MingBabo('ming')
# ming.SayBabo('민석')

# list = [1, 2, 3, 4, 5]

# for a in enumerate(list):
#    print(type(a))
#    print('{} : {}'.format(*a))

# a = 3/0

# print("0으로 나눌 수 없습니다.")