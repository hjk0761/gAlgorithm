# Info
[18428 감시 피하기](https://www.acmicpc.net/problem/18428)

## 💡 풀이 방법 요약
1. 장애물 두기
   - dfs를 이용해 0행 0열부터 빈 공간에 장애물 하나씩 두며 탐색
2. 장애물이 3개가 되는 순간 가능 여부 확인
   - 선생님의 위치를 기준으로 사방으로 학생 확인
   - 장애물이나 다른 선생님이 존재할 경우 확인 정지
   - 학생을 만난 경우 바로 리턴
   - 모든 선생님이 학생을 만나지 않은 경우 YES 출력 후 종료
3. 모든 장애물의 경우에서 성공하지 못한 경우 NO 출력 후 종료

## 👀 실패 이유

## 🙂 마무리
장애물을 두는 모든 경우를 어떻게 구현해야 할 지 감이 안잡혀 찾아보고 구현함...
