class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters) - 1
        while l <= r:
            mid = l + (r-l)//2
            if letters[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return letters[r+1] if r+1 < len(letters) else letters[0]