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

) static_StartEnd_unlock_zip.py

![4](https://user-images.githubusercontent.com/85146195/123521194-3420ec00-d6f0-11eb-9b06-501855a3e5ea.JPG)

비밀번호의 앞의 '25'인 것을 알고 있을 경우 static_start_char에 '25'를 입력한다.  
25는 비밀번호에 고정되고 나머지 자리를 입력받은 chars의 모든 경우의 수로 대입한다.  
앞 또는 뒤에서 고정된 비밀번호를 사용하게 되면 그만큼 경우의 수가 줄어든다.  
#
  
  
) oneclick_unlock_zip.py

![5](https://user-images.githubusercontent.com/85146195/123521395-4b140e00-d6f1-11eb-9f68-b7c444f2218b.JPG)

비밀번호를 아는 자리는 입력하고, 모르는 자리는 [space bar]를 입력한다.  
공백도 하나의 자리로 인식하기 때문에 공백으로 원하는 자릿수만큼 채워줘야한다.  
고정된 비밀번호를 제외한 나머지 자리를 입력받은 chars의 모든 경우의 수로 대입한다.  
자릿 수를 문자와 공백으로 지정해주기 때문에 자릿 수를 따로 입력받지 않는다.  
#

tistory : https://she11.tistory.com/79  
#
