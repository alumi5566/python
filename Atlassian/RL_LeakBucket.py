from time import time, sleep
""""
Picture a bucket in your mind.
Fill the buckets with tokens at a constant rate.
When a packet arrives, check if there is any token in the bucket.
If there was any token left, remove one from the bucket and forward the packet. If the bucket was empty, simply drop the packet.
"""
class LeakBucket:

    def __init__(self, maxBucket, time_unit, forward_callback, drop_callback):
        # time_unit: the tokens are added in this time frame.
        self.time_unit = time_unit
        self.forward_callback = forward_callback
        self.drop_callback = drop_callback
        # maxBucket the size of the bucket
        self.maxBucket = maxBucket
        self.stack = []
        # last_check is the timestamp that we previously handled a packet.
        self.last_check = int(time())

    def handle(self, packet):
        # if current time is in the next time frame, reset and allow max capacity to process
        if int(time()) >= self.last_check + self.time_unit:
            while len(self.stack) > 0:
                self.forward_callback(self.stack[0])
                self.stack.pop(0)
            self.last_check = int(time())
            # self.allowance = self.capacity

        if (len(self.stack) >= self.maxBucket):
            return self.drop_callback(packet)

        self.stack.append(packet)
        return
        # return self.forward_callback(packet)


def forward(packet):
    print("Packet Forwarded: " + str(packet))


def drop(packet):
    print("Packet Dropped: " + str(packet))

# def __init__(self, init_token, maxBucket, time_unit, forward_callback, drop_callback):
throttle = LeakBucket(1, 1, forward, drop)

packet = 0

while True:
    sleep(0.2)
    throttle.handle(packet)
    packet += 1