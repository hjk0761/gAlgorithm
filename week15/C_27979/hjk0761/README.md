# Info
[볼링장 아르바이트](https://boj.kr/27979)

## 💡 풀이 방법 요약

움직일 필요가 없는 애들의 수를 세서 전체 개수에서 뺐습니다.

움직일 필요가 없는 애들을 판단하는 로직은 현재 놓인 상태를 뒤에서부터 보면서 내림차순으로 정렬된 것과 비교하는 것입니다.

뒤에서부터 보면서 내림차순 정렬된 수와 같으면 정렬된 인덱스를 하나 줄여가면서 카운트를 늘리면 됩니다.

## 👀 실패 이유

움직여야 하는 것들의 갯수를 셌는데 로직이 틀렸었나 봅니다.

## 🙂 마무리
