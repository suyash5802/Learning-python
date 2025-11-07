class Dog():
    def __init__(self):
        self.result=[]
        
    def return_name(self,name):
        return self.result.append(name);
    def return_breed(self,breed):
        return self.result.append(breed)
    


dog1= Dog.return_name("rio","labra")
dog2= Dog.return_breed("rio","labra")
print(dog1)
print(dog2)
