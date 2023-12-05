class Logger(object):
    # logRecord = {}
    def __init__(self):
        self.logRecord = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        print("msg: ", message, " t: ", timestamp)
        print(self.logRecord)
        if message not in self.logRecord.keys():
            print("not in")
            self.logRecord[message] = timestamp
            return True
        else:
            print("in")
            previousTime = self.logRecord[message]
            if timestamp >= previousTime + 10:
                self.logRecord[message] = timestamp
                return True
            else:
                return False

logger = Logger();
print(logger.shouldPrintMessage(1, "foo"))  # return true, next allowed timestamp for "foo" is 1 + 10 = 11
print(logger.shouldPrintMessage(2, "bar"))  # return true, next allowed timestamp for "bar" is 2 + 10 = 12
print(logger.shouldPrintMessage(3, "foo"))  # 3 < 11, return false
print(logger.shouldPrintMessage(8, "bar"))  # 8 < 12, return false
print(logger.shouldPrintMessage(10, "foo")) # 10 < 11, return false
print(logger.shouldPrintMessage(11, "foo")) # 11 >= 11, return true, next allowed timestamp for "foo" is 11 + 10 = 21