class A:
    def __init__(self):
        self.number = 0

    def edit_value(self, num):
        self.number = num

class B:
    def __init__(self):
        self.list = list()

    def add_ele(self, instance_A):
        self.list.append(instance_A)

    def get_ele(self):
        return self.list[-1]

a = A()
b = B()
b.add_ele(a)
x = b.get_ele()
x.edit_value(100)
for e in b.list:
    print(e.number)
