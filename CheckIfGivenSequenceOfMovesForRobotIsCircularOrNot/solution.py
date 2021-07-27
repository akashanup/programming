class Solution:
    def isCircularMove(self, moves):
        x, y = 0, 0
        head = 1
        '''
            1: up
            2: down
            3: right
            4: left
        '''
        for move in moves:
            if move == "G":
                if head == 1:
                    y += 1
                elif head == 2:
                    y -= 1
                elif head == 3:
                    x += 1
                else:
                    x -= 1
            elif move == "R":
                if head == 1:
                    head = 3
                elif head == 2:
                    head = 4
                elif head == 3:
                    head = 2
                else:
                    head = 1
            else:
                if head == 1:
                    head = 4
                elif head == 2:
                    head = 3
                elif head == 3:
                    head = 1
                else:
                    head = 2
            print(x, y)
        return x == 0 and y == 0
