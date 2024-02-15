import random

class PacmanGame:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.pacman_pos = [0, 0]
        self.ghost_pos = [rows - 1, cols - 1]
        self.dot_pos = [random.randint(0, rows - 1), random.randint(0, cols - 1)]

    def print_board(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if [i, j] == self.pacman_pos:
                    print('P', end=' ')
                elif [i, j] == self.ghost_pos:
                    print('G', end=' ')
                elif [i, j] == self.dot_pos:
                    print('.', end=' ')
                else:
                    print(self.board[i][j], end=' ')
            print()

    def move_pacman(self, direction):
        if direction == 'up' and self.pacman_pos[0] > 0:
            self.pacman_pos[0] -= 1
        elif direction == 'down' and self.pacman_pos[0] < self.rows - 1:
            self.pacman_pos[0] += 1
        elif direction == 'left' and self.pacman_pos[1] > 0:
            self.pacman_pos[1] -= 1
        elif direction == 'right' and self.pacman_pos[1] < self.cols - 1:
            self.pacman_pos[1] += 1

    def check_collision(self):
        if self.pacman_pos == self.ghost_pos:
            return True
        elif self.pacman_pos == self.dot_pos:
            self.dot_pos = [random.randint(0, self.rows - 1), random.randint(0, self.cols - 1)]
        return False


def main():
    rows, cols = 5, 5
    game = PacmanGame(rows, cols)

    while True:
        game.print_board()
        direction = input("Enter direction (up/down/left/right): ").lower()

        if direction in ['up', 'down', 'left', 'right']:
            game.move_pacman(direction)
            if game.check_collision():
                print("Game Over! Pacman collided with the ghost.")
                break
        else:
            print("Invalid direction. Please enter a valid direction.")

if __name__ == "__main__":
    main()
