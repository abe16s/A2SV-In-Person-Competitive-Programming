class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contents = defaultdict(list)
        for path in paths:
            current = path.split(" ")
            for i in range(1, len(current)):
                start = current[i].find("(")
                end = current[i].find(")", start)
                contents[current[i][start:end]].append(current[0]+"/"+current[i][:start])
        return [v for v in contents.values() if len(v) > 1]