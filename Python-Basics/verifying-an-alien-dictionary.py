class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        c = {}
        for i,j in enumerate(order):
            c[j] = i
        
        def check(w1, w2):
            i = min(len(w1), len(w2))
            for _ in range(i):
                print(w1, w2, _)
                if c[w1[_]] > c[w2[_]]:
                    return False
                elif c[w1[_]] < c[w2[_]]:
                    return True
            return len(w1) <= len(w2)
        for i in range(len(words)-1):
            if not check(words[i], words[i+1]):
                return False
        return True
        
        