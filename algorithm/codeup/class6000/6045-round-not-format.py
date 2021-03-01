# https://codeup.kr/problem.php?id=6045
'''
이 문제는 round()를 쓰고 format을 쓰지 말라는 것이다

"{:.02f}".format(num) 을 사용하면, 언제나 항상 소수점 2자리 수를 표현하지만
round()를 사용하면, 최대 2자리의 소수점을 표현할 수 있게 된다. 이 문제를 round()를 쓰라는 것이다.
'''
my_list = list(input().split())
dec_list = [int(a) for a in my_list]
sum = sum(dec_list)
print(sum, round(sum/len(dec_list), 2))
# print(sum, "{:.02f}".format(sum/len(dec_list)))