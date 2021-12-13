print('hello')
print('hi')

class MingBabo:

    def __init__(self, name):
        self.Name = name

    def SayBabo(self, name):
        for x in range(5):
            print(name +'babo')
            
name='ming'
ming = MingBabo('ming')
ming.SayBabo('민석')