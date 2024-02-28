class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        cout = []
        def search(cur, cur_sum, idx):
            if cur_sum == n and len(cur) == k:
                cout.append(cur[:])
                return True
            if cur_sum > n or len(cur) >= k:
                return 
            
            for i in range(idx, 10):
                cur.append(i)
                search(cur, cur_sum+i, i+1)
                cur.pop()

        search([], 0, 1)
        return cout

        