score = int(input())
if 100 >= score >= 90:
    print('A')
elif 90 > score >= 80:
    print('B')
elif 80 > score >= 70:
    print('C')
elif 70 > score >= 60:
    print('D')
else:
    print('F')

#score 라는 variable을 int로 값을 받고
#if+else인 elif를 사용하여 많은 조건을 만들고
# socore가 90보다 작고 80보다 크거나 같으면 이런식으로
#조건을 씁니다.
