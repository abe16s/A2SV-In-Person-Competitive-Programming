class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        maxi = 0
        k = 0
        for i in range(len(processorTime)):
            for j in range(4):
                print(processorTime[i], tasks[k])
                maxi = max(maxi, processorTime[i] + tasks[k])
                k += 1
        return maxi