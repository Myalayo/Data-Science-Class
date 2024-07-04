class Parent():
    def __init__(self, Name, Stature, Nose):
        self.name = Name
        self.Stature = Stature
        self.Nose = Nose
    def Dparent(self):
        print(f"My name is {self.name}. I've got a {self.Stature} stature and my nose is {self.Nose}.")

class Child(Parent):
    def Childern (self,Colour):
        self.Colour = Colour 
        print(f"My name is {self.name}. I've got a {self.Stature} stature and my nose is {self.Nose}cm. I am also {self.Colour} in colour.")

class Grandchild (Child):
    def GrandChildern(self, Height): 
        self.Height = Height
        print(f"My name is {self.name}. I've got a {self.Stature} stature and my nose is {self.Nose}. I am also {self.Height} tall.")

Person1 = Parent("Alayo", "small", "Pointed")
Person2 = Child("Olabisi", "big", "round") 
Person3 = Grandchild("Eniolanime", "normal", "round")     

Person1.Dparent()
Person2.Childern("fair")
Person3.GrandChildern(6.9)