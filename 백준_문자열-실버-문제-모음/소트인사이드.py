#백준 1427 : 소트인사이드 (https://www.acmicpc.net/problem/1427)
print(''.join(sorted(input(),reverse=True)))

#문자열은 sort로 정렬 불가 - > - str type에 sort()라는 메소드가 없기 때문(이유는 string의 경우 첫글자의 주소값으로 참조를 하기에 원본이 변경되면 안된다.)
#대신 sorted(s)처럼 쓰는 것은 가능하다. - 대신 return type은 list이다.
#이를 하나로 이어진 문자열로 만들기 위해선 ''.join을 사용하면 된다.
#출처 : https://otugi.tistory.com/268
