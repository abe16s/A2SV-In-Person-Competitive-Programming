class Robot:

    def __init__(self, width: int, height: int):
        self.width = width - 1
        self.height = height - 1  
        self.dim = self.width + self.height
        self.pos = [0,0]    
        self.oneDimension = 0
        self.moves = 0

    def step(self, num: int) -> None:
        self.moves += 1
        self.oneDimension = (self.oneDimension + num) % (2*self.dim)
        if self.oneDimension // self.width == 0:
            self.pos[0] = self.oneDimension
            self.pos[1] = 0 
        elif self.oneDimension // self.dim == 0:
            self.pos[1] = self.oneDimension - self.width
            self.pos[0] = self.width
        elif self.oneDimension // (self.dim + self.width) == 0:
            self.pos[1] = self.height
            self.pos[0] = self.width - self.oneDimension + self.dim 
        else:
            self.pos[0] = 0
            self.pos[1] = self.dim * 2 - self.oneDimension 

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        if self.moves == 0:
            return "East"
        if self.pos[1] == 0 and self.pos[0] > 0:
            return "East"
        if self.pos[0] == self.width:
            return "North"
        if self.pos[1] == self.height:
            return "West"
        if self.pos[0] == 0:
            return "South"
        
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()