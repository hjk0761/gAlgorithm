# Info
[29754 세상에는 많은...](https://www.acmicpc.net/problem/29754)

## 💡 풀이 방법 요약

시간 파싱 - 분으로 환산해 차이를 구함

전체 이름을 가지는 집합 계산

방송 목록을 날짜별로 정리해서 한 주 단위로 이름을 키로 dictionary 를 만들어 횟수와 시간을 합산해주었다.

한 주가 넘어가는 날이 되었을 때 이전 주까지의 dictionary 를 순회해서 5회, 3600분이 넘어가는 이름 목록을 구한 후 앞서 구한 전체 이름과 교집합 계산을 하여 이를 유지

마지막 날까지 계산을 한 이후 주가 바뀌지 않았을 경우를 고려해 방송 목록 마지막에 M + 7(6이여도 됨) 인 날짜를 가지는 방송을 하나 추가해서 마지막 주도 정산하도록 계산


## 👀 실패 이유

16퍼.. 16퍼... 16퍼... 알고리즘을 바꿨더니 키에러 * 3, 다시 원래 알고리즘으로 돌아와 좀 더 생각해보니 맞았다.

## 🙂 마무리

백준은 테케를 공개해라!