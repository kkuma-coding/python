from adult import Adult

class Police(Adult):
    pass


p = Police("haha")

print(p.get_name())
print(p.get_introduce_message())