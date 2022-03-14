class Cube:
    def __init__(self, initial_state=None):
        self.move_count = 0
        if initial_state:
            self.wall_U = initial_state[0]
            self.wall_L = initial_state[1]
            self.wall_F = initial_state[2]
            self.wall_R = initial_state[3]
            self.wall_B = initial_state[4]
            self.wall_D = initial_state[5]
        else:
            self.wall_U = [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']]
            self.wall_L = [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]
            self.wall_F = [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']]
            self.wall_R = [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']]
            self.wall_B = [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']]
            self.wall_D = [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']]
        self.history = ''

    def __eq__(self, other):
        if self.wall_U == other.wall_U and \
            self.wall_D == other.wall_D and \
            self.wall_R == other.wall_R and \
            self.wall_L == other.wall_L and \
            self.wall_F == other.wall_F and \
            self.wall_B == other.wall_B:
            return True
        else:
            return False


    def print(self):
        print('\t{}{}{}'.format(self.wall_U[0][0], self.wall_U[0][1], self.wall_U[0][2]))
        print('\t{}{}{}'.format(self.wall_U[1][0], self.wall_U[1][1], self.wall_U[1][2]))
        print('\t{}{}{}'.format(self.wall_U[2][0], self.wall_U[2][1], self.wall_U[2][2]))
        print('{}{}{} {}{}{} {}{}{} {}{}{}'.format(self.wall_L[0][0], self.wall_L[0][1], self.wall_L[0][2],
                                                   self.wall_F[0][0], self.wall_F[0][1], self.wall_F[0][2],
                                                   self.wall_R[0][0], self.wall_R[0][1], self.wall_R[0][2],
                                                   self.wall_B[0][0], self.wall_B[0][1], self.wall_B[0][2]))
        print('{}{}{} {}{}{} {}{}{} {}{}{}'.format(self.wall_L[1][0], self.wall_L[1][1], self.wall_L[1][2],
                                                   self.wall_F[1][0], self.wall_F[1][1], self.wall_F[1][2],
                                                   self.wall_R[1][0], self.wall_R[1][1], self.wall_R[1][2],
                                                   self.wall_B[1][0], self.wall_B[1][1], self.wall_B[1][2]))
        print('{}{}{} {}{}{} {}{}{} {}{}{}'.format(self.wall_L[2][0], self.wall_L[2][1], self.wall_L[2][2],
                                                   self.wall_F[2][0], self.wall_F[2][1], self.wall_F[2][2],
                                                   self.wall_R[2][0], self.wall_R[2][1], self.wall_R[2][2],
                                                   self.wall_B[2][0], self.wall_B[2][1], self.wall_B[2][2]))
        print('\t{}{}{}'.format(self.wall_D[0][0], self.wall_D[0][1], self.wall_D[0][2]))
        print('\t{}{}{}'.format(self.wall_D[1][0], self.wall_D[1][1], self.wall_D[1][2]))
        print('\t{}{}{}'.format(self.wall_D[2][0], self.wall_D[2][1], self.wall_D[2][2]))

    def move(self, moves, save_to_history=True):
        while moves != '':
            is_reverse = False
            is_double = False
            if len(moves) >= 2:
                if moves[1] == "'":
                    is_reverse = True
                elif moves[1] == "2":
                    is_double = True
            if moves[0] == 'R':
                if is_reverse:
                    self.wall_D[0][2], self.wall_D[1][2], self.wall_D[2][2], \
                        self.wall_B[2][0], self.wall_B[1][0], self.wall_B[0][0], \
                        self.wall_U[0][2], self.wall_U[1][2], self.wall_U[2][2], \
                        self.wall_F[0][2], self.wall_F[1][2], self.wall_F[2][2] \
                        = self.wall_F[0][2], self.wall_F[1][2], self.wall_F[2][2], \
                        self.wall_D[0][2], self.wall_D[1][2], self.wall_D[2][2], \
                        self.wall_B[2][0], self.wall_B[1][0], self.wall_B[0][0], \
                        self.wall_U[0][2], self.wall_U[1][2], self.wall_U[2][2]
                    self.wall_R[2][0], self.wall_R[2][2], self.wall_R[0][2], self.wall_R[0][0] = \
                        self.wall_R[0][0], self.wall_R[2][0], self.wall_R[2][2], self.wall_R[0][2]
                    self.wall_R[1][0], self.wall_R[0][1], self.wall_R[1][2], self.wall_R[2][1] = \
                        self.wall_R[0][1], self.wall_R[1][2], self.wall_R[2][1], self.wall_R[1][0]
                elif is_double:
                    self.wall_D[0][2], self.wall_D[1][2], self.wall_D[2][2], \
                        self.wall_B[2][0], self.wall_B[1][0], self.wall_B[0][0], \
                        self.wall_U[0][2], self.wall_U[1][2], self.wall_U[2][2], \
                        self.wall_F[0][2], self.wall_F[1][2], self.wall_F[2][2] \
                        = self.wall_U[0][2], self.wall_U[1][2], self.wall_U[2][2], \
                        self.wall_F[0][2], self.wall_F[1][2], self.wall_F[2][2], \
                        self.wall_D[0][2], self.wall_D[1][2], self.wall_D[2][2], \
                        self.wall_B[2][0], self.wall_B[1][0], self.wall_B[0][0]
                    self.wall_R[2][0], self.wall_R[2][2], self.wall_R[0][2], self.wall_R[0][0] = \
                        self.wall_R[0][2], self.wall_R[0][0], self.wall_R[2][0], self.wall_R[2][2]
                    self.wall_R[1][0], self.wall_R[0][1], self.wall_R[1][2], self.wall_R[2][1] = \
                        self.wall_R[1][2], self.wall_R[2][1], self.wall_R[1][0], self.wall_R[0][1]
                else:
                    self.wall_F[0][2], self.wall_F[1][2], self.wall_F[2][2], \
                        self.wall_D[0][2], self.wall_D[1][2], self.wall_D[2][2], \
                        self.wall_B[2][0], self.wall_B[1][0], self.wall_B[0][0], \
                        self.wall_U[0][2], self.wall_U[1][2], self.wall_U[2][2] \
                        = self.wall_D[0][2], self.wall_D[1][2], self.wall_D[2][2], \
                        self.wall_B[2][0], self.wall_B[1][0], self.wall_B[0][0], \
                        self.wall_U[0][2], self.wall_U[1][2], self.wall_U[2][2], \
                        self.wall_F[0][2], self.wall_F[1][2], self.wall_F[2][2]
                    self.wall_R[0][0], self.wall_R[2][0], self.wall_R[2][2], self.wall_R[0][2] = \
                        self.wall_R[2][0], self.wall_R[2][2], self.wall_R[0][2], self.wall_R[0][0]
                    self.wall_R[0][1], self.wall_R[1][2], self.wall_R[2][1], self.wall_R[1][0] = \
                        self.wall_R[1][0], self.wall_R[0][1], self.wall_R[1][2], self.wall_R[2][1]
            elif moves[0] == 'U':
                if is_reverse:
                    self.wall_R[0][0], self.wall_R[0][1], self.wall_R[0][2], \
                        self.wall_B[0][0], self.wall_B[0][1], self.wall_B[0][2], \
                        self.wall_L[0][0], self.wall_L[0][1], self.wall_L[0][2], \
                        self.wall_F[0][0], self.wall_F[0][1], self.wall_F[0][2] \
                        = self.wall_F[0][0], self.wall_F[0][1], self.wall_F[0][2], \
                        self.wall_R[0][0], self.wall_R[0][1], self.wall_R[0][2], \
                        self.wall_B[0][0], self.wall_B[0][1], self.wall_B[0][2], \
                        self.wall_L[0][0], self.wall_L[0][1], self.wall_L[0][2]
                    self.wall_U[2][0], self.wall_U[2][2], self.wall_U[0][2], self.wall_U[0][0] = \
                        self.wall_U[0][0], self.wall_U[2][0], self.wall_U[2][2], self.wall_U[0][2]
                    self.wall_U[1][0], self.wall_U[0][1], self.wall_U[1][2], self.wall_U[2][1] = \
                        self.wall_U[0][1], self.wall_U[1][2], self.wall_U[2][1], self.wall_U[1][0]
                elif is_double:
                    self.wall_R[0][0], self.wall_R[0][1], self.wall_R[0][2], \
                        self.wall_B[0][0], self.wall_B[0][1], self.wall_B[0][2], \
                        self.wall_L[0][0], self.wall_L[0][1], self.wall_L[0][2], \
                        self.wall_F[0][0], self.wall_F[0][1], self.wall_F[0][2] \
                        = self.wall_L[0][0], self.wall_L[0][1], self.wall_L[0][2], \
                        self.wall_F[0][0], self.wall_F[0][1], self.wall_F[0][2], \
                        self.wall_R[0][0], self.wall_R[0][1], self.wall_R[0][2], \
                        self.wall_B[0][0], self.wall_B[0][1], self.wall_B[0][2]
                    self.wall_U[2][0], self.wall_U[2][2], self.wall_U[0][2], self.wall_U[0][0] = \
                        self.wall_U[0][2], self.wall_U[0][0], self.wall_U[2][0], self.wall_U[2][2]
                    self.wall_U[1][0], self.wall_U[0][1], self.wall_U[1][2], self.wall_U[2][1] = \
                        self.wall_U[1][2], self.wall_U[2][1], self.wall_U[1][0], self.wall_U[0][1]
                else:
                    self.wall_F[0][0], self.wall_F[0][1], self.wall_F[0][2], \
                        self.wall_R[0][0], self.wall_R[0][1], self.wall_R[0][2], \
                        self.wall_B[0][0], self.wall_B[0][1], self.wall_B[0][2], \
                        self.wall_L[0][0], self.wall_L[0][1], self.wall_L[0][2], \
                        = self.wall_R[0][0], self.wall_R[0][1], self.wall_R[0][2], \
                        self.wall_B[0][0], self.wall_B[0][1], self.wall_B[0][2], \
                        self.wall_L[0][0], self.wall_L[0][1], self.wall_L[0][2], \
                        self.wall_F[0][0], self.wall_F[0][1], self.wall_F[0][2]
                    self.wall_U[0][0], self.wall_U[2][0], self.wall_U[2][2], self.wall_U[0][2] = \
                        self.wall_U[2][0], self.wall_U[2][2], self.wall_U[0][2], self.wall_U[0][0]
                    self.wall_U[0][1], self.wall_U[1][2], self.wall_U[2][1], self.wall_U[1][0] = \
                        self.wall_U[1][0], self.wall_U[0][1], self.wall_U[1][2], self.wall_U[2][1]
            elif moves[0] == 'F':
                if is_reverse:
                    self.wall_L[0][2], self.wall_L[1][2], self.wall_L[2][2], \
                        self.wall_U[2][0], self.wall_U[2][1], self.wall_U[2][2], \
                        self.wall_R[0][0], self.wall_R[1][0], self.wall_R[2][0], \
                        self.wall_D[0][0], self.wall_D[0][1], self.wall_D[0][2] \
                        = self.wall_U[2][2], self.wall_U[2][1], self.wall_U[2][0], \
                        self.wall_R[0][0], self.wall_R[1][0], self.wall_R[2][0], \
                        self.wall_D[0][2], self.wall_D[0][1], self.wall_D[0][0], \
                        self.wall_L[0][2], self.wall_L[1][2], self.wall_L[2][2]
                    self.wall_F[2][0], self.wall_F[2][2], self.wall_F[0][2], self.wall_F[0][0] = \
                        self.wall_F[0][0], self.wall_F[2][0], self.wall_F[2][2], self.wall_F[0][2]
                    self.wall_F[1][0], self.wall_F[0][1], self.wall_F[1][2], self.wall_F[2][1] = \
                        self.wall_F[0][1], self.wall_F[1][2], self.wall_F[2][1], self.wall_F[1][0]
                elif is_double:
                    self.wall_U[2][0], self.wall_U[2][1], self.wall_U[2][2], \
                        self.wall_R[0][0], self.wall_R[1][0], self.wall_R[2][0], \
                        self.wall_D[0][0], self.wall_D[0][1], self.wall_D[0][2], \
                        self.wall_L[0][2], self.wall_L[1][2], self.wall_L[2][2] \
                        = self.wall_D[0][2], self.wall_D[0][1], self.wall_D[0][0], \
                        self.wall_L[2][2], self.wall_L[1][2], self.wall_L[0][2], \
                        self.wall_U[2][2], self.wall_U[2][1], self.wall_U[2][0], \
                        self.wall_R[2][0], self.wall_R[1][0], self.wall_R[0][0]
                    self.wall_F[0][0], self.wall_F[2][0], self.wall_F[2][2], self.wall_F[0][2] = \
                        self.wall_F[2][2], self.wall_F[0][2], self.wall_F[0][0], self.wall_F[2][0]
                    self.wall_F[0][1], self.wall_F[1][2], self.wall_F[2][1], self.wall_F[1][0] = \
                        self.wall_F[2][1], self.wall_F[1][0], self.wall_F[0][1], self.wall_F[1][2]
                else:
                    self.wall_U[2][0], self.wall_U[2][1], self.wall_U[2][2], \
                        self.wall_R[0][0], self.wall_R[1][0], self.wall_R[2][0], \
                        self.wall_D[0][2], self.wall_D[0][1], self.wall_D[0][0], \
                        self.wall_L[0][2], self.wall_L[1][2], self.wall_L[2][2] \
                        = self.wall_L[2][2], self.wall_L[1][2], self.wall_L[0][2], \
                        self.wall_U[2][0], self.wall_U[2][1], self.wall_U[2][2], \
                        self.wall_R[0][0], self.wall_R[1][0], self.wall_R[2][0], \
                        self.wall_D[0][0], self.wall_D[0][1], self.wall_D[0][2]
                    self.wall_F[0][0], self.wall_F[2][0], self.wall_F[2][2], self.wall_F[0][2] = \
                        self.wall_F[2][0], self.wall_F[2][2], self.wall_F[0][2], self.wall_F[0][0]
                    self.wall_F[0][1], self.wall_F[1][2], self.wall_F[2][1], self.wall_F[1][0] = \
                        self.wall_F[1][0], self.wall_F[0][1], self.wall_F[1][2], self.wall_F[2][1]
            elif moves[0] == 'L':
                if is_reverse:
                    self.wall_B[0][2], self.wall_B[1][2], self.wall_B[2][2], \
                        self.wall_U[0][0], self.wall_U[1][0], self.wall_U[2][0], \
                        self.wall_F[0][0], self.wall_F[1][0], self.wall_F[2][0], \
                        self.wall_D[0][0], self.wall_D[1][0], self.wall_D[2][0] = \
                        self.wall_U[2][0], self.wall_U[1][0], self.wall_U[0][0], \
                        self.wall_F[0][0], self.wall_F[1][0], self.wall_F[2][0], \
                        self.wall_D[0][0], self.wall_D[1][0], self.wall_D[2][0], \
                        self.wall_B[2][2], self.wall_B[1][2], self.wall_B[0][2]
                    self.wall_L[2][0], self.wall_L[2][2], self.wall_L[0][2], self.wall_L[0][0] = \
                        self.wall_L[0][0], self.wall_L[2][0], self.wall_L[2][2], self.wall_L[0][2]
                    self.wall_L[1][0], self.wall_L[0][1], self.wall_L[1][2], self.wall_L[2][1] = \
                        self.wall_L[0][1], self.wall_L[1][2], self.wall_L[2][1], self.wall_L[1][0]
                elif is_double:
                    self.wall_B[0][2], self.wall_B[1][2], self.wall_B[2][2], \
                        self.wall_U[0][0], self.wall_U[1][0], self.wall_U[2][0], \
                        self.wall_F[0][0], self.wall_F[1][0], self.wall_F[2][0], \
                        self.wall_D[0][0], self.wall_D[1][0], self.wall_D[2][0] = \
                        self.wall_F[2][0], self.wall_F[1][0], self.wall_F[0][0], \
                        self.wall_D[0][0], self.wall_D[1][0], self.wall_D[2][0], \
                        self.wall_B[2][2], self.wall_B[1][2], self.wall_B[0][2],                         \
                        self.wall_U[0][0], self.wall_U[1][0], self.wall_U[2][0],
                    self.wall_L[2][0], self.wall_L[2][2], self.wall_L[0][2], self.wall_L[0][0] = \
                        self.wall_L[0][2], self.wall_L[0][0], self.wall_L[2][0], self.wall_L[2][2]
                    self.wall_L[1][0], self.wall_L[0][1], self.wall_L[1][2], self.wall_L[2][1] = \
                        self.wall_L[1][2], self.wall_L[2][1], self.wall_L[1][0], self.wall_L[0][1]
                else:
                    self.wall_U[2][0], self.wall_U[1][0], self.wall_U[0][0], \
                        self.wall_F[0][0], self.wall_F[1][0], self.wall_F[2][0], \
                        self.wall_D[0][0], self.wall_D[1][0], self.wall_D[2][0], \
                        self.wall_B[0][2], self.wall_B[1][2], self.wall_B[2][2] \
                        = self.wall_B[0][2], self.wall_B[1][2], self.wall_B[2][2], \
                        self.wall_U[0][0], self.wall_U[1][0], self.wall_U[2][0], \
                        self.wall_F[0][0], self.wall_F[1][0], self.wall_F[2][0], \
                        self.wall_D[2][0], self.wall_D[1][0], self.wall_D[0][0]
                    self.wall_L[0][0], self.wall_L[2][0], self.wall_L[2][2], self.wall_L[0][2] = \
                        self.wall_L[2][0], self.wall_L[2][2], self.wall_L[0][2], self.wall_L[0][0]
                    self.wall_L[0][1], self.wall_L[1][2], self.wall_L[2][1], self.wall_L[1][0] = \
                        self.wall_L[1][0], self.wall_L[0][1], self.wall_L[1][2], self.wall_L[2][1]
            elif moves[0] == 'D':
                if is_reverse:
                    self.wall_L[2][0], self.wall_L[2][1], self.wall_L[2][2], \
                        self.wall_B[2][0], self.wall_B[2][1], self.wall_B[2][2], \
                        self.wall_R[2][0], self.wall_R[2][1], self.wall_R[2][2], \
                        self.wall_F[2][0], self.wall_F[2][1], self.wall_F[2][2] \
                        = self.wall_F[2][0], self.wall_F[2][1], self.wall_F[2][2], \
                        self.wall_L[2][0], self.wall_L[2][1], self.wall_L[2][2], \
                        self.wall_B[2][0], self.wall_B[2][1], self.wall_B[2][2], \
                        self.wall_R[2][0], self.wall_R[2][1], self.wall_R[2][2]
                    self.wall_D[2][0], self.wall_D[2][2], self.wall_D[0][2], self.wall_D[0][0] = \
                        self.wall_D[0][0], self.wall_D[2][0], self.wall_D[2][2], self.wall_D[0][2]
                    self.wall_D[1][0], self.wall_D[0][1], self.wall_D[1][2], self.wall_D[2][1] = \
                        self.wall_D[0][1], self.wall_D[1][2], self.wall_D[2][1], self.wall_D[1][0]
                elif is_double:
                    self.wall_L[2][0], self.wall_L[2][1], self.wall_L[2][2], \
                        self.wall_B[2][0], self.wall_B[2][1], self.wall_B[2][2], \
                        self.wall_R[2][0], self.wall_R[2][1], self.wall_R[2][2], \
                        self.wall_F[2][0], self.wall_F[2][1], self.wall_F[2][2] \
                        = self.wall_R[2][0], self.wall_R[2][1], self.wall_R[2][2], \
                        self.wall_F[2][0], self.wall_F[2][1], self.wall_F[2][2], \
                        self.wall_L[2][0], self.wall_L[2][1], self.wall_L[2][2], \
                        self.wall_B[2][0], self.wall_B[2][1], self.wall_B[2][2]
                    self.wall_D[2][0], self.wall_D[2][2], self.wall_D[0][2], self.wall_D[0][0] = \
                        self.wall_D[0][2], self.wall_D[0][0], self.wall_D[2][0], self.wall_D[2][2]
                    self.wall_D[1][0], self.wall_D[0][1], self.wall_D[1][2], self.wall_D[2][1] = \
                        self.wall_D[1][2], self.wall_D[2][1], self.wall_D[1][0], self.wall_D[0][1]
                else:
                    self.wall_F[2][0], self.wall_F[2][1], self.wall_F[2][2], \
                        self.wall_R[2][0], self.wall_R[2][1], self.wall_R[2][2], \
                        self.wall_B[2][0], self.wall_B[2][1], self.wall_B[2][2], \
                        self.wall_L[2][0], self.wall_L[2][1], self.wall_L[2][2] \
                        = self.wall_L[2][0], self.wall_L[2][1], self.wall_L[2][2], \
                        self.wall_F[2][0], self.wall_F[2][1], self.wall_F[2][2], \
                        self.wall_R[2][0], self.wall_R[2][1], self.wall_R[2][2], \
                        self.wall_B[2][0], self.wall_B[2][1], self.wall_B[2][2]
                    self.wall_D[0][0], self.wall_D[2][0], self.wall_D[2][2], self.wall_D[0][2] = \
                        self.wall_D[2][0], self.wall_D[2][2], self.wall_D[0][2], self.wall_D[0][0]
                    self.wall_D[0][1], self.wall_D[1][2], self.wall_D[2][1], self.wall_D[1][0] = \
                        self.wall_D[1][0], self.wall_D[0][1], self.wall_D[1][2], self.wall_D[2][1]
            elif moves[0] == 'B':
                if is_reverse:
                    self.wall_R[0][2], self.wall_R[1][2], self.wall_R[2][2], \
                        self.wall_D[2][0], self.wall_D[2][1], self.wall_D[2][2], \
                        self.wall_L[0][0], self.wall_L[1][0], self.wall_L[2][0], \
                        self.wall_U[0][0], self.wall_U[0][1], self.wall_U[0][2] \
                        = self.wall_U[0][0], self.wall_U[0][1], self.wall_U[0][2], \
                        self.wall_R[2][2], self.wall_R[1][2], self.wall_R[0][2], \
                        self.wall_D[2][0], self.wall_D[2][1], self.wall_D[2][2], \
                        self.wall_L[2][0], self.wall_L[1][0], self.wall_L[0][0]
                    self.wall_B[2][0], self.wall_B[2][2], self.wall_B[0][2], self.wall_B[0][0] = \
                        self.wall_B[0][0], self.wall_B[2][0], self.wall_B[2][2], self.wall_B[0][2]
                    self.wall_B[1][0], self.wall_B[0][1], self.wall_B[1][2], self.wall_B[2][1] = \
                        self.wall_B[0][1], self.wall_B[1][2], self.wall_B[2][1], self.wall_B[1][0]
                elif is_double:
                    self.wall_U[0][2], self.wall_U[0][1], self.wall_U[0][0], \
                        self.wall_R[2][2], self.wall_R[1][2], self.wall_R[0][2], \
                        self.wall_D[2][0], self.wall_D[2][1], self.wall_D[2][2], \
                        self.wall_L[0][0], self.wall_L[1][0], self.wall_L[2][0] \
                        = self.wall_D[2][0], self.wall_D[2][1], self.wall_D[2][2], \
                        self.wall_L[0][0], self.wall_L[1][0], self.wall_L[2][0], \
                        self.wall_U[0][2], self.wall_U[0][1], self.wall_U[0][0], \
                        self.wall_R[2][2], self.wall_R[1][2], self.wall_R[0][2]
                    self.wall_B[2][0], self.wall_B[2][2], self.wall_B[0][2], self.wall_B[0][0] = \
                        self.wall_B[0][2], self.wall_B[0][0], self.wall_B[2][0], self.wall_B[2][2]
                    self.wall_B[1][0], self.wall_B[0][1], self.wall_B[1][2], self.wall_B[2][1] = \
                        self.wall_B[1][2], self.wall_B[2][1], self.wall_B[1][0], self.wall_B[0][1]
                else:
                    self.wall_U[0][0], self.wall_U[0][1], self.wall_U[0][2], \
                        self.wall_R[2][2], self.wall_R[1][2], self.wall_R[0][2], \
                        self.wall_D[2][0], self.wall_D[2][1], self.wall_D[2][2], \
                        self.wall_L[2][0], self.wall_L[1][0], self.wall_L[0][0] \
                        = self.wall_R[0][2], self.wall_R[1][2], self.wall_R[2][2], \
                        self.wall_D[2][0], self.wall_D[2][1], self.wall_D[2][2], \
                        self.wall_L[0][0], self.wall_L[1][0], self.wall_L[2][0], \
                        self.wall_U[0][0], self.wall_U[0][1], self.wall_U[0][2]
                    self.wall_B[0][0], self.wall_B[2][0], self.wall_B[2][2], self.wall_B[0][2] = \
                        self.wall_B[2][0], self.wall_B[2][2], self.wall_B[0][2], self.wall_B[0][0]
                    self.wall_B[0][1], self.wall_B[1][2], self.wall_B[2][1], self.wall_B[1][0] = \
                        self.wall_B[1][0], self.wall_B[0][1], self.wall_B[1][2], self.wall_B[2][1]
            elif moves[0] == 'M':
                if is_reverse:
                    self.wall_B[2][1], self.wall_B[1][1], self.wall_B[0][1], \
                        self.wall_U[0][1], self.wall_U[1][1], self.wall_U[2][1], \
                        self.wall_F[0][1], self.wall_F[1][1], self.wall_F[2][1], \
                        self.wall_D[2][1], self.wall_D[1][1], self.wall_D[0][1] \
                        = self.wall_U[0][1], self.wall_U[1][1], self.wall_U[2][1], \
                        self.wall_F[0][1], self.wall_F[1][1], self.wall_F[2][1], \
                        self.wall_D[0][1], self.wall_D[1][1], self.wall_D[2][1], \
                        self.wall_B[0][1], self.wall_B[1][1], self.wall_B[2][1]
                elif is_double:
                    self.wall_U[0][1], self.wall_U[1][1], self.wall_U[2][1], \
                        self.wall_F[0][1], self.wall_F[1][1], self.wall_F[2][1], \
                        self.wall_D[0][1], self.wall_D[1][1], self.wall_D[2][1], \
                        self.wall_B[0][1], self.wall_B[1][1], self.wall_B[2][1], \
                        = self.wall_D[0][1], self.wall_D[1][1], self.wall_D[2][1], \
                        self.wall_B[2][1], self.wall_B[1][1], self.wall_B[0][1], \
                        self.wall_U[0][1], self.wall_U[1][1], self.wall_U[2][1], \
                        self.wall_F[2][1], self.wall_F[1][1], self.wall_F[0][1]
                else:
                    self.wall_U[0][1], self.wall_U[1][1], self.wall_U[2][1], \
                        self.wall_F[0][1], self.wall_F[1][1], self.wall_F[2][1], \
                        self.wall_D[0][1], self.wall_D[1][1], self.wall_D[2][1], \
                        self.wall_B[0][1], self.wall_B[1][1], self.wall_B[2][1], \
                        = self.wall_B[2][1], self.wall_B[1][1], self.wall_B[0][1], \
                        self.wall_U[0][1], self.wall_U[1][1], self.wall_U[2][1], \
                        self.wall_F[0][1], self.wall_F[1][1], self.wall_F[2][1], \
                        self.wall_D[2][1], self.wall_D[1][1], self.wall_D[0][1]
            else:
                print("WARNING: bad move", moves[0])
            if save_to_history:
                self.move_count += 1
                self.history += moves[0:2] if is_reverse or is_double else moves[0]
            moves = moves[2:] if is_reverse or is_double else moves[1:]

    def get_opposite_colour(self, colour):
        if colour == 'W': return 'Y'
        elif colour == 'Y': return 'W'
        elif colour == 'R': return 'O'
        elif colour == 'O': return 'R'
        elif colour == 'B': return 'G'
        elif colour == 'G': return 'B'

    def get_edges(self):
        return [[self.wall_U[0][1], self.wall_B[0][1]],
                [self.wall_U[1][0], self.wall_L[0][1]],
                [self.wall_U[1][2], self.wall_R[0][1]],
                [self.wall_U[2][1], self.wall_F[0][1]],
                [self.wall_F[1][0], self.wall_L[1][2]],
                [self.wall_F[1][2], self.wall_R[1][0]],
                [self.wall_B[1][2], self.wall_L[1][0]],
                [self.wall_B[1][0], self.wall_R[1][2]],
                [self.wall_D[0][1], self.wall_F[2][1]],
                [self.wall_D[1][0], self.wall_L[2][1]],
                [self.wall_D[1][2], self.wall_R[2][1]],
                [self.wall_D[2][1], self.wall_B[2][1]]]

    def get_corners(self):
        return [[self.wall_U[0][0], self.wall_L[0][0], self.wall_B[0][2]],
                [self.wall_U[0][2], self.wall_R[0][2], self.wall_B[0][0]],
                [self.wall_U[2][0], self.wall_L[0][2], self.wall_F[0][0]],
                [self.wall_U[2][2], self.wall_R[0][0], self.wall_F[0][2]],
                [self.wall_D[0][0], self.wall_L[2][2], self.wall_F[2][0]],
                [self.wall_D[0][2], self.wall_R[2][0], self.wall_F[2][2]],
                [self.wall_D[2][0], self.wall_L[2][0], self.wall_B[2][2]],
                [self.wall_D[2][2], self.wall_R[2][2], self.wall_B[2][0]]]

    def is_cube_correct_set(self):
        whites = 0
        yellows = 0
        greens = 0
        blues = 0
        reds = 0
        oranges = 0
        for wall in [self.wall_F, self.wall_L, self.wall_R, self.wall_B, self.wall_U, self.wall_D]:
            for row in wall:
                for element in row:
                    if element == 'W': whites += 1
                    elif element == 'Y': yellows += 1
                    elif element == 'G': greens += 1
                    elif element == 'B': blues += 1
                    elif element == 'R': reds += 1
                    elif element == 'O': oranges += 1
        if whites != 9 or yellows != 9 or greens != 9 or blues != 9 or reds != 9 or oranges != 9:
            print("WARNING: cube is not correct set")
            return False
        rotation_local_counter = 0
        while self.wall_U[1][1] != 'W':
            if rotation_local_counter < 2:
                self.rotate('x')
            else:
                self.rotate('y')
            rotation_local_counter += 1
        while self.wall_F[1][1] != 'G':
            self.rotate('y')
            rotation_local_counter += 1
        if self.wall_R[1][1] != 'R' or self.wall_L[1][1] != 'O' or self.wall_B[1][1] != 'B' or self.wall_D[1][1] != 'Y':
            print("WARNING: cube is not correct set")
            self.undo(rotation_local_counter)
            return False
        self.undo(rotation_local_counter)
        for corner in self.get_corners():
            for sticker in corner:
                if corner.count(sticker) > 1:
                    print("WARNING: cube is not correct set")
                    return False
        for edge in self.get_edges():
            for sticker in edge:
                if edge.count(sticker) > 1:
                    print("WARNING: cube is not correct set")
                    return False
        return True

    def is_cube_solved(self):
        if not self.is_cube_correct_set():
            return False
        for wall in [self.wall_F, self.wall_L, self.wall_R, self.wall_B, self.wall_U, self.wall_D]:
            center_colour = wall[1][1]
            for row in wall:
                for element in row:
                    if element != center_colour:
                        return False
        return True

    def undo(self, num):
        while num != 0 and self.history != '':
            was_reversed = True if self.history[-1] == "'" else False
            was_doubled = True if self.history[-1] == "2" else False
            undo_move = self.history[-1] if not was_reversed and not was_doubled else self.history[-2]
            if undo_move == 'R':
                if was_reversed:
                    self.move("R", save_to_history=False)
                elif was_doubled:
                    self.move("R2", save_to_history=False)
                else:
                    self.move("R'", save_to_history=False)
            elif undo_move == 'L':
                if was_reversed:
                    self.move("L", save_to_history=False)
                elif was_doubled:
                    self.move("L2", save_to_history=False)
                else:
                    self.move("L'", save_to_history=False)
            elif undo_move == 'U':
                if was_reversed:
                    self.move("U", save_to_history=False)
                elif was_doubled:
                    self.move("U2", save_to_history=False)
                else:
                    self.move("U'", save_to_history=False)
            elif undo_move == 'D':
                if was_reversed:
                    self.move("D", save_to_history=False)
                elif was_doubled:
                    self.move("D2", save_to_history=False)
                else:
                    self.move("D'", save_to_history=False)
            elif undo_move == 'F':
                if was_reversed:
                    self.move("F", save_to_history=False)
                elif was_doubled:
                    self.move("F2", save_to_history=False)
                else:
                    self.move("F'", save_to_history=False)
            elif undo_move == 'B':
                if was_reversed:
                    self.move("B", save_to_history=False)
                elif was_doubled:
                    self.move("B2", save_to_history=False)
                else:
                    self.move("B'", save_to_history=False)
            elif undo_move == 'M':
                if was_reversed:
                    self.move("M", save_to_history=False)
                elif was_doubled:
                    self.move("M2", save_to_history=False)
                else:
                    self.move("M'", save_to_history=False)
            elif undo_move == 'x':
                if was_reversed:
                    self.rotate("x", save_to_history=False)
                elif was_doubled:
                    self.rotate("x2", save_to_history=False)
                else:
                    self.rotate("x'", save_to_history=False)
            elif undo_move == 'y':
                if was_reversed:
                    self.rotate("y", save_to_history=False)
                elif was_doubled:
                    self.rotate("y2", save_to_history=False)
                else:
                    self.rotate("y'", save_to_history=False)
            elif undo_move == 'z':
                if was_reversed:
                    self.rotate("z", save_to_history=False)
                elif was_doubled:
                    self.rotate("z2", save_to_history=False)
                else:
                    self.rotate("z'", save_to_history=False)
            self.history = self.history[0:-1] if not was_reversed and not was_doubled else self.history[0:-2]
            self.move_count -= 1
            num -= 1

    def rotate(self, rotation, save_to_history=True):
        if rotation == "x":
            self.move("RL'", save_to_history=False)
            self.wall_B[2][1], self.wall_B[1][1], self.wall_B[0][1], \
                self.wall_U[0][1], self.wall_U[1][1], self.wall_U[2][1], \
                self.wall_F[0][1], self.wall_F[1][1], self.wall_F[2][1], \
                self.wall_D[2][1], self.wall_D[1][1], self.wall_D[0][1] \
                = self.wall_U[0][1], self.wall_U[1][1], self.wall_U[2][1], \
                self.wall_F[0][1], self.wall_F[1][1], self.wall_F[2][1], \
                self.wall_D[0][1], self.wall_D[1][1], self.wall_D[2][1], \
                self.wall_B[0][1], self.wall_B[1][1], self.wall_B[2][1]
        elif rotation == "x'":
            self.move("R'L", save_to_history=False)
            self.wall_U[0][1], self.wall_U[1][1], self.wall_U[2][1], \
                self.wall_F[0][1], self.wall_F[1][1], self.wall_F[2][1], \
                self.wall_D[0][1], self.wall_D[1][1], self.wall_D[2][1], \
                self.wall_B[0][1], self.wall_B[1][1], self.wall_B[2][1], \
                = self.wall_B[2][1], self.wall_B[1][1], self.wall_B[0][1], \
                self.wall_U[0][1], self.wall_U[1][1], self.wall_U[2][1], \
                self.wall_F[0][1], self.wall_F[1][1], self.wall_F[2][1], \
                self.wall_D[2][1], self.wall_D[1][1], self.wall_D[0][1]
        elif rotation == "x2":
            self.move("R2L2", save_to_history=False)
            self.wall_U[0][1], self.wall_U[1][1], self.wall_U[2][1], \
                self.wall_F[0][1], self.wall_F[1][1], self.wall_F[2][1], \
                self.wall_D[0][1], self.wall_D[1][1], self.wall_D[2][1], \
                self.wall_B[0][1], self.wall_B[1][1], self.wall_B[2][1], \
                = self.wall_D[0][1], self.wall_D[1][1], self.wall_D[2][1], \
                self.wall_B[2][1], self.wall_B[1][1], self.wall_B[0][1], \
                self.wall_U[0][1], self.wall_U[1][1], self.wall_U[2][1], \
                self.wall_F[2][1], self.wall_F[1][1], self.wall_F[0][1]
        elif rotation == "y":
            self.move("UD'", save_to_history=False)
            self.wall_F[1][0], self.wall_F[1][1], self.wall_F[1][2], \
                self.wall_R[1][0], self.wall_R[1][1], self.wall_R[1][2], \
                self.wall_B[1][0], self.wall_B[1][1], self.wall_B[1][2], \
                self.wall_L[1][0], self.wall_L[1][1], self.wall_L[1][2] \
                = self.wall_R[1][0], self.wall_R[1][1], self.wall_R[1][2], \
                self.wall_B[1][0], self.wall_B[1][1], self.wall_B[1][2], \
                self.wall_L[1][0], self.wall_L[1][1], self.wall_L[1][2], \
                self.wall_F[1][0], self.wall_F[1][1], self.wall_F[1][2]
        elif rotation == "y'":
            self.move("U'D", save_to_history=False)
            self.wall_R[1][0], self.wall_R[1][1], self.wall_R[1][2], \
                self.wall_B[1][0], self.wall_B[1][1], self.wall_B[1][2], \
                self.wall_L[1][0], self.wall_L[1][1], self.wall_L[1][2], \
                self.wall_F[1][0], self.wall_F[1][1], self.wall_F[1][2] \
                = self.wall_F[1][0], self.wall_F[1][1], self.wall_F[1][2], \
                self.wall_R[1][0], self.wall_R[1][1], self.wall_R[1][2], \
                self.wall_B[1][0], self.wall_B[1][1], self.wall_B[1][2], \
                self.wall_L[1][0], self.wall_L[1][1], self.wall_L[1][2]
        elif rotation == "y2":
            self.move("U2D2", save_to_history=False)
            self.wall_F[1][0], self.wall_F[1][1], self.wall_F[1][2], \
                self.wall_R[1][0], self.wall_R[1][1], self.wall_R[1][2], \
                self.wall_B[1][0], self.wall_B[1][1], self.wall_B[1][2], \
                self.wall_L[1][0], self.wall_L[1][1], self.wall_L[1][2] \
                = self.wall_B[1][0], self.wall_B[1][1], self.wall_B[1][2], \
                self.wall_L[1][0], self.wall_L[1][1], self.wall_L[1][2], \
                self.wall_F[1][0], self.wall_F[1][1], self.wall_F[1][2], \
                self.wall_R[1][0], self.wall_R[1][1], self.wall_R[1][2]
        elif rotation == "z":
            self.move("FB'", save_to_history=False)
            self.wall_U[1][0], self.wall_U[1][1], self.wall_U[1][2], \
                self.wall_L[2][1], self.wall_L[1][1], self.wall_L[0][1], \
                self.wall_D[1][2], self.wall_D[1][1], self.wall_D[1][0], \
                self.wall_R[0][1], self.wall_R[1][1], self.wall_R[2][1] \
                = self.wall_L[2][1], self.wall_L[1][1], self.wall_L[0][1], \
                self.wall_D[1][2], self.wall_D[1][1], self.wall_D[1][0], \
                self.wall_R[0][1], self.wall_R[1][1], self.wall_R[2][1], \
                self.wall_U[1][0], self.wall_U[1][1], self.wall_U[1][2]
        elif rotation == "z'":
            self.move("F'B", save_to_history=False)
            self.wall_L[2][1], self.wall_L[1][1], self.wall_L[0][1], \
                self.wall_D[1][2], self.wall_D[1][1], self.wall_D[1][0], \
                self.wall_R[0][1], self.wall_R[1][1], self.wall_R[2][1], \
                self.wall_U[1][0], self.wall_U[1][1], self.wall_U[1][2] \
                = self.wall_U[1][0], self.wall_U[1][1], self.wall_U[1][2], \
                self.wall_L[2][1], self.wall_L[1][1], self.wall_L[0][1], \
                self.wall_D[1][2], self.wall_D[1][1], self.wall_D[1][0], \
                self.wall_R[0][1], self.wall_R[1][1], self.wall_R[2][1]
        elif rotation == "z2":
            self.move("F2B2", save_to_history=False)
            self.wall_L[2][1], self.wall_L[1][1], self.wall_L[0][1], \
                self.wall_D[1][2], self.wall_D[1][1], self.wall_D[1][0], \
                self.wall_R[0][1], self.wall_R[1][1], self.wall_R[2][1], \
                self.wall_U[1][0], self.wall_U[1][1], self.wall_U[1][2] = \
                self.wall_R[0][1], self.wall_R[1][1], self.wall_R[2][1], \
                self.wall_U[1][0], self.wall_U[1][1], self.wall_U[1][2], \
                self.wall_L[2][1], self.wall_L[1][1], self.wall_L[0][1], \
                self.wall_D[1][2], self.wall_D[1][1], self.wall_D[1][0]
        else:
            print("WARNING: bad rotation")
        if save_to_history:
            self.move_count += 1
            self.history += rotation
