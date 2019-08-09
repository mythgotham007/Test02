class Users:
    name=""
    def __init__(self,name):
        self.name=name
    def sayHello(self):
        print('Hi ' + self.name)
jj=Users('jame')
mm=Users('Mike')

jj.sayHello( )

class coffeemc:
    name=''
    bean=0
    milk=0
    water=0
    def __init__(self,name,bean,milk,water):
        self.name=name
        self.bean=bean
        self.milk=milk
        self.water=water
    def sayhello(self):
        print('say hello to  ' +str(self.name))
    def addbean(self):
        self.bean=self.bean+1
    def removebean(self):
        self.bean=self.bean-1
    def addbmilk(self):
        self.milk=self.milk+1
    def removemilk(self):
        self.milk=self.milk-1
    def addwater(self):
        self.water=self.water+1
    def removewater(self):
        self.water=self.water-1
    def printState(self):
            print ("Name  = " + self.name)
            print ("Beans = " + str(self.bean))
            print ("Water = " + str(self.water))
            print ("milk = " + str(self.milk))

pythonBean = coffeemc("Python Bean", 83, 20,23)
pythonBean.printState()
pythonBean.printState()
pythonBean = coffeemc("Python Bean1", 33, 33,42)
pythonBean1.printState()
pythonBean1.printState()
                
            