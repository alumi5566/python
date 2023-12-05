import time
""""
Picture a bucket in your mind.
Fill the buckets with tokens at a constant rate.
When a packet arrives, check if there is any token in the bucket.
If there was any token left, remove one from the bucket and forward the packet. If the bucket was empty, simply drop the packet.
"""
class TokenBucket:

    def __init__(self, init_token, maxBucket, time_unit, forward_callback, drop_callback):
        # tokens: number of current available token
        self.tokens = init_token
        # time_unit: the tokens are added in this time frame.
        self.time_unit = time_unit
        self.forward_callback = forward_callback
        self.drop_callback = drop_callback
        # maxBucket the size of the bucket
        self.maxBucket = maxBucket
        # last_check is the timestamp that we previously handled a packet.
        self.last_check = time.time()

    def handle(self, packet):
        current = time.time()
        time_passed = current - self.last_check
        self.last_check = current

        self.tokens = self.tokens + time_passed * self.time_unit

        if (self.tokens > self.maxBucket):
            self.tokens = self.maxBucket

        if (self.tokens < 1):
            self.drop_callback(packet)
        else:
            self.tokens = self.tokens - 1
            self.forward_callback(packet)


def forward(packet):
    print("Packet Forwarded: " + str(packet))


def drop(packet):
    print("Packet Dropped: " + str(packet))

# def __init__(self, init_token, maxBucket, time_unit, forward_callback, drop_callback):
throttle = TokenBucket(1, 1, 1, forward, drop)

packet = 0

while True:
    time.sleep(0.2)
    throttle.handle(packet)
    packet += 1