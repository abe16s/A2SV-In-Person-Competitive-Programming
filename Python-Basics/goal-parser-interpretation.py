class Solution:
    def interpret(self, command: str) -> str:
        cout = ""
        i = 0
        while i < len(command):
            if command[i] == "G":
                cout += "G"
                i += 1
            elif command[i+1] == ")":
                cout += "o"
                i += 2
            else:
                cout += "al"
                i += 4
        return cout