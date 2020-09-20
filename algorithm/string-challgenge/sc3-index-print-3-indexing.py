a = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth"]

print (a[-1::])

print (a[0:6:-1]) # 비어있는 list 가 됩니다.
print (a[::-1]) # list의 순서를 뒤집게 됩니다.

# list 앞의 3개 item을 출력 해 줍니다.
print (a[0], a[1], a[2])
print (a [0:3])

# 1번 list 부터 3개를 출력 해 줍니다.
print (a[1], a[2], a[3])
print (a [1:4])

# 3번 list 부터 끝까지 출력 해 줍니다.
print (list[3:])

# ['First', 'Second', 'Third']
# ['Fourth', 'Fifth', 'Sixth']
# ['First', 'Third', 'Fifth']
# []
# ['Sixth', 'Fifth', 'Fourth', 'Third', 'Second', 'First']
