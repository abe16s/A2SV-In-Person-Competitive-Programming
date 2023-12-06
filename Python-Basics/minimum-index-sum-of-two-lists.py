class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = set(list1).intersection(set(list2))
        index_sum = defaultdict(int)
        for idx,word in enumerate(list1):
            if word in common:
                index_sum[word] += idx
        for idx,word in enumerate(list2):
            if word in common:
                index_sum[word] += idx
        mini = min(index_sum.values())
        output = []
        for k in index_sum:
            if index_sum[k] == mini:
                output.append(k)
        return output