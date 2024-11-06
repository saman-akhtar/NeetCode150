class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append((timestamp, value))
        # self.timeMap.get(key, []).append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        # print("self.timeMap:: ",self.timeMap)
        res = self.timeMap.get(key, "")
        # print("resu",res)
        if (res == "" or not res):
            return res
        if(len(res)  == 1 and res[0][0] <= timestamp):
            return res[0][1]
        l = 0
        r = len(res)-1
        result = ""#(res[0][0], res[0][1])
        while l <= r:
            m = (l + r) //2
            if( res[m][0] == timestamp ):
                # result = res[m][1]
                return res[m][1]
            # if( res[m][0] < timestamp and res[m][0] > result[0] ):
            #     result = (res[m][0],res[m][1])
            if timestamp > res[m][0]:
                result = res[m][1]
                l = m + 1

            else:
                
                r = m -1
        return result
            
        

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)