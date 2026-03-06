from collections import deque

q = deque([1, 2, 3, 4, 5])

def reverseQueue(q):
    st = []
    
    while q:
        st.append(q.popleft())
    
    while st:
        q.append(st.pop())
    
    return q

print(reverseQueue(q))