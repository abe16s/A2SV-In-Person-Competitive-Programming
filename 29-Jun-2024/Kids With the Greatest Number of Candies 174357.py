# Problem: Kids With the Greatest Number of Candies - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        cout = []
        for c in candies:
            if c + extraCandies < maxi:
                cout.append(False)
            else:
                cout.append(True)
        return cout