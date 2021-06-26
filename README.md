# [Python] zip 파일 비밀번호 무차별 대입 공격(brute-force attack)

1-1) dictionary.py

![1](https://user-images.githubusercontent.com/85146195/123520825-b78d0e00-d6ed-11eb-8b62-3062d73366a4.JPG)

Input에 조합할 문자들을 모두 나열해서 적는다. 자릿수 범위는 코드부분에 들어가서 수정해줘야 한다. 현재는 5자리로 자동 생성된다.
#

![2](https://user-images.githubusercontent.com/85146195/123520834-ce336500-d6ed-11eb-8d2a-294c32381318.jpg)

brute_force.txt 라는 파일이 생성되는 것을 볼 수 있다. 이 파일을 통해 zip 파일의 비밀번호를 뚫어볼 것이다.
#

1-2) unlock_zip.py

![3](https://user-images.githubusercontent.com/85146195/123520951-88c36780-d6ee-11eb-8533-c902819ff780.JPG)

zip file path와 dictionary file path 경로를 지정해주면 자동으로 대입되고, 비밀번호가 일치하면 그 값을 출력한다.
출력된 비밀번호로 압축파일 속의 정보들을 확인할 수 있다.
#

