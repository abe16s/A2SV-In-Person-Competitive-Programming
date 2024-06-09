# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count/description/

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        output = defaultdict(int)
        for i in range(len(cpdomains)):
            current = cpdomains[i].split(" ")
            domains = current[1].split(".")
            for j in range(len(domains)-1,-1,-1):
                output[".".join(domains[j:])] += int(current[0])
        return [str(output[key]) + " " + key for key in output]