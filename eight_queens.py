from itertools import permutations  

# A Chessboard is made up of 
#    columns (called "files" that are letters from a to g) and 
#    row (called "ranks" that are numbers from 1 to 8). Therefore,
#    if a chess piece is said to be in "e4",
#    then it is in the "e file" (5th column) and "4th rank" (4th column)
class Queen:
    def __init__(self, position):
        self.position = position
        self.file = position[0]
        self.rank = int(position[1])
    
    
    # --------------------------------------------------------
    # Static methods to get the next/previous files and ranks
    @staticmethod
    def next_files(file):
        files = []
        while(file != 'h'):
            file = chr(ord(file) + 1)
            files.append(file)
        return files
    
    @staticmethod
    def prev_files(file):
        files = []
        while(file != 'a'):
            file = chr(ord(file) - 1)
            files.append(file)
        return files
    
    @staticmethod
    def next_ranks(rank):
        ranks = []
        while(rank != 8):
            rank = rank + 1
            ranks.append(rank)
        return ranks
    
    @staticmethod
    def prev_ranks(rank):
        ranks = []
        while(rank != 1):
            rank = rank - 1
            ranks.append(rank)
        return ranks
    # --------------------------------------------------------
    
    
    # --------------------------------------------------------
    # Class Methods to check intersections in the file, rank, and both diagonals
    
    # Check for two queens in the same position
    @classmethod
    def same_position(cls, queen1, queen2):
        return queen1.position == queen2.position
    
    # Check for intersections in the file "|"
    @classmethod
    def same_file(cls, queen1, queen2):
        return queen1.file == queen2.file
    
    # Check for intersections in the rank "—"
    @classmethod
    def same_rank(cls, queen1, queen2):
        return queen1.rank == queen2.rank
    
    # Check for intersections in the rising diagonal "⟋"
    @classmethod
    def same_rising_diagonal(cls, queen1, queen2):
        next_files = Queen.next_files(queen1.file)
        prev_files = Queen.prev_files(queen1.file)
        next_ranks = Queen.next_ranks(queen1.rank)
        prev_ranks = Queen.prev_ranks(queen1.rank)
        
        prev_squares = [
            prev_files[i]+str(prev_ranks[i])
            for i in range(min(len(prev_files), len(prev_ranks)))
        ]
        
        next_squares = [
            next_files[i]+str(next_ranks[i])
            for i in range(min(len(next_files), len(next_ranks)))
        ]
        
        rising_diagonal_squares = prev_squares + next_squares
        return queen2.position in rising_diagonal_squares
    
    # Check for intersections in the falling diagonal "⟍"
    @classmethod
    def same_falling_diagonal(cls, queen1, queen2):
        next_files = Queen.next_files(queen1.file)
        prev_files = Queen.prev_files(queen1.file)
        next_ranks = Queen.next_ranks(queen1.rank)
        prev_ranks = Queen.prev_ranks(queen1.rank)
        
        prev_squares = [
            prev_files[i]+str(next_ranks[i])
            for i in range(min(len(prev_files), len(next_ranks)))
        ]
        
        next_squares = [
            next_files[i]+str(prev_ranks[i])
            for i in range(min(len(next_files), len(prev_ranks)))
        ]
        
        rising_diagonal_squares = prev_squares + next_squares
        return queen2.position in rising_diagonal_squares
    # --------------------------------------------------------
    
    # --------------------------------------------------------
    # Check for intersections in the file, rank, and both diagonals
    @classmethod
    def intersects_with(cls, queen1, queen2):
        return Queen.same_position(queen1, queen2) or Queen.same_rank(queen1, queen2) or Queen.same_file(queen1, queen2) or Queen.same_rising_diagonal(queen1, queen2) or Queen.same_falling_diagonal(queen1, queen2)
    
    # Given a list of queens, figure out whether it would be a solution
    # to the n-queens problem
    @classmethod
    def is_a_solution(cls, queens):
        bools = []
        for q1 in queens:
            for q2 in queens:
                if q1.position != q2.position:
                    bools.append(Queen.intersects_with(q1,q2))
        
        is_a_solution = True
        for b in bools:
            is_a_solution = is_a_solution and not b
            
        return is_a_solution

queens = [Queen('a2'), Queen('b4'), Queen('c6'), Queen('d8'), Queen('e3'), Queen('f1'), Queen('g7'), Queen('h5')]
print(Queen.is_a_solution(queens))



