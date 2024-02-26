class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        cout = []
        def backtrack(num, combination):
            if len(combination) == k:
                cout.append(combination[:])
                return
            if num > n:
                return
            
            backtrack(num+1, combination + [num])
            backtrack(num+1, combination)
        
        backtrack(1,[])
        return cout