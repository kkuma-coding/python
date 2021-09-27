'''
전체 page 수와 뜯고자 하는 특정 페이지를 입력 받아
함께 뜯겨지는 연관된 세 개의 페이지를 구하는
프로그램을 작성하시오
'''
pages, target_page = input().split()
pages, target_page = int(pages), int(target_page)

'''
1,  (11)   12
2,  (9)  11

3   (7)  10
4   (5)  9

5   (3) 8
6   (1) 7
'''

page_sequence = range(1, pages +1)

groups = []
gap = pages - 1
for i in range(0, pages // 2, 2):
    groups.append(list([page_sequence[i],
                        page_sequence[i+1],
                        page_sequence[-1-i],
                        page_sequence[-1-(i+1)]]))

for l in groups:
    if target_page in l:
        l.remove(target_page)
        l.sort()
        print (l)