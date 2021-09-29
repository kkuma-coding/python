def spam(eggs):
    "__call_by_reference__"
    eggs.append(1)  # 기존 객체의 주소값을 참조하여 [1] 추가
    eggs = [2, 3]  # eggs는 새로운 객체 주소값 저장


ham = [0]
spam(ham)
print(ham)

help(spam)