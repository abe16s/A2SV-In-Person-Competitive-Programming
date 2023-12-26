class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(names)):
            maxi_idx = i    
            for j in range(i, len(names)):
                if heights[j] > heights[maxi_idx]:
                    maxi_idx = j
            heights[maxi_idx], heights[i] = heights[i], heights[maxi_idx]
            names[maxi_idx], names[i] = names[i], names[maxi_idx]
            
        return names