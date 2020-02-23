import math
import random


class MrsRescueBot:

    def print_field(self, field):
        # Print the playing field
        print('Mrs Bot = M')
        print('Mr Bot = O')
        print("This is what the playing field looks like \n(if only 'M' is visible, then Mrs Bot already found Mr Bot!):")
        for f in field:
            print(f)

    def generate_positions(self, x, y):
        # Randomly generate Bot positions
        m_x = random.randint(0, x-1)
        m_y = random.randint(0, y-1)
        o_x = random.randint(0, x-1)
        o_y = random.randint(0, y-1)
        return [m_x, m_y], [o_x, o_y]

    def place_bots_in_field(self, field, m, o):
        # Set the positions of the Bots
        Y = field[o[1]]
        a = Y[:]
        a[o[0]] = 'O'
        field[o[1]] = a

        Y = field[m[1]]
        b = Y[:]
        b[m[0]] = 'M'
        field[m[1]] = b

        return field

    def get_field_dimensions(self):
        # Get the x * y dimensions for the field and randomly places places Mr and Mrs Bot within

        print('Input field size: X direction - Choose a number less than 50:')
        x = input()
        print('Input field size - Y direction - Choose a number less than 50:')
        y = input()

        x_direction = ['_'] * x
        field = [x_direction] * y

        return x, y, field

    def _distance(self, mrs, mr):
        # Calculates straight line distance between Mrs Rescue Bot and Mr Bot
        dx = mrs[0] - mr[0]
        dy = mrs[1] - mr[1]
        return math.sqrt(dx ** 2 + dy ** 2)

    def _explore_options(self, m, o):
        # Explores the environment and returns the best move to save Mr Bot

        down = [m[0], m[1] + 1]
        left = [m[0] - 1, m[1]]
        right = [m[0] + 1, m[1]]
        up = [m[0], m[1] - 1]

        moves = {'LEFT': self._distance(left, o),
                 'UP': self._distance(up, o),
                 'RIGHT': self._distance(right, o),
                 'DOWN': self._distance(down, o)}

        best_move = min(moves, key=moves.get)

        if best_move == 'LEFT':
            return left, best_move
        elif best_move == 'UP':
            return up, best_move
        elif best_move == 'RIGHT':
            return right, best_move
        else:
            return down, best_move

    def save_mr_bot(self, m, o):
        # Execute Save Mr Bot

        moves = []
        for _ in range(10000):
            m, n = self._explore_options(m, o)
            moves.append(n)
            if m[0] == o[0] and m[1] == o[1]:
                break
            else:
                pass

        print('\nDirections for Mrs Bot to find Mr Bot:')
        return '\n'.join(moves)


if __name__ == '__main__':

    mrb = MrsRescueBot()

    x, y, field = mrb.get_field_dimensions()
    m, o = mrb.generate_positions(x, y)
    field = mrb.place_bots_in_field(field, m, o)
    mrb.print_field(field)
    moves = mrb.save_mr_bot(m, o)
    print(moves)
