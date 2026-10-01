from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        shm = Counter(text)

        return min(
            shm.get('b', 0),
            shm.get('a', 0),
            shm.get('l', 0) // 2,
            shm.get('o', 0) // 2,
            shm.get('n', 0)
        )