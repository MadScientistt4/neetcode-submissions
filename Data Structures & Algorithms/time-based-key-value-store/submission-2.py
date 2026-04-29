class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.keyStore:
            l, r = 0, len(self.keyStore[key])-1
            candidate = -1
            while l <= r:
                mid = (l+r)//2
                value, curtime = self.keyStore[key][mid]
                if curtime <= timestamp:
                    candidate = value
                    l = mid + 1
                else:
                    r = mid - 1
                
            return candidate if candidate != -1 else ""
        else:
            return ""
