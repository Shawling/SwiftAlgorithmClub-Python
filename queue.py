""" 队列的实现。FIFO，入列出列都为O(1)，当达到条件时挪动队列元素，耗时O(n)。
注意队列边界的判断。
"""

class Queue(object):

    def __init__(self):
        self.entries = []
        self.length = 0
        self.front = 0

    def __str__(self):
        printed = str(self.entries[self.front:])
        return printed

    def enqueue(self, item):
        self.entries.append(item)
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        dequeued = self.entries[self.front]
        self.front += 1
        self.length -= 1

        # 达到一定比例，则数组元素位置调整，利用前面未被利用的区域，耗时O(n)
        if self.front / len(self.entries) > 0.25 and len(self.entries) > 50:
            for i in range(self.size()):
                self.entries[i] = self.entries[i + self.front]
        return dequeued

    def head(self):
        if self.length == 0:
            return None
        return self.entries[self.front]

    def size(self):
        return self.length


if __name__ == '__main__':
    queue = Queue()
    print(queue)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)
    print(queue.dequeue())
    print(queue)
    print(queue.dequeue())
    print(queue)
    queue.enqueue(2)
    print(queue)
