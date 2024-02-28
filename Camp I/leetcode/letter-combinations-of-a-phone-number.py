class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = []
        mapping = {
            2:"abc", 3: "def", 4: "ghi", 5: "jkl",
            6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"
        }
        def search(idx, cur):
            if idx == len(digits):
                if cur:
                    combinations.append(cur)
                return 
            for c in mapping[int(digits[idx])]:
                search(idx+1, cur+c)
        
        search(0, "")
        return combinations
            