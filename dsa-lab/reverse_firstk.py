from collections import deque

q = deque([1, 2, 3, 4, 5])

def reverseFirstK(q, k):
    st = []
    
    if k > len(q) or k <= 0:
        return q
    
    for _ in range(k):
        st.append(q.popleft())
    
    while st:
        q.append(st.pop())
    
    for _ in range(len(q)-k):
        q.append(q.popleft())
    
    return q

print(reverseFirstK(q, 3))