# Info
[27313_효율적인 애니메이션 감상](https://www.acmicpc.net/problem/27313)

## 💡 풀이 방법 요약

시청 가능한 애니메이션의 갯수를 매개 변수로 두고, 이를 탐색으로 찾아갔습니다.

최대 100,000 개가 될 수 있어 혹시몰라 이분탐색으로 찾았습니다.

애니메이션의 시간을 내림차순으로 정렬한 이후에, k개씩 끊어서 시청 시간을 더해주었습니다.

t 시간이 소요되는 애니메이션을 볼 때에 무슨 애니메이션을 같이 봐도 t 만큼의 시간이 소요되므로

t 이하의, 가장 큰 시간을 가지는 애니메이션을 보는 것이 논리적으로 최단 시간을 계산할 수 있는 방법입니다.

## 👀 실패 이유

이분 탐색 조건이나 그 외 잡다한 오류들로 인한 실패입니다.

## 🙂 마무리

