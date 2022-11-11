**RuntimeError(IndexError)**
1. sort()가 너무 오래 걸렸나? -> 아님
2. -0을 0으로 바꿔주는 avg()가 너무 오래 걸렸나> -> 아님
3. n = 1인 경우 최빈값 구하기  
  -> most_common 0번째와 1번째를 비교하는 코드르 작성했는데,   
     n = 1이면 most_common 후 생성된 리스트의 원소의 개수가 1개뿐이라 IndexError 발생   
  => if n == 1인 경우를 추가하여 해결 !
