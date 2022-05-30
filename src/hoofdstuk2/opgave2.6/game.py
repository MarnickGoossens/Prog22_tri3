from random import choice


class Game:
    """Game loop of Minesweeper (already completed)"""

    def game_loop(self):
        self.board.display_mines_grid()
        self.board.display_neighbouring_mines_grid()

        game_end = None
        while True:
            self.board.display_play_grid()
            game_end = self.make_move()
            if game_end == True:
                print(f"Congrats you won!")
                break
            if game_end == False:
                print(f"Bomb exploded!!!!")
                self.board.display_mines()
                break


class Board:
    def __init__(self, CHAR_MINE="*", CHAR_BLANK="?", SQUARE_SIZE=9, MINE_NUMBER=9):
        self.CHAR_MINE = CHAR_MINE
        self.CHAR_BLANK = CHAR_BLANK
        self.SQUARE_SIZE = SQUARE_SIZE
        self.covered_cells = self.SQUARE_SIZE**2 - MINE_NUMBER
        self.grid = []

        for row in range(SQUARE_SIZE):
            self.grid.append([Cell(CHAR_BLANK)] * SQUARE_SIZE)

    def generate_mines(self, mine_number):
        for i in range(10):
            row = choice(self.grid)
            cell = choice(row)
            teken = cell.display_character
            while teken == "*":
                row = choice(self.grid)
                cell = choice(row)
                teken = cell.display_character
            cell.display_character = "*"

    def calculate_neighbouring_mines(self):
        pass


class Cell:
    def __init__(self, display_character):
        self.is_revealed = False
        self.display_character = display_character
        neighbouring_mine_count = 0

    def __repr__(self):
        return self.display_character


"""
This will be executed when running the game.py file

Game settings, to be passed on to Board through Game.
    CHAR_MINE: Character to be used when displaying mines (default *)
    CHAR_BLANK: Character to be used when displaying blanks (default ?)
    SQUARE_SIZE: The width and height of the minesweeper square (default 9)
    MINE_NUMBER: THe amount of mines in the square (default 9)

When leaving Game() empty, the default values listed above should be used.
"""
if __name__ == "__main__":
    game = Game()
    game.game_loop()
