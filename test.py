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

import queue as Q

q = Q.PriorityQueue()
print(type(q))
q.put(("v", 1, "f"))
q.put(("e", 1, "f"))
q.put(("a", 1, "f"))
print(q.get())
