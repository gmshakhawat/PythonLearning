class human():
    type="student"
    sex="male"
    age=18
    yt="pola"
    @property
    def get_sex(self):
        print(self.sex)

    @property
    def get_age(self):
        print(self.age)

    @property
    def get_type(self,kw='you'):
        print(kw+' '+self.type)




class myclass(human):
    name="shakhawat"
    type="fakibaz"
    # def bc(self):
    #     print(self.name,self.type)

obj=myclass()
print(obj.name)
yt='polaa'
obj.get_type
obj.get_sex
obj.get_age
obj.type="employe"
obj.get_type


