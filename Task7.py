class Animal:
    num_of_inst = 0
    def __init__(self):
        Animal.num_of_inst = Animal.num_of_inst + 1
    def print_num():
        print(Animal.num_of_inst)
    print_num = staticmethod(print_num)
    def voice(self):
        pass

class cow(Animal):
    def voice(self):
        return 'мууу'

class dog(Animal):
    def voice(self):
        return 'гав'

class cat(Animal):
    def voice(self):
        return 'мяу'

Nyasha = cow()
Sharik = dog()
Matroskin = cat()

print (Nyasha.voice())
print (Sharik.voice())
print (Matroskin.voice())
Animal.print_num()