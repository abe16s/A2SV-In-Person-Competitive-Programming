class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits)<=2:
            return len(fruits)
        count = defaultdict(int)
        start = 0
        end = 0
        maxi = 0
        while end < len(fruits):
            if len(count) == 2 and fruits[end] not in count:
                maxi = max(maxi, end-start)
                while 0 not in count.values():
                    count[fruits[start]] -= 1
                    start += 1
                for k in count:
                    if count[k] == 0:
                        count.pop(k)
                        break

            count[fruits[end]] += 1
            end += 1
        
        maxi = max(maxi, end-start)

        return maxi
