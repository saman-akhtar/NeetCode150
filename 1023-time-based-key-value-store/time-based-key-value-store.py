class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        res = self.timeMap.get(key, "")
        if (res == "" or not res):
            return res
        if(len(res)  == 1 and res[0][0] <= timestamp):
            return res[0][1]
        l = 0
        r = len(res)-1
        result = ""
        while l <= r:
            m = (l + r) //2
            if( res[m][0] == timestamp ):
                return res[m][1]
            if timestamp > res[m][0]:
                #more we move right , more max close value to timestam be assigned
                result = res[m][1]
                l = m + 1
            else:
                r = m -1
        return result
            
        

# TC 1) O(1) 2). O(1) 3) Ologn
# SC      O(n)  


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)