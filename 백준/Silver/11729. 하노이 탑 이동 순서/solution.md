### 1. 이동 과정 구하기  
가장 작은 판(1) ~ 가장 큰 판(N)일 때,   
(N - 1)판까지 모두 중간 기둥으로 보내고 N판을 제일 오른쪽 기둥으로 보냄  

### 2. 이동 횟수 구하기
- sol1. global 변수 count 선언해서 재귀함수의 횟수 세기  
  => 횟수가 가장 마지막에 구해지기 때문에 출력 시 문제 조건에 맞지 않음  
  
- sol2. 일반항 구하기  
  <img width="674" alt="스크린샷 2022-11-13 오후 1 45 54" src="https://user-images.githubusercontent.com/69826406/201506371-6b229b96-a8de-44c8-a17e-2dcfeec74f9f.png">
  [블로그 참고](https://shoark7.github.io/programming/algorithm/tower-of-hanoi)
