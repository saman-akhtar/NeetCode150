class Logger:

    def __init__(self):
        self.msg = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if(message in self.msg):
            if timestamp >= self.msg[message]:
                 self.msg[message]= timestamp + 10
                 return True
            else:
                return False
        else:
            self.msg[message]= timestamp + 10
            return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)