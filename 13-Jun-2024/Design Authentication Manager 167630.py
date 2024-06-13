# Problem: Design Authentication Manager - https://leetcode.com/problems/design-authentication-manager/

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.timeExpires = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.timeExpires[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.timeExpires and self.timeExpires[tokenId] > currentTime:
            self.timeExpires[tokenId] = currentTime + self.timeToLive
            
    def countUnexpiredTokens(self, currentTime: int) -> int:
        ctr = 0
        for k, v in self.timeExpires.items():
            if v > currentTime:
                ctr += 1
        return ctr


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)