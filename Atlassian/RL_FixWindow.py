from time import time, sleep


class FixedWindow:

    def __init__(self, capacity, time_unit, forward_callback, drop_callback):
        self.current_time = int(time())
        # print(self.current_time)
        self.allowance = capacity
        # capacity: number of the allowed packets that can pass through in a second.
        self.capacity = capacity

        self.time_unit = time_unit
        self.forward_callback = forward_callback
        self.drop_callback = drop_callback

    def handle(self, packet):
        # if current time is in the next time frame, reset and allow max capacity to process
        if int(time()) >= self.current_time + self.time_unit:
            self.current_time = int(time())
            self.allowance = self.capacity

        if (self.allowance < 1):
            return self.drop_callback(packet)

        self.allowance -= 1
        return self.forward_callback(packet)


def forward(packet):
    print("Packet Forwarded: " + str(packet))


def drop(packet):
    print("Packet Dropped: " + str(packet))

# def __init__(self, capacity, time_unit, forward_callback, drop_callback):
throttle = FixedWindow(1, 1, forward, drop)

packet = 0

while True:
    sleep(0.2)
    throttle.handle(packet)
    packet += 1