class MyStack:
    def __init__(self):
        self.queue1 = deque() # Main queue
        self.queue2 = deque() # Helper queue

    def push(self, x: int) -> None:
        # Add the new element to queue1
        self.queue1.append(x)

    def pop(self) -> int:
        # Transfer all elements except the last to queue2
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        # Remove the last element (top of the stack)
        top_element = self.queue1.popleft()
        # Swap queues
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top_element

    def top(self) -> int:
        # Similar to pop, but do not remove the last element
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        # Peek the last element
        top_element = self.queue1.popleft()
        self.queue2.append(top_element)  # Put it back in queue2
        # Swap queues
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top_element

    def empty(self) -> bool:
        # Check if queue1 is empty
        return not self.queue1
