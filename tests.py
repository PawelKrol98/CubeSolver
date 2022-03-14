import cube
import unittest


class TestCubeMethods(unittest.TestCase):

    def test_cube_size(self):
        rubic = cube.Cube()
        self.assertEqual(len(rubic.wall_F), 3)
        self.assertEqual(len(rubic.wall_B), 3)
        self.assertEqual(len(rubic.wall_R), 3)
        self.assertEqual(len(rubic.wall_L), 3)
        self.assertEqual(len(rubic.wall_U), 3)
        self.assertEqual(len(rubic.wall_D), 3)
        self.assertEqual(len(rubic.wall_D[0]), 3)
        self.assertEqual(len(rubic.wall_D[1]), 3)
        self.assertEqual(len(rubic.wall_D[2]), 3)

    def test_cube_no_initial(self):
        rubic = cube.Cube()
        self.assertEqual(rubic.wall_D[2][1], 'Y')
        self.assertEqual(rubic.wall_R[0][0], 'R')
        self.assertEqual(rubic.wall_B[2], ['B', 'B', 'B'])

    def test_cube_0_moves(self):
        rubic = cube.Cube()
        self.assertEqual(rubic.move_count, 0)

    def test_cube_10_moves(self):
        rubic = cube.Cube()
        rubic.move("R2UDLFB'D'R'UD2")
        self.assertEqual(rubic.move_count, 10)

    def test_cube_10_moves_scrambling(self):
        rubic = cube.Cube()
        rubic.move("R2UDLFB'D'R'UD2", save_to_history=False)
        self.assertEqual(rubic.move_count, 0)

    def test_cube_initial(self):
        rubic = cube.Cube(initial_state=[[['W', 'W', 'R'], ['W', 'W', 'R'], ['O', 'O', 'G']],
                                         [['G', 'G', 'Y'], ['W', 'O', 'Y'], ['B', 'B', 'B']],
                                         [['G', 'G', 'R'], ['G', 'G', 'R'], ['W', 'O', 'Y']],
                                         [['W', 'B', 'B'], ['W', 'R', 'Y'], ['G', 'G', 'Y']],
                                         [['W', 'O', 'O'], ['B', 'B', 'B'], ['R', 'R', 'Y']],
                                         [['O', 'Y', 'R'], ['O', 'Y', 'R'], ['O', 'Y', 'B']]])
        self.assertEqual(rubic.wall_D[1][1], 'Y')
        self.assertEqual(rubic.wall_U[2][0], 'O')
        self.assertEqual(rubic.wall_L[1][2], 'Y')

    def test_move_R(self):
        rubic = cube.Cube(initial_state=[[['W', 'W', 'R'], ['W', 'W', 'R'], ['O', 'O', 'G']],
                                         [['G', 'G', 'Y'], ['W', 'O', 'Y'], ['B', 'B', 'B']],
                                         [['G', 'G', 'R'], ['G', 'G', 'R'], ['W', 'O', 'Y']],
                                         [['W', 'B', 'B'], ['W', 'R', 'Y'], ['G', 'G', 'Y']],
                                         [['W', 'O', 'O'], ['B', 'B', 'B'], ['R', 'R', 'Y']],
                                         [['O', 'Y', 'R'], ['O', 'Y', 'R'], ['O', 'Y', 'B']]])
        rubic.move("R")
        self.assertEqual(rubic.wall_F[2][2], 'B')
        self.assertEqual(rubic.wall_R[2][2], 'B')
        self.assertEqual(rubic.wall_R[1][2], 'B')
        self.assertEqual(rubic.wall_B[0][0], 'G')

    def test_move_R_prime(self):
        rubic = cube.Cube(initial_state=[[['W', 'W', 'R'], ['W', 'W', 'R'], ['O', 'O', 'G']],
                                         [['G', 'G', 'Y'], ['W', 'O', 'Y'], ['B', 'B', 'B']],
                                         [['G', 'G', 'R'], ['G', 'G', 'R'], ['W', 'O', 'Y']],
                                         [['W', 'B', 'B'], ['W', 'R', 'Y'], ['G', 'G', 'Y']],
                                         [['W', 'O', 'O'], ['B', 'B', 'B'], ['R', 'R', 'Y']],
                                         [['O', 'Y', 'R'], ['O', 'Y', 'R'], ['O', 'Y', 'B']]])
        rubic.move("R'")
        self.assertEqual(rubic.wall_F[2][2], 'G')
        self.assertEqual(rubic.wall_R[2][2], 'G')
        self.assertEqual(rubic.wall_R[1][2], 'G')
        self.assertEqual(rubic.wall_B[0][0], 'B')

    def test_move_R2(self):
        rubic = cube.Cube(initial_state=[[['W', 'W', 'R'], ['W', 'W', 'R'], ['O', 'O', 'G']],
                                         [['G', 'G', 'Y'], ['W', 'O', 'Y'], ['B', 'B', 'B']],
                                         [['G', 'G', 'R'], ['G', 'G', 'R'], ['W', 'O', 'Y']],
                                         [['W', 'B', 'B'], ['W', 'R', 'Y'], ['G', 'G', 'Y']],
                                         [['W', 'O', 'O'], ['B', 'B', 'B'], ['R', 'R', 'Y']],
                                         [['O', 'Y', 'R'], ['O', 'Y', 'R'], ['O', 'Y', 'B']]])
        rubic.move("R2")
        self.assertEqual(rubic.wall_F[2][2], 'W')
        self.assertEqual(rubic.wall_R[2][2], 'W')
        self.assertEqual(rubic.wall_R[1][2], 'W')
        self.assertEqual(rubic.wall_B[0][0], 'Y')

    def test_move_U(self):
        rubic = cube.Cube(initial_state=[[['W', 'W', 'R'], ['W', 'W', 'R'], ['O', 'O', 'G']],
                                         [['G', 'G', 'Y'], ['W', 'O', 'Y'], ['B', 'B', 'B']],
                                         [['G', 'G', 'R'], ['G', 'G', 'R'], ['W', 'O', 'Y']],
                                         [['W', 'B', 'B'], ['W', 'R', 'Y'], ['G', 'G', 'Y']],
                                         [['W', 'O', 'O'], ['B', 'B', 'B'], ['R', 'R', 'Y']],
                                         [['O', 'Y', 'R'], ['O', 'Y', 'R'], ['O', 'Y', 'B']]])
        rubic.move("U")
        self.assertEqual(rubic.wall_R[0][0], 'W')
        self.assertEqual(rubic.wall_U[2][2], 'R')
        self.assertEqual(rubic.wall_U[1][2], 'W')
        self.assertEqual(rubic.wall_B[0][0], 'G')

    def test_move_U_prime(self):
        rubic = cube.Cube(initial_state=[[['W', 'W', 'R'], ['W', 'W', 'R'], ['O', 'O', 'G']],
                                         [['G', 'G', 'Y'], ['W', 'O', 'Y'], ['B', 'B', 'B']],
                                         [['G', 'G', 'R'], ['G', 'G', 'R'], ['W', 'O', 'Y']],
                                         [['W', 'B', 'B'], ['W', 'R', 'Y'], ['G', 'G', 'Y']],
                                         [['W', 'O', 'O'], ['B', 'B', 'B'], ['R', 'R', 'Y']],
                                         [['O', 'Y', 'R'], ['O', 'Y', 'R'], ['O', 'Y', 'B']]])
        rubic.move("U'")
        self.assertEqual(rubic.wall_R[0][0], 'G')
        self.assertEqual(rubic.wall_U[2][2], 'O')
        self.assertEqual(rubic.wall_U[1][2], 'O')
        self.assertEqual(rubic.wall_B[0][0], 'W')

    def test_move_U2(self):
        rubic = cube.Cube(initial_state=[[['W', 'W', 'R'], ['W', 'W', 'R'], ['O', 'O', 'G']],
                                         [['G', 'G', 'Y'], ['W', 'O', 'Y'], ['B', 'B', 'B']],
                                         [['G', 'G', 'R'], ['G', 'G', 'R'], ['W', 'O', 'Y']],
                                         [['W', 'B', 'B'], ['W', 'R', 'Y'], ['G', 'G', 'Y']],
                                         [['W', 'O', 'O'], ['B', 'B', 'B'], ['R', 'R', 'Y']],
                                         [['O', 'Y', 'R'], ['O', 'Y', 'R'], ['O', 'Y', 'B']]])
        rubic.move("U2")
        self.assertEqual(rubic.wall_R[0][0], 'G')
        self.assertEqual(rubic.wall_U[2][2], 'W')
        self.assertEqual(rubic.wall_U[1][2], 'W')
        self.assertEqual(rubic.wall_B[0][0], 'G')

    def test_move_F(self):
        rubic = cube.Cube(initial_state=[[['W', 'W', 'R'], ['W', 'W', 'R'], ['O', 'O', 'G']],
                                         [['G', 'G', 'Y'], ['W', 'O', 'Y'], ['B', 'B', 'B']],
                                         [['G', 'G', 'R'], ['G', 'G', 'R'], ['W', 'O', 'Y']],
                                         [['W', 'B', 'B'], ['W', 'R', 'Y'], ['G', 'G', 'Y']],
                                         [['W', 'O', 'O'], ['B', 'B', 'B'], ['R', 'R', 'Y']],
                                         [['O', 'Y', 'R'], ['O', 'Y', 'R'], ['O', 'Y', 'B']]])
        rubic.move("F")
        self.assertEqual(rubic.wall_R[0][0], 'O')
        self.assertEqual(rubic.wall_F[2][2], 'R')
        self.assertEqual(rubic.wall_F[1][2], 'G')
        self.assertEqual(rubic.wall_D[0][2], 'W')

    def test_move_F_prime(self):
        rubic = cube.Cube(initial_state=[[['W', 'W', 'R'], ['W', 'W', 'R'], ['O', 'O', 'G']],
                                         [['G', 'G', 'Y'], ['W', 'O', 'Y'], ['B', 'B', 'B']],
                                         [['G', 'G', 'R'], ['G', 'G', 'R'], ['W', 'O', 'Y']],
                                         [['W', 'B', 'B'], ['W', 'R', 'Y'], ['G', 'G', 'Y']],
                                         [['W', 'O', 'O'], ['B', 'B', 'B'], ['R', 'R', 'Y']],
                                         [['O', 'Y', 'R'], ['O', 'Y', 'R'], ['O', 'Y', 'B']]])
        rubic.move("F'")
        self.assertEqual(rubic.wall_R[0][0], 'R')
        self.assertEqual(rubic.wall_F[2][2], 'W')
        self.assertEqual(rubic.wall_F[1][2], 'O')
        self.assertEqual(rubic.wall_U[2][0], 'W')
        self.assertEqual(rubic.wall_U[2][2], 'G')

    def test_move_F2(self):
        rubic = cube.Cube(initial_state=[[['W', 'W', 'R'], ['W', 'W', 'R'], ['O', 'O', 'G']],
                                         [['G', 'G', 'Y'], ['W', 'O', 'Y'], ['B', 'B', 'B']],
                                         [['G', 'G', 'R'], ['G', 'G', 'R'], ['W', 'O', 'Y']],
                                         [['W', 'B', 'B'], ['W', 'R', 'Y'], ['G', 'G', 'Y']],
                                         [['W', 'O', 'O'], ['B', 'B', 'B'], ['R', 'R', 'Y']],
                                         [['O', 'Y', 'R'], ['O', 'Y', 'R'], ['O', 'Y', 'B']]])
        rubic.move("F2")
        self.assertEqual(rubic.wall_R[0][0], 'B')
        self.assertEqual(rubic.wall_F[2][2], 'G')
        self.assertEqual(rubic.wall_F[1][2], 'G')
        self.assertEqual(rubic.wall_U[2][0], 'R')
        self.assertEqual(rubic.wall_U[2][2], 'O')
        self.assertEqual(rubic.wall_L[0][2], 'G')
        self.assertEqual(rubic.wall_L[2][2], 'W')

    def test_move_L(self):
        rubic = cube.Cube(initial_state=[[['W', 'W', 'R'], ['W', 'W', 'R'], ['O', 'O', 'G']],
                                         [['G', 'G', 'Y'], ['W', 'O', 'Y'], ['B', 'B', 'B']],
                                         [['G', 'G', 'R'], ['G', 'G', 'R'], ['W', 'O', 'Y']],
                                         [['W', 'B', 'B'], ['W', 'R', 'Y'], ['G', 'G', 'Y']],
                                         [['W', 'O', 'O'], ['B', 'B', 'B'], ['R', 'R', 'Y']],
                                         [['O', 'Y', 'R'], ['O', 'Y', 'R'], ['O', 'Y', 'B']]])
        rubic.move("L")
        self.assertEqual(rubic.wall_F[0][0], 'W')
        self.assertEqual(rubic.wall_L[2][2], 'Y')
        self.assertEqual(rubic.wall_L[1][2], 'G')
        self.assertEqual(rubic.wall_B[0][2], 'O')

    def test_move_L_prime(self):
        rubic = cube.Cube(initial_state=[[['W', 'W', 'R'], ['W', 'W', 'R'], ['O', 'O', 'G']],
                                         [['G', 'G', 'Y'], ['W', 'O', 'Y'], ['B', 'B', 'B']],
                                         [['G', 'G', 'R'], ['G', 'G', 'R'], ['W', 'O', 'Y']],
                                         [['W', 'B', 'B'], ['W', 'R', 'Y'], ['G', 'G', 'Y']],
                                         [['W', 'O', 'O'], ['B', 'B', 'B'], ['R', 'R', 'Y']],
                                         [['O', 'Y', 'R'], ['O', 'Y', 'R'], ['O', 'Y', 'B']]])
        rubic.move("L'")
        self.assertEqual(rubic.wall_F[0][0], 'O')
        self.assertEqual(rubic.wall_F[2][0], 'O')
        self.assertEqual(rubic.wall_L[2][2], 'B')
        self.assertEqual(rubic.wall_L[1][2], 'B')
        self.assertEqual(rubic.wall_B[0][2], 'O')
        self.assertEqual(rubic.wall_B[2][2], 'W')

    def test_move_L2(self):
        rubic = cube.Cube(initial_state=[[['W', 'W', 'R'], ['W', 'W', 'R'], ['O', 'O', 'G']],
                                         [['G', 'G', 'Y'], ['W', 'O', 'Y'], ['B', 'B', 'B']],
                                         [['G', 'G', 'R'], ['G', 'G', 'R'], ['W', 'O', 'Y']],
                                         [['W', 'B', 'B'], ['W', 'R', 'Y'], ['G', 'G', 'Y']],
                                         [['W', 'O', 'O'], ['B', 'B', 'B'], ['R', 'R', 'Y']],
                                         [['O', 'Y', 'R'], ['O', 'Y', 'R'], ['O', 'Y', 'B']]])
        rubic.move("L2")
        self.assertEqual(rubic.wall_F[0][0], 'Y')
        self.assertEqual(rubic.wall_L[2][2], 'G')
        self.assertEqual(rubic.wall_L[1][2], 'W')
        self.assertEqual(rubic.wall_B[0][2], 'W')

    def test_move_D(self):
        rubic = cube.Cube(initial_state=[[['W', 'W', 'R'], ['W', 'W', 'R'], ['O', 'O', 'G']],
                                         [['G', 'G', 'Y'], ['W', 'O', 'Y'], ['B', 'B', 'B']],
                                         [['G', 'G', 'R'], ['G', 'G', 'R'], ['W', 'O', 'Y']],
                                         [['W', 'B', 'B'], ['W', 'R', 'Y'], ['G', 'G', 'Y']],
                                         [['W', 'O', 'O'], ['B', 'B', 'B'], ['R', 'R', 'Y']],
                                         [['O', 'Y', 'R'], ['O', 'Y', 'R'], ['O', 'Y', 'B']]])
        rubic.move("D")
        self.assertEqual(rubic.wall_F[2][2], 'B')
        self.assertEqual(rubic.wall_D[2][2], 'R')
        self.assertEqual(rubic.wall_D[1][2], 'Y')
        self.assertEqual(rubic.wall_B[2][0], 'G')
        self.assertEqual(rubic.wall_B[2][2], 'Y')
        self.assertEqual(rubic.wall_L[2][0], 'R')
        self.assertEqual(rubic.wall_L[2][2], 'Y')

    def test_move_D_prime(self):
        rubic = cube.Cube(initial_state=[[['W', 'W', 'R'], ['W', 'W', 'R'], ['O', 'O', 'G']],
                                         [['G', 'G', 'Y'], ['W', 'O', 'Y'], ['B', 'B', 'B']],
                                         [['G', 'G', 'R'], ['G', 'G', 'R'], ['W', 'O', 'Y']],
                                         [['W', 'B', 'B'], ['W', 'R', 'Y'], ['G', 'G', 'Y']],
                                         [['W', 'O', 'O'], ['B', 'B', 'B'], ['R', 'R', 'Y']],
                                         [['O', 'Y', 'R'], ['O', 'Y', 'R'], ['O', 'Y', 'B']]])
        rubic.move("D'")
        self.assertEqual(rubic.wall_F[2][2], 'Y')
        self.assertEqual(rubic.wall_D[2][2], 'O')
        self.assertEqual(rubic.wall_D[1][2], 'Y')
        self.assertEqual(rubic.wall_B[2][0], 'B')
        self.assertEqual(rubic.wall_B[2][2], 'B')
        self.assertEqual(rubic.wall_L[2][0], 'W')
        self.assertEqual(rubic.wall_L[2][2], 'Y')
        self.assertEqual(rubic.wall_R[2][0], 'R')
        self.assertEqual(rubic.wall_R[2][2], 'Y')

    def test_move_D2(self):
        rubic = cube.Cube(initial_state=[[['W', 'W', 'R'], ['W', 'W', 'R'], ['O', 'O', 'G']],
                                         [['G', 'G', 'Y'], ['W', 'O', 'Y'], ['B', 'B', 'B']],
                                         [['G', 'G', 'R'], ['G', 'G', 'R'], ['W', 'O', 'Y']],
                                         [['W', 'B', 'B'], ['W', 'R', 'Y'], ['G', 'G', 'Y']],
                                         [['W', 'O', 'O'], ['B', 'B', 'B'], ['R', 'R', 'Y']],
                                         [['O', 'Y', 'R'], ['O', 'Y', 'R'], ['O', 'Y', 'B']]])
        rubic.move("D2")
        self.assertEqual(rubic.wall_F[2][2], 'Y')
        self.assertEqual(rubic.wall_D[2][2], 'O')
        self.assertEqual(rubic.wall_D[1][2], 'O')

    def test_move_B(self):
        rubic = cube.Cube(initial_state=[[['W', 'W', 'R'], ['W', 'W', 'R'], ['O', 'O', 'G']],
                                         [['G', 'G', 'Y'], ['W', 'O', 'Y'], ['B', 'B', 'B']],
                                         [['G', 'G', 'R'], ['G', 'G', 'R'], ['W', 'O', 'Y']],
                                         [['W', 'B', 'B'], ['W', 'R', 'Y'], ['G', 'G', 'Y']],
                                         [['W', 'O', 'O'], ['B', 'B', 'B'], ['R', 'R', 'Y']],
                                         [['O', 'Y', 'R'], ['O', 'Y', 'R'], ['O', 'Y', 'B']]])
        rubic.move("B")
        self.assertEqual(rubic.wall_R[2][2], 'O')
        self.assertEqual(rubic.wall_B[2][2], 'O')
        self.assertEqual(rubic.wall_B[1][2], 'O')

    def test_move_B_prime(self):
        rubic = cube.Cube(initial_state=[[['W', 'W', 'R'], ['W', 'W', 'R'], ['O', 'O', 'G']],
                                         [['G', 'G', 'Y'], ['W', 'O', 'Y'], ['B', 'B', 'B']],
                                         [['G', 'G', 'R'], ['G', 'G', 'R'], ['W', 'O', 'Y']],
                                         [['W', 'B', 'B'], ['W', 'R', 'Y'], ['G', 'G', 'Y']],
                                         [['W', 'O', 'O'], ['B', 'B', 'B'], ['R', 'R', 'Y']],
                                         [['O', 'Y', 'R'], ['O', 'Y', 'R'], ['O', 'Y', 'B']]])
        rubic.move("B'")
        self.assertEqual(rubic.wall_R[2][2], 'R')
        self.assertEqual(rubic.wall_B[2][2], 'R')
        self.assertEqual(rubic.wall_B[1][2], 'R')

    def test_move_B2(self):
        rubic = cube.Cube(initial_state=[[['W', 'W', 'R'], ['W', 'W', 'R'], ['O', 'O', 'G']],
                                         [['G', 'G', 'Y'], ['W', 'O', 'Y'], ['B', 'B', 'B']],
                                         [['G', 'G', 'R'], ['G', 'G', 'R'], ['W', 'O', 'Y']],
                                         [['W', 'B', 'B'], ['W', 'R', 'Y'], ['G', 'G', 'Y']],
                                         [['W', 'O', 'O'], ['B', 'B', 'B'], ['R', 'R', 'Y']],
                                         [['O', 'Y', 'R'], ['O', 'Y', 'R'], ['O', 'Y', 'B']]])
        rubic.move("B2")
        self.assertEqual(rubic.wall_R[2][2], 'G')
        self.assertEqual(rubic.wall_B[2][2], 'W')
        self.assertEqual(rubic.wall_B[1][2], 'B')
        self.assertEqual(rubic.wall_U[0][0], 'B')
        self.assertEqual(rubic.wall_U[0][2], 'O')

    def test_sexy_move(self):
        rubic = cube.Cube()
        rubic.move("RUR'U'L'U'LU")
        self.assertEqual(rubic.wall_F, [['Y', 'G', 'Y'], ['W', 'G', 'W'], ['G', 'G', 'G']])

    def test_5_movesA(self):
        rubic = cube.Cube()
        rubic.move("RF'D2LU'")
        self.assertEqual(rubic.wall_F, [['Y', 'O', 'O'], ['W', 'G', 'G'], ['R', 'B', 'B']])

    def test_5_movesB(self):
        rubic = cube.Cube()
        rubic.move("R2F2D2B'D'")
        self.assertEqual(rubic.wall_F, [['B', 'G', 'G'], ['B', 'G', 'G'], ['O', 'O', 'Y']])

    def test_10_movesA(self):
        rubic = cube.Cube()
        rubic.move("R2F2D2B'D'F2R'LUB")
        self.assertEqual(rubic.wall_F, [['W', 'W', 'B'], ['W', 'G', 'Y'], ['R', 'G', 'Y']])

    def test_10_movesB(self):
        rubic = cube.Cube()
        rubic.move("B'U'L'RF2DBD2F2R2")
        self.assertEqual(rubic.wall_F, [['O', 'O', 'B'], ['Y', 'G', 'W'], ['R', 'G', 'O']])

    def test_20_movesA(self):
        rubic = cube.Cube()
        rubic.move("BFLFR'U'BU2L2RBU'D'L'B'L'FD'F2L'")
        self.assertEqual(rubic.wall_F, [['G', 'G', 'O'], ['O', 'G', 'O'], ['W', 'W', 'G']])

    def test_20_movesB(self):
        rubic = cube.Cube()
        rubic.move("L2U2FL'F'LFR'B2U2R2UB'R'L2F2RD2F2L")
        self.assertEqual(rubic.wall_F, [['G', 'Y', 'O'], ['B', 'G', 'Y'], ['W', 'G', 'B']])

    def test_20_movesC(self):
        rubic = cube.Cube()
        rubic.move("D'F2BRDB'DLU'R'LF2D'BR2DB'DL'R2")
        self.assertEqual(rubic.wall_F, [['B', 'B', 'B'], ['B', 'G', 'Y'], ['O', 'G', 'W']])

    def test_25_moves(self):
        rubic = cube.Cube()
        rubic.move("B2L2FD'LF2B'L'D'UBD'B'LU'R2F'D2L'F2RU'F2U2D")
        self.assertEqual(rubic.wall_F, [['O', 'R', 'Y'], ['G', 'G', 'B'], ['B', 'B', 'O']])

    def test_50_moves_A(self):
        rubic = cube.Cube()
        rubic.move("L'B'RDB2FD'RF'L'BU2B2LRB'R'D2R'LF'R'U2R'B2L'R2F'UL'B2R2BRL'FRL2FR'LF2RF'B2R'U2D'LU'")
        self.assertEqual(rubic.wall_F, [['R', 'B', 'G'], ['Y', 'G', 'G'], ['G', 'R', 'B']])

    def test_50_moves_B(self):
        rubic = cube.Cube()
        rubic.move("BFDB'D'F2B'U2L'F'LR2F'LD'L'ULF'L'UL2R'U2B'DF2D2F'B2UL'BR'F'L2D2R2B'R'D2F2D2U'R2BURUR")
        self.assertEqual(rubic.wall_F, [['R', 'G', 'W'], ['Y', 'G', 'B'], ['R', 'O', 'W']])

    def test_correct_setup(self):
        rubic = cube.Cube()
        self.assertTrue(rubic.is_cube_correct_set())

    def test_incorrect_setup_too_much_white(self):
        rubic = cube.Cube(initial_state=[[['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],
                                         [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']],
                                         [['G', 'G', 'G'], ['G', 'G', 'W'], ['G', 'G', 'G']],
                                         [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']],
                                         [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],
                                         [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']]])
        self.assertFalse(rubic.is_cube_correct_set())

    def test_incorrect_setup_too_much_green(self):
        rubic = cube.Cube(initial_state=[[['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],
                                         [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']],
                                         [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']],
                                         [['R', 'R', 'R'], ['R', 'R', 'G'], ['R', 'R', 'R']],
                                         [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],
                                         [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']]])
        self.assertFalse(rubic.is_cube_correct_set())

    def test_incorrect_setup_white_switched_with_yellow(self):
        rubic = cube.Cube(initial_state=[[['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']],
                                         [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']],
                                         [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']],
                                         [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']],
                                         [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],
                                         [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']]])
        self.assertFalse(rubic.is_cube_correct_set())

    def test_incorrect_setup_white_switched_with_green(self):
        rubic = cube.Cube(initial_state=[[['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']],
                                         [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']],
                                         [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],
                                         [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']],
                                         [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],
                                         [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']]])
        self.assertFalse(rubic.is_cube_correct_set())

    def test_empty_history(self):
        rubic = cube.Cube()
        self.assertEqual(rubic.history, '')

    def test_empty_history_scrambling(self):
        rubic = cube.Cube()
        rubic.move("RURB'U2", save_to_history=False)
        self.assertEqual(rubic.history, '')

    def test_history_filled(self):
        rubic = cube.Cube()
        rubic.move("RURB'U2")
        self.assertEqual(rubic.history, "RURB'U2")

    def test_cube_solved(self):
        rubic = cube.Cube()
        self.assertTrue(rubic.is_cube_solved())

    def test_cube_not_solved(self):
        rubic = cube.Cube()
        rubic.move("R")
        self.assertFalse(rubic.is_cube_solved())

    def test_cube_solved_bad_set(self):
        rubic = cube.Cube(initial_state=[[['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']],
                                         [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']],
                                         [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],
                                         [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']],
                                         [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],
                                         [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']]])
        self.assertEqual(rubic.is_cube_solved(), False)

    def test_undo_history(self):
        rubic = cube.Cube()
        rubic.move("RUBF'U2DURL'")
        rubic.undo(5)
        self.assertEqual(rubic.history, "RUBF'")

    def test_undo_count_moves(self):
        rubic = cube.Cube()
        rubic.move("RUBF'U2DURL'")
        rubic.undo(5)
        self.assertEqual(rubic.move_count, 4)

    def test_undo_wall(self):
        rubic = cube.Cube()
        rubic.move("RUBF'U2DURL'")
        rubic.undo(5)
        self.assertEqual(rubic.wall_F, [['R', 'Y', 'Y'], ['R', 'G', 'G'], ['R', 'G', 'G']])

    def test_undo_more_moves(self):
        rubic = cube.Cube()
        rubic.move("RUBF'U2DURL'")
        rubic.undo(10)
        self.assertEqual(rubic.move_count, 0)
        self.assertEqual(rubic.history, '')

    def test_equal_op_pass(self):
        rubicA = cube.Cube(initial_state=[[['Y', 'G', 'Y'], ['W', 'W', 'R'], ['W', 'O', 'G']],
                                         [['G', 'R', 'B'], ['G', 'O', 'Y'], ['W', 'O', 'W']],
                                         [['O', 'B', 'R'], ['R', 'G', 'W'], ['B', 'B', 'Y']],
                                         [['W', 'B', 'B'], ['B', 'R', 'G'], ['O', 'Y', 'Y']],
                                         [['R', 'R', 'R'], ['Y', 'B', 'O'], ['B', 'W', 'O']],
                                         [['R', 'Y', 'G'], ['W', 'Y', 'O'], ['G', 'G', 'O']]])
        rubicB = cube.Cube(initial_state=[[['Y', 'G', 'Y'], ['W', 'W', 'R'], ['W', 'O', 'G']],
                                         [['G', 'R', 'B'], ['G', 'O', 'Y'], ['W', 'O', 'W']],
                                         [['O', 'B', 'R'], ['R', 'G', 'W'], ['B', 'B', 'Y']],
                                         [['W', 'B', 'B'], ['B', 'R', 'G'], ['O', 'Y', 'Y']],
                                         [['R', 'R', 'R'], ['Y', 'B', 'O'], ['B', 'W', 'O']],
                                         [['R', 'Y', 'G'], ['W', 'Y', 'O'], ['G', 'G', 'O']]])
        self.assertTrue(rubicA == rubicB)

    def test_equal_op_fail(self):
        rubicA = cube.Cube(initial_state=[[['Y', 'G', 'Y'], ['W', 'W', 'R'], ['W', 'O', 'G']],
                                          [['G', 'R', 'B'], ['G', 'O', 'Y'], ['W', 'O', 'W']],
                                          [['O', 'B', 'R'], ['R', 'G', 'W'], ['B', 'B', 'Y']],
                                          [['W', 'B', 'B'], ['B', 'R', 'G'], ['O', 'Y', 'Y']],
                                          [['R', 'R', 'R'], ['Y', 'B', 'O'], ['B', 'W', 'O']],
                                          [['R', 'Y', 'G'], ['W', 'Y', 'O'], ['G', 'G', 'O']]])
        rubicA.move("R")
        rubicB = cube.Cube(initial_state=[[['Y', 'G', 'Y'], ['W', 'W', 'R'], ['W', 'O', 'G']],
                                          [['G', 'R', 'B'], ['G', 'O', 'Y'], ['W', 'O', 'W']],
                                          [['O', 'B', 'R'], ['R', 'G', 'W'], ['B', 'B', 'Y']],
                                          [['W', 'B', 'B'], ['B', 'R', 'G'], ['O', 'Y', 'Y']],
                                          [['R', 'R', 'R'], ['Y', 'B', 'O'], ['B', 'W', 'O']],
                                          [['R', 'Y', 'G'], ['W', 'Y', 'O'], ['G', 'G', 'O']]])
        self.assertFalse(rubicA == rubicB)

    def test_rotation_x(self):
        rubic = cube.Cube(initial_state=[[['Y', 'G', 'Y'], ['W', 'W', 'R'], ['W', 'O', 'G']],
                                         [['G', 'R', 'B'], ['G', 'O', 'Y'], ['W', 'O', 'W']],
                                         [['O', 'B', 'R'], ['R', 'G', 'W'], ['B', 'B', 'Y']],
                                         [['W', 'B', 'B'], ['B', 'R', 'G'], ['O', 'Y', 'Y']],
                                         [['R', 'R', 'R'], ['Y', 'B', 'O'], ['B', 'W', 'O']],
                                         [['R', 'Y', 'G'], ['W', 'Y', 'O'], ['G', 'G', 'O']]])
        rubic_rotated = cube.Cube(initial_state=[[['O', 'B', 'R'], ['R', 'G', 'W'], ['B', 'B', 'Y']],
                                                 [['B', 'Y', 'W'], ['R', 'O', 'O'], ['G', 'G', 'W']],
                                                 [['R', 'Y', 'G'], ['W', 'Y', 'O'], ['G', 'G', 'O']],
                                                 [['O', 'B', 'W'], ['Y', 'R', 'B'], ['Y', 'G', 'B']],
                                                 [['G', 'O', 'W'], ['R', 'W', 'W'], ['Y', 'G', 'Y']],
                                                 [['O', 'W', 'B'], ['O', 'B', 'Y'], ['R', 'R', 'R']]])
        rubic.rotate("x")
        self.assertTrue(rubic == rubic_rotated)

    def test_rotation_x_prime(self):
        rubic = cube.Cube(initial_state=[[['Y', 'G', 'Y'], ['W', 'W', 'R'], ['W', 'O', 'G']],
                                         [['G', 'R', 'B'], ['G', 'O', 'Y'], ['W', 'O', 'W']],
                                         [['O', 'B', 'R'], ['R', 'G', 'W'], ['B', 'B', 'Y']],
                                         [['W', 'B', 'B'], ['B', 'R', 'G'], ['O', 'Y', 'Y']],
                                         [['R', 'R', 'R'], ['Y', 'B', 'O'], ['B', 'W', 'O']],
                                         [['R', 'Y', 'G'], ['W', 'Y', 'O'], ['G', 'G', 'O']]])
        rubic_rotated = cube.Cube(initial_state=[[['O', 'W', 'B'], ['O', 'B', 'Y'], ['R', 'R', 'R']],
                                                 [['W', 'G', 'G'], ['O', 'O', 'R'], ['W', 'Y', 'B']],
                                                 [['Y', 'G', 'Y'], ['W', 'W', 'R'], ['W', 'O', 'G']],
                                                 [['B', 'G', 'Y'], ['B', 'R', 'Y'], ['W', 'B', 'O']],
                                                 [['O', 'G', 'G'], ['O', 'Y', 'W'], ['G', 'Y', 'R']],
                                                 [['O', 'B', 'R'], ['R', 'G', 'W'], ['B', 'B', 'Y']]])
        rubic.rotate("x'")
        self.assertTrue(rubic == rubic_rotated)

    def test_rotation_x_double(self):
        rubic = cube.Cube(initial_state=[[['Y', 'G', 'Y'], ['W', 'W', 'R'], ['W', 'O', 'G']],
                                         [['G', 'R', 'B'], ['G', 'O', 'Y'], ['W', 'O', 'W']],
                                         [['O', 'B', 'R'], ['R', 'G', 'W'], ['B', 'B', 'Y']],
                                         [['W', 'B', 'B'], ['B', 'R', 'G'], ['O', 'Y', 'Y']],
                                         [['R', 'R', 'R'], ['Y', 'B', 'O'], ['B', 'W', 'O']],
                                         [['R', 'Y', 'G'], ['W', 'Y', 'O'], ['G', 'G', 'O']]])
        rubic_rotated = cube.Cube(initial_state=[[['R', 'Y', 'G'], ['W', 'Y', 'O'], ['G', 'G', 'O']],
                                                 [['W', 'O', 'W'], ['Y', 'O', 'G'], ['B', 'R', 'G']],
                                                 [['O', 'W', 'B'], ['O', 'B', 'Y'], ['R', 'R', 'R']],
                                                 [['Y', 'Y', 'O'], ['G', 'R', 'B'], ['B', 'B', 'W']],
                                                 [['Y', 'B', 'B'], ['W', 'G', 'R'], ['R', 'B', 'O']],
                                                 [['Y', 'G', 'Y'], ['W', 'W', 'R'], ['W', 'O', 'G']]])
        rubic.rotate("x2")
        self.assertTrue(rubic == rubic_rotated)

    def test_rotation_y(self):
        rubic = cube.Cube(initial_state=[[['Y', 'G', 'Y'], ['W', 'W', 'R'], ['W', 'O', 'G']],
                                         [['G', 'R', 'B'], ['G', 'O', 'Y'], ['W', 'O', 'W']],
                                         [['O', 'B', 'R'], ['R', 'G', 'W'], ['B', 'B', 'Y']],
                                         [['W', 'B', 'B'], ['B', 'R', 'G'], ['O', 'Y', 'Y']],
                                         [['R', 'R', 'R'], ['Y', 'B', 'O'], ['B', 'W', 'O']],
                                         [['R', 'Y', 'G'], ['W', 'Y', 'O'], ['G', 'G', 'O']]])
        rubic_rotated = cube.Cube(initial_state=[[['W', 'W', 'Y'], ['O', 'W', 'G'], ['G', 'R', 'Y']],
                                                 [['O', 'B', 'R'], ['R', 'G', 'W'], ['B', 'B', 'Y']],
                                                 [['W', 'B', 'B'], ['B', 'R', 'G'], ['O', 'Y', 'Y']],
                                                 [['R', 'R', 'R'], ['Y', 'B', 'O'], ['B', 'W', 'O']],
                                                 [['G', 'R', 'B'], ['G', 'O', 'Y'], ['W', 'O', 'W']],
                                                 [['G', 'O', 'O'], ['Y', 'Y', 'G'], ['R', 'W', 'G']]])
        rubic.rotate("y")
        self.assertTrue(rubic == rubic_rotated)

    def test_rotation_y_prime(self):
        rubic = cube.Cube(initial_state=[[['Y', 'G', 'Y'], ['W', 'W', 'R'], ['W', 'O', 'G']],
                                         [['G', 'R', 'B'], ['G', 'O', 'Y'], ['W', 'O', 'W']],
                                         [['O', 'B', 'R'], ['R', 'G', 'W'], ['B', 'B', 'Y']],
                                         [['W', 'B', 'B'], ['B', 'R', 'G'], ['O', 'Y', 'Y']],
                                         [['R', 'R', 'R'], ['Y', 'B', 'O'], ['B', 'W', 'O']],
                                         [['R', 'Y', 'G'], ['W', 'Y', 'O'], ['G', 'G', 'O']]])
        rubic_rotated = cube.Cube(initial_state=[[['Y', 'R', 'G'], ['G', 'W', 'O'], ['Y', 'W', 'W']],
                                                 [['R', 'R', 'R'], ['Y', 'B', 'O'], ['B', 'W', 'O']],
                                                 [['G', 'R', 'B'], ['G', 'O', 'Y'], ['W', 'O', 'W']],
                                                 [['O', 'B', 'R'], ['R', 'G', 'W'], ['B', 'B', 'Y']],
                                                 [['W', 'B', 'B'], ['B', 'R', 'G'], ['O', 'Y', 'Y']],
                                                 [['G', 'W', 'R'], ['G', 'Y', 'Y'], ['O', 'O', 'G']]])
        rubic.rotate("y'")
        self.assertTrue(rubic == rubic_rotated)

    def test_rotation_y_double(self):
        rubic = cube.Cube(initial_state=[[['Y', 'G', 'Y'], ['W', 'W', 'R'], ['W', 'O', 'G']],
                                         [['G', 'R', 'B'], ['G', 'O', 'Y'], ['W', 'O', 'W']],
                                         [['O', 'B', 'R'], ['R', 'G', 'W'], ['B', 'B', 'Y']],
                                         [['W', 'B', 'B'], ['B', 'R', 'G'], ['O', 'Y', 'Y']],
                                         [['R', 'R', 'R'], ['Y', 'B', 'O'], ['B', 'W', 'O']],
                                         [['R', 'Y', 'G'], ['W', 'Y', 'O'], ['G', 'G', 'O']]])
        rubic_rotated = cube.Cube(initial_state=[[['G', 'O', 'W'], ['R', 'W', 'W'], ['Y', 'G', 'Y']],
                                                 [['W', 'B', 'B'], ['B', 'R', 'G'], ['O', 'Y', 'Y']],
                                                 [['R', 'R', 'R'], ['Y', 'B', 'O'], ['B', 'W', 'O']],
                                                 [['G', 'R', 'B'], ['G', 'O', 'Y'], ['W', 'O', 'W']],
                                                 [['O', 'B', 'R'], ['R', 'G', 'W'], ['B', 'B', 'Y']],
                                                 [['O', 'G', 'G'], ['O', 'Y', 'W'], ['G', 'Y', 'R']]])
        rubic.rotate("y2")
        self.assertTrue(rubic == rubic_rotated)

    def test_rotation_z(self):
        rubic = cube.Cube(initial_state=[[['Y', 'G', 'Y'], ['W', 'W', 'R'], ['W', 'O', 'G']],
                                         [['G', 'R', 'B'], ['G', 'O', 'Y'], ['W', 'O', 'W']],
                                         [['O', 'B', 'R'], ['R', 'G', 'W'], ['B', 'B', 'Y']],
                                         [['W', 'B', 'B'], ['B', 'R', 'G'], ['O', 'Y', 'Y']],
                                         [['R', 'R', 'R'], ['Y', 'B', 'O'], ['B', 'W', 'O']],
                                         [['R', 'Y', 'G'], ['W', 'Y', 'O'], ['G', 'G', 'O']]])
        rubic_rotated = cube.Cube(initial_state=[[['W', 'G', 'G'], ['O', 'O', 'R'], ['W', 'Y', 'B']],
                                                 [['G', 'W', 'R'], ['G', 'Y', 'Y'], ['O', 'O', 'G']],
                                                 [['B', 'R', 'O'], ['B', 'G', 'B'], ['Y', 'W', 'R']],
                                                 [['W', 'W', 'Y'], ['O', 'W', 'G'], ['G', 'R', 'Y']],
                                                 [['R', 'O', 'O'], ['R', 'B', 'W'], ['R', 'Y', 'B']],
                                                 [['O', 'B', 'W'], ['Y', 'R', 'B'], ['Y', 'G', 'B']]])
        rubic.rotate("z")
        self.assertTrue(rubic == rubic_rotated)

    def test_rotation_z_prime(self):
        rubic = cube.Cube(initial_state=[[['Y', 'G', 'Y'], ['W', 'W', 'R'], ['W', 'O', 'G']],
                                         [['G', 'R', 'B'], ['G', 'O', 'Y'], ['W', 'O', 'W']],
                                         [['O', 'B', 'R'], ['R', 'G', 'W'], ['B', 'B', 'Y']],
                                         [['W', 'B', 'B'], ['B', 'R', 'G'], ['O', 'Y', 'Y']],
                                         [['R', 'R', 'R'], ['Y', 'B', 'O'], ['B', 'W', 'O']],
                                         [['R', 'Y', 'G'], ['W', 'Y', 'O'], ['G', 'G', 'O']]])
        rubic_rotated = cube.Cube(initial_state=[[['B', 'G', 'Y'], ['B', 'R', 'Y'], ['W', 'B', 'O']],
                                                 [['Y', 'R', 'G'], ['G', 'W', 'O'], ['Y', 'W', 'W']],
                                                 [['R', 'W', 'Y'], ['B', 'G', 'B'], ['O', 'R', 'B']],
                                                 [['G', 'O', 'O'], ['Y', 'Y', 'G'], ['R', 'W', 'G']],
                                                 [['B', 'Y', 'R'], ['W', 'B', 'R'], ['O', 'O', 'R']],
                                                 [['B', 'Y', 'W'], ['R', 'O','O'], ['G', 'G', 'W']]])
        rubic.rotate("z'")
        self.assertTrue(rubic == rubic_rotated)

    def test_rotation_z_double(self):
        rubic = cube.Cube(initial_state=[[['Y', 'G', 'Y'], ['W', 'W', 'R'], ['W', 'O', 'G']],
                                         [['G', 'R', 'B'], ['G', 'O', 'Y'], ['W', 'O', 'W']],
                                         [['O', 'B', 'R'], ['R', 'G', 'W'], ['B', 'B', 'Y']],
                                         [['W', 'B', 'B'], ['B', 'R', 'G'], ['O', 'Y', 'Y']],
                                         [['R', 'R', 'R'], ['Y', 'B', 'O'], ['B', 'W', 'O']],
                                         [['R', 'Y', 'G'], ['W', 'Y', 'O'], ['G', 'G', 'O']]])
        rubic_rotated = cube.Cube(initial_state=[[['O', 'G', 'G'], ['O', 'Y', 'W'], ['G', 'Y', 'R']],
                                                 [['Y', 'Y', 'O'], ['G', 'R', 'B'], ['B', 'B', 'W']],
                                                 [['Y', 'B', 'B'], ['W', 'G', 'R'], ['R', 'B', 'O']],
                                                 [['W', 'O', 'W'], ['Y', 'O', 'G'], ['B', 'R', 'G']],
                                                 [['O', 'W', 'B'], ['O', 'B', 'Y'], ['R', 'R', 'R']],
                                                 [['G', 'O', 'W'], ['R', 'W', 'W'], ['Y', 'G', 'Y']]])
        rubic.rotate("z2")
        self.assertTrue(rubic == rubic_rotated)

    def test_move_M(self):
        rubic = cube.Cube(initial_state=[[['Y', 'G', 'Y'], ['W', 'W', 'R'], ['W', 'O', 'G']],
                                         [['G', 'R', 'B'], ['G', 'O', 'Y'], ['W', 'O', 'W']],
                                         [['O', 'B', 'R'], ['R', 'G', 'W'], ['B', 'B', 'Y']],
                                         [['W', 'B', 'B'], ['B', 'R', 'G'], ['O', 'Y', 'Y']],
                                         [['R', 'R', 'R'], ['Y', 'B', 'O'], ['B', 'W', 'O']],
                                         [['R', 'Y', 'G'], ['W', 'Y', 'O'], ['G', 'G', 'O']]])
        rubic_moved = cube.Cube(initial_state=[[['Y', 'W', 'Y'], ['W', 'B', 'R'], ['W', 'R', 'G']],
                                                 [['G', 'R', 'B'], ['G', 'O', 'Y'], ['W', 'O', 'W']],
                                                 [['O', 'G', 'R'], ['R', 'W', 'W'], ['B', 'O', 'Y']],
                                                 [['W', 'B', 'B'], ['B', 'R', 'G'], ['O', 'Y', 'Y']],
                                                 [['R', 'G', 'R'], ['Y', 'Y', 'O'], ['B', 'Y', 'O']],
                                                 [['R', 'B', 'G'], ['W', 'G', 'O'], ['G', 'B', 'O']]])
        rubic.move("M")
        self.assertTrue(rubic == rubic_moved)

    def test_move_M_prime(self):
        rubic = cube.Cube(initial_state=[[['Y', 'G', 'Y'], ['W', 'W', 'R'], ['W', 'O', 'G']],
                                         [['G', 'R', 'B'], ['G', 'O', 'Y'], ['W', 'O', 'W']],
                                         [['O', 'B', 'R'], ['R', 'G', 'W'], ['B', 'B', 'Y']],
                                         [['W', 'B', 'B'], ['B', 'R', 'G'], ['O', 'Y', 'Y']],
                                         [['R', 'R', 'R'], ['Y', 'B', 'O'], ['B', 'W', 'O']],
                                         [['R', 'Y', 'G'], ['W', 'Y', 'O'], ['G', 'G', 'O']]])
        rubic_moved = cube.Cube(initial_state=[[['Y', 'B', 'Y'], ['W', 'G', 'R'], ['W', 'B', 'G']],
                                                [['G', 'R', 'B'], ['G', 'O', 'Y'], ['W', 'O', 'W']],
                                                [['O', 'Y', 'R'], ['R', 'Y', 'W'], ['B', 'G', 'Y']],
                                                [['W', 'B', 'B'], ['B', 'R', 'G'], ['O', 'Y', 'Y']],
                                                [['R', 'O', 'R'], ['Y', 'W', 'O'], ['B', 'G', 'O']],
                                                [['R', 'W', 'G'], ['W', 'B', 'O'], ['G', 'R', 'O']]])
        rubic.move("M'")
        self.assertTrue(rubic == rubic_moved)

    def test_move_M_double(self):
        rubic = cube.Cube(initial_state=[[['Y', 'G', 'Y'], ['W', 'W', 'R'], ['W', 'O', 'G']],
                                         [['G', 'R', 'B'], ['G', 'O', 'Y'], ['W', 'O', 'W']],
                                         [['O', 'B', 'R'], ['R', 'G', 'W'], ['B', 'B', 'Y']],
                                         [['W', 'B', 'B'], ['B', 'R', 'G'], ['O', 'Y', 'Y']],
                                         [['R', 'R', 'R'], ['Y', 'B', 'O'], ['B', 'W', 'O']],
                                         [['R', 'Y', 'G'], ['W', 'Y', 'O'], ['G', 'G', 'O']]])
        rubic_moved = cube.Cube(initial_state=[[['Y', 'Y', 'Y'], ['W', 'Y', 'R'], ['W', 'G', 'G']],
                                                 [['G', 'R', 'B'], ['G', 'O', 'Y'], ['W', 'O', 'W']],
                                                 [['O', 'W', 'R'], ['R', 'B', 'W'], ['B', 'R', 'Y']],
                                                 [['W', 'B', 'B'], ['B', 'R', 'G'], ['O', 'Y', 'Y']],
                                                 [['R', 'B', 'R'], ['Y', 'G', 'O'], ['B', 'B', 'O']],
                                                 [['R', 'G', 'G'], ['W', 'W', 'O'], ['G', 'O', 'O']]])
        rubic.move("M2")
        self.assertTrue(rubic == rubic_moved)

    def test_double_colour_on_edge(self):
        rubic = cube.Cube(initial_state=[[['Y', 'R', 'Y'], ['W', 'W', 'G'], ['W', 'O', 'G']],
                                         [['G', 'R', 'B'], ['G', 'O', 'Y'], ['W', 'O', 'W']],
                                         [['O', 'B', 'R'], ['R', 'G', 'W'], ['B', 'B', 'Y']],
                                         [['W', 'B', 'B'], ['B', 'R', 'G'], ['O', 'Y', 'Y']],
                                         [['R', 'R', 'R'], ['Y', 'B', 'O'], ['B', 'W', 'O']],
                                         [['R', 'Y', 'G'], ['W', 'Y', 'O'], ['G', 'G', 'O']]])
        self.assertFalse(rubic.is_cube_correct_set())

    def test_double_colour_on_corner(self):
        rubic = cube.Cube(initial_state=[[['B', 'G', 'Y'], ['W', 'W', 'R'], ['W', 'O', 'G']],
                                         [['G', 'R', 'B'], ['G', 'O', 'Y'], ['W', 'O', 'W']],
                                         [['O', 'B', 'R'], ['R', 'G', 'W'], ['B', 'B', 'Y']],
                                         [['W', 'B', 'Y'], ['B', 'R', 'G'], ['O', 'Y', 'Y']],
                                         [['R', 'R', 'R'], ['Y', 'B', 'O'], ['B', 'W', 'O']],
                                         [['R', 'Y', 'G'], ['W', 'Y', 'O'], ['G', 'G', 'O']]])
        self.assertFalse(rubic.is_cube_correct_set())

if __name__ == '__main__':
    unittest.main()

