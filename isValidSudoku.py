class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        for i in range(len(board)):
            row_dict = dict()
            for j in range(len(board[0])):
                if board[i][j] in row_dict.keys():
                    return False
                else: 
                    row_dict[board[i][j]] = 1
                

        for i in range(len(board)):
            col_dict = dict()
            for j in range(len(board[0])):
                if board[i][j] in col_dict.keys():
                    return False
                else: 
                    col_dict[board[j][i]] = 1
                                
        # 3x3 dolasmayi da ekle
        for i in range(len(board)):
            col_dict = dict()
            for j in range(len(board[0])):
                if board[i][j] in col_dict.keys():
                    return False
                else: 
                    col_dict[board[j][i]] = 1
                                