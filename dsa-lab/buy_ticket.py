from collections import deque
from typing import List

def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
    q = deque([x for x in range(len(tickets))])
    time_taken = 0
    while tickets[k] != 0:
        front = q.popleft()
        if tickets[front] == 0:
            continue
        else:
            tickets[front] -= 1
            time_taken += 1
            q.append(front)

    return time_taken

tickets = [2, 3, 2]
k = 2
print(timeRequiredToBuy(None, tickets, k))