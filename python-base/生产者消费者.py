import threading
import queue
import time
import random

# 共享的缓冲区（队列）作为生产者和消费者之间的中介，允许它们异步工作。生产者不需要等待消费者处理完，消费者也不需要等待生产者生成。
# 队列可以作为缓冲区，平衡生产者和消费者的速度差异，避免任务丢失。
# 设置最大容量为 5，就像一个最多只能放 5 个面包的货架
shared_queue = queue.Queue(maxsize=5)

# 特殊的结束信号，告诉消费者没有更多任务了
SENTINEL = None # 哨兵

class Producer(threading.Thread):
    """
    生产者线程：负责生成数据或任务，并将其放入一个共享的缓冲区（队列）
    就像面包师，不停地烤面包放到货架上
    """
    def __init__(self, queue, name="Producer", items_to_produce=10): # items_to_produce:要生产的总物品数量
        super().__init__(name=name)
        self.queue = queue
        self.items_to_produce = items_to_produce

    def run(self):
        print(f"{self.name}: 开始生产...")
        for i in range(self.items_to_produce):
            item = f"产品-{i}"
            # 模拟生产需要时间
            time.sleep(random.uniform(0.1, 0.5))
            print(f"{self.name}: 生产了 -> {item}")
            # 将产品放入队列，如果队列满了，put() 会阻塞等待
            self.queue.put(item)
            print(f"{self.name}: 放入队列 <- {item} (队列大小: {self.queue.qsize()})")
        print(f"{self.name}: 生产结束。")
        # 注意：这里不直接放 SENTINEL，由主线程统一放置

class Consumer(threading.Thread):
    """
    消费者线程：从共享缓冲区中获取数据或任务，并进行处理。
    就像顾客，从货架上拿面包吃,模拟从队列中取出物品并消费
    """
    def __init__(self, queue, name="Consumer"):
        super().__init__(name=name)
        self.queue = queue

    def run(self):
        print(f"{self.name}: 开始消费...")
        while True:
            # get:从队列中取出产品，如果队列空了，get() 会阻塞等待
            item = self.queue.get()
            if item is SENTINEL:
                # 如果收到结束信号，就告诉队列这个任务完成了，然后退出
                print(f"{self.name}: 收到结束信号，停止消费。")
                self.queue.task_done() # task_done：消费者从队列中取出一个任务后，当队列为空时，会唤醒调用 join() 的线程。相当于java中的notify()
                break
            else:
                # 模拟消费需要时间
                print(f"{self.name}: 拿到队列 -> {item} (队列大小: {self.queue.qsize()})")
                consume_time = random.uniform(0.2, 1.0)
                print(f"{self.name}: 正在消费 {item} (预计 {consume_time:.2f} 秒)...")
                time.sleep(consume_time)
                print(f"{self.name}: 消费完成 <- {item}")
                # 告诉队列这个任务处理完了
                self.queue.task_done()
        print(f"{self.name}: 消费结束。")

if __name__ == "__main__":
    # 设置要生产的总物品数量
    total_items = 15
    # 设置消费者数量
    num_consumers = 3

    # 创建一个生产者线程
    producer = Producer(shared_queue, items_to_produce=total_items)

    # 创建多个消费者线程
    consumers = []
    for i in range(num_consumers):
        consumer = Consumer(shared_queue, name=f"Consumer-{i+1}")
        consumers.append(consumer)

    # 启动生产者线程
    producer.start()

    # 启动所有消费者线程
    for consumer in consumers:
        consumer.start()

    # 等待生产者完成所有生产任务
    producer.join()
    print("主线程：生产者已经完成生产。")

    # 生产者完成后，向队列中放入相应数量的结束信号，确保每个消费者都能收到
    print(f"主线程：向队列放入 {num_consumers} 个结束信号...")
    for _ in range(num_consumers):
        shared_queue.put(SENTINEL) # put:入队，如果队列已满，put() 会阻塞等待

    # 等待队列中的所有任务都被处理完毕
    # join() 会阻塞，直到队列中所有放入的 item 都被 get() 并且其 task_done() 被调用
    print("主线程：等待队列为空...")
    shared_queue.join() # join:若队列不为空，join() 会阻塞等待，直到队列为空
    print("主线程：队列中的所有任务已被处理完毕。")

    # 等待所有消费者线程结束（虽然 join() 保证任务完成，但等待线程退出是好习惯）
    # for consumer in consumers:
    #     consumer.join()
    # print("主线程：所有消费者线程已结束。") # 这行通常不需要，因为 queue.join() 已经确保消费者处理完并收到 SENTINEL

    print("主线程：程序结束。")
