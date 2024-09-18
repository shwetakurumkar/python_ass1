class queue:
    def __init__(self) -> None:
        self.queue = []
    def enqueue(self,item):
        self.queue.append(item)
        print(f"Enqueue:{item}")
    def dequeue(Self):
        if len(self.queue)<1:
            return "queue is empty"
        return Self.queue.pop(0)
    def disply(self):
        print("current queue:",self.queue)
    def size(self):
        return len(self.queue)
    
q = queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.disply()
print(f"dequeue:{q.dequeue()}")
q.disply()
print(f"size:{q.size()}")