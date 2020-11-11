from collections import deque


queue = deque(maxlen=3)
queue.append('Joseph')
print(queue)
queue.append('Caolan')
print(queue)
queue.append('Freya')
print(queue)
queue.pop()
print(queue)
queue.popleft()
print(queue)
queue.append('Susan')
queue.append('Conor')
print(queue)
queue.append('Aoife')
print(queue)