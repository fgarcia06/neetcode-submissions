class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rc_track = {}
        box_track = {}
    
        l = len(board)

        # check each row duplicates
        for i in range(l):
            for j in range(l):
                if board[i][j] == '.':
                    continue

                if board[i][j] in rc_track:
                    return False
                else:
                    rc_track[board[i][j]] = 1

            rc_track.clear()
        
        # check each column duplicates
        for i in range(l):
            for j in range(l):
                if board[j][i] == '.':
                    continue

                if board[j][i] in rc_track:
                    return False
                else:
                    rc_track[board[j][i]] = 1

            rc_track.clear()
        

        for i in range(l):
            for j in range(l):
                if board[i][j] == '.':
                    continue

                box = (i // 3, j // 3)

                if box not in box_track:
                    box_track[box] = set()

                if board[i][j] in box_track[box]:
                    return False

                box_track[box].add(board[i][j])
        
        return True