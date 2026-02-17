class TimeMap:

    def __init__(self):
        self.dicts = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dicts[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dicts:
            return ""
        res = self.dicts[key]
        
        l = 0
        n = len(res)
        r = n - 1
        ans = ""
        while l <= r:
            m = (l + r)//2
            
            if (res[m][0] <= timestamp):
                ans = res[m][1]
                #current <= timestamp AND next > timestamp
                l = m +1
                
            else:
                r = m -1
        return ans

        # return ""


        
        # if !
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)