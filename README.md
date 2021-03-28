# Baekjun_No2
백준 온라인 문제풀이 사이트의 문제를 푸는 커밋입니다.

<h1>두 수 비교하기 1330</h1>

두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.<br>
첫째 줄에 다음 세 가지 중 하나를 출력한다.<br>
A가 B보다 큰 경우에는 '>'를 출력한다.<br>
A가 B보다 작은 경우에는 '<'를 출력한다. <br>
A와 B가 같은 경우에는 '=='를 출력한다. <br>
  
<pre>
<code>
    a,b  = map(int,input().split())
if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')
</pre>
</code>

<strong>처음에는 a,b를 한번에 int의 입력값을 받으면서 리스트를 나눠두고 
문제에서 시키는대로 a > b 일시에는 > 를 출력 이런식으로 코드를 작성합니다. </strong>

<h1>시험성적 9498</h1>
시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.<br>
첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

<pre>
<code>
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
</pre>
</code>

<strong>처음에는 score라는 variable 을 지정합니다. 그후에 score는 int로 입력값을 받는다고 선언을 한후 조건문을 작성합니다. <br>
  첫번째줄 코드는 "만약 score가 100보다 작거나 같고 , 90보다 크거나 같다면 A를 출력시켜주세요" 라는 코드입니다.
  그러면 두번째 줄도 똑같은데요 "만약 score가 90보다 작고 , 80보다 크거나 같다면 B를 출력시켜주세요" 라는 코드였습니다.
</strong>

<h1>윤년 2753</h1>
연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.

윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.

예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다. 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다. 하지만, 2000년은 400의 배수이기 때문에 윤년이다.

<pre>
<code>
a = int(input())
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print(1)
else:
    print(0)
</pre>
</code>

<strong>이 문제는 어려워서 해설을 추가해야할거 같습니다. 양해바랍니다.
  <a href="https://pacific-ocean.tistory.com/72">해설링크</a>
</strong>

<h1>사분면 고르기 14681</h1>
이 문제는 그림자료를 보고 풀어야하기에 링크를 남깁니다 . <br>보고 참고해주시면 감사하겟습니다
<a href="https://www.acmicpc.net/problem/14681">사분면 고르기 문제링크 </a>

<pre>
<code>
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("1")
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
else:
    print('4')
</pre>
</code>

<strong>
문제를 보셨다면 알겟지만 , 이런 문장이 있습니다.<br>
'점 A는 x좌표와 y좌표가 모두 양수이므로 제1사분면에 속한다. 점 B는 x좌표가 음수이고 y좌표가 양수이므로 제2사분면' 
우선 저가 생각한것은 음수와 양수였습니다. <br>

음수: 0이 x보다 큰것 즉 - 라고 말하겟죠?
양수: 0이 x보다 작은것 즉 + 라고 말합니다.
<br>
그러면 우선 A는 x좌표와 y좌표가 모두 양수이니 1사분면에 속한다고 했는데 , 그러면 코드처럼 and를 사용해서
"둘다 충족시" 출력을 시키는 문제입니다.

</strong>
 
<h1>알람 시계 2884</h1>
상근이는 매일 아침 알람을 듣고 일어난다. 알람을 듣고 바로 일어나면 다행이겠지만, 항상 조금만 더 자려는 마음 때문에 매일 학교를 지각하고 있다.
상근이는 모든 방법을 동원해보았지만, 조금만 더 자려는 마음은 그 어떤 것도 없앨 수가 없었다.
이런 상근이를 불쌍하게 보던, 창영이는 자신이 사용하는 방법을 추천해 주었다.
바로 "45분 일찍 알람 설정하기"이다.

이 방법은 단순하다. 원래 설정되어 있는 알람을 45분 앞서는 시간으로 바꾸는 것이다. 어차피 알람 소리를 들으면, 알람을 끄고 조금 더 잘 것이기 때문이다. 이 방법을 사용하면, 매일 아침 더 잤다는 기분을 느낄 수 있고, 학교도 지각하지 않게 된다.
현재 상근이가 설정한 알람 시각이 주어졌을 때, 창영이의 방법을 사용한다면, 이를 언제로 고쳐야 하는지 구하는 프로그램을 작성하시오.

---------------------------------------------------------------------------------------------------------

첫째 줄에 두 정수 H와 M이 주어진다. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 그리고 이것은 현재 상근이가 설정한 놓은 알람 시간 H시 M분을 의미한다.

입력 시간은 24시간 표현을 사용한다. 24시간 표현에서 하루의 시작은 0:0(자정)이고, 끝은 23:59(다음날 자정 1분 전)이다. 시간을 나타낼 때, 불필요한 0은 사용하지 않는다.

<br>

<pre>
<code>
H,M = map(int,input().split())

if M > 44:
    print(H,M-45);
elif M < 45 and H > 0:
    print(H-1,M+15)
else:
    print(23,M+15)
</pre>
</code>

<strong> 이 문제 또한 너무 어려웠기에 검색자료 링크를 남깁니다 죄송합니다.
          <a href="https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-2884%EB%B2%88-%EC%95%8C%EB%9E%8C-%EC%8B%9C%EA%B3%84-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython">해설 링크</a>입니다. 감사합니다.
  
