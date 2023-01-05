class Laptop:
    a="laptop"#class variable
    def __init__(self,ram,rom):
        print(self)
        self.RAM=ram#instance variable
        self.ROM=rom

    def booting(self):
        print("Booting....")
dell=Laptop(4,512)
hp=Laptop(6,1024)
print("dell=",dell)            