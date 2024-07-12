# Problem: 2115. Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        indegree = defaultdict(int)
        needs = defaultdict(list)
        for i in range(len(recipes)):
            for ing in ingredients[i]:
                if ing not in supplies:
                    indegree[recipes[i]] += 1
                    needs[ing].append(recipes[i])
        cout = []
        queue = deque()
        for i in range(len(recipes)):
            if recipes[i] not in indegree:
                queue.append(recipes[i])
        while queue:
            for i in range(len(queue)):
                cur = queue.popleft()
                cout.append(cur)
                for nbr in needs[cur]:
                    indegree[nbr] -= 1
                    if indegree[nbr] == 0:
                        queue.append(nbr)

        return cout