# Baekjun_No2(ENG.Ver)
<h6>All translations inform you that Google Translator was used.</h6>
This is a commit that solves the problem of the Baekjun online problem solving site.

<h1>Compare two numbers 1330</h1>

Given two integers A and B, write a program that compares A and B.<br>
On the first line, print one of the following three things:<br>
If A is greater than B,'>' is output.<br>
If A is less than B,'<' is output. <br>
If A and B are the same,'==' is output. <br>
  
<pre>
<code>
    a,b = map(int,input().split())
if a> b:
    print('>')
elif a <b:
    print('<')
else:
    print('==')
</pre>
</code>

<strong>At first, a,b is divided into a list while receiving an input of an int at a time.
Write the code in this way, as the problem tells you to output a> b at the time>. </strong>

<h1>Test score 9498</h1>
Write a program that receives test scores and outputs A for 90 to 100 points, B for 80 to 89 points, C for 70 to 79 points, D for 60 to 69 points, and F for the remaining points.<br>
Test scores are given on the first line. The test score is an integer greater than or equal to 0 and less than or equal to 100.

<pre>
<code>
score = int(input())
if 100 >= score >= 90:
    print('A')
elif 90> score >= 80:
    print('B')
elif 80> score >= 70:
    print('C')
elif 70> score >= 60:
    print('D')
else:
    print('F')
</pre>
</code>

<strong>In the beginning, we specify a variable called score. After that, declare that score receives an input value as an int, and write a conditional statement. <br>
  The first line of code is "If the score is less than or equal to 100 and greater than or equal to 90, print A."
  Then the second line is also the same. It was a code that says, "If the score is less than 90 and greater than or equal to 80, print B."
</strong>

<h1>Leap year 2753</h1>
Given a year, write a program that prints 1 if it is a leap year, or 0 otherwise.

A leap year is when the year is a multiple of 4, not a multiple of 100, or a multiple of 400.

For example, 2012 is a leap year because it is a multiple of 4 and not a multiple of 100. Since 1900 is a multiple of 100 and not a multiple of 400, it is not a leap year. However, since 2000 is a multiple of 400, it is a leap year.

<pre>
<code>
a = int(input())
if (a% 4 == 0 and a% 100 != 0) or a% 400 == 0:
    print(1)
else:
    print(0)
</pre>
</code>

<strong>This problem is difficult, so I think I'll have to add some commentary. please understand.
  <a href="https://pacific-ocean.tistory.com/72">Explanation link</a>
</strong>

<h1>Select quadrant 14681</h1>
This problem has to be solved by looking at the picture material, so I leave a link. <br>I would be grateful if you see and refer to it.
<a href="https://www.acmicpc.net/problem/14681">Quadrant selection problem link </a>

<pre>
<code>
x = int(input())
y = int(input())

if x> 0 and y> 0:
    print("1")
elif x <0 and y> 0:
    print('2')
elif x <0 and y <0:
    print('3')
else:
    print('4')
</pre>
</code>

<strong>
If you have seen the problem, you know, but there is a sentence like this.<br>
'Point A belongs to the first quadrant because both the x and y coordinates are positive. Point B has a negative x-coordinate and a positive y-coordinate, so the second quadrant'
First of all, what I thought about was negative and positive numbers. <br>

Negative number: You would say that 0 is greater than x, that is, -?
Positive number: Says that 0 is less than x, that is, +.
<br>
Then, first of all, A said that it belongs to the first quadrant because both the x and y coordinates are positive. Then, using and like the code
This is a problem of outputting "when both are satisfied".

</strong>
 
<h1>Alarm clock 2884</h1>
The full-time worker wakes up after hearing the alarm every morning. It would be nice to wake up right away after hearing the alarm, but he's always late to school because of his desire to sleep a little longer.
Full-timer tried all the way, but he couldn't get rid of anything he wanted to sleep a little longer.
Changyoung, who was sorry for this full-time job, recommended the method he used.
That's "Set an alarm 45 minutes early."

This method is simple. This is to change the alarm that was originally set to a time that is 45 minutes ahead. Because if you hear the alarm sound anyway, you will turn off the alarm and sleep a little better. This way, you can feel like you slept more every morning, and you won't be late for school.
If you use Changyoung's method when the alarm time set by the current full-time worker is given, write a program to find when to fix it.

-------------------------------------------------- -------------------------------------------------- -----

Two integers H and M are given in the first line. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) And this means the alarm time H hours M minutes set by the current full-time employee.

The input time uses a 24-hour representation. In a 24-hour representation, the start of the day is 0:0 (midnight), and the end is 23:59 (one minute before midnight the next day). When representing time, unnecessary zeros are not used.

<br>

<pre>
<code>
H,M = map(int,input().split())

if M> 44:
    print(H,M-45);
elif M <45 and H> 0:
    print(H-1,M+15)
else:
    print(23,M+15)
</pre>
</code>

<strong> This problem was also too difficult to leave a link to the search material Sorry.
          <a href="https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-2884%EB%B2%88-%EC%95%8C%EB%9E%8C -%EC%8B%9C%EA%B3%84-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython">Explanation link</a>. Thank you.
  
 
  

