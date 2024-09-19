class person:
    def set(self,name,age):
        self.name = name 
        self.age = age
    def output(self):
        print(f"Persona {self.name}, kuram ir {self.age} gadi")

p = person()
p.set("Peter",20)
p.output()

p = person()
p.set("Daniil",16)
p.output()