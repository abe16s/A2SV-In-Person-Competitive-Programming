class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        operators = ['+','-','*','/']
        for i in range(len(tokens)):
            oper = True
            for j in range(4):
                if operators[j] == tokens[i]:
                    o2 = operands.pop()
                    o1 = operands.pop()
                    if j == 0:
                        result = o1 + o2
                    elif j == 1:
                        result = o1 - o2
                    elif j == 2:
                        result = o1 * o2
                    else:
                        result = o1 // o2
                        if result < 0 and result != o1/o2:
                            result += 1
                    operands.append(result)
                    oper = False
                    break
            if oper: operands.append(int(tokens[i]))

        return operands[0]
            
                
