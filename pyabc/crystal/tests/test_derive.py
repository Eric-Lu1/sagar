import unittest

from pyabc.crystal.structure import Cell
from pyabc.crystal.derive import ConfigurationGenerator as CG


class TestDerive(unittest.TestCase):

    def setUp(self):
        fcc_latt = [0, 5, 5,
                    5, 0, 5,
                    5, 5, 0]
        fcc_pos = [(0, 0, 0), (0.5, 0.5, 0.5)]
        fcc_atoms = [1, 2]
        self.fcc_pcell = Cell(fcc_latt, fcc_pos, fcc_atoms)

    def test_conf_non_redun(self):
        # 最大体积下可能产生的所有结构的总和，不包含超胞。
        wanted = [2, 4, 10, 29]
        got = []
        cg = CG(self.fcc_pcell)
        for v in [1, 2, 3, 4]:
            con = cg.cons_max_volume([[1, 5], [2]], v)
            got.append(len([i for i in con]))

        self.assertEqual(got, wanted)

    def test_confs_nondup_specific_volume(self):
        # confs_nondup_specific_volume(fcc_pcell, [[1, 5]], 5)
        wanted = [2, 6, 12, 41]
        got = []
        cg = CG(self.fcc_pcell)
        for v in [1, 2, 3, 4]:
            con = cg.cons_specific_volume([[1, 5], [2]], v)
            got.append(len([i for i in con]))

        self.assertEqual(got, wanted)

    # def test_degeneracy_of_confs_nondup_specific_volume(self):
    #     wanted = [1, 2, 4, 16, 32]
    #     got = []
    #     for v in [1, 2, 3, 4, 5]:
    #         deg_all = 0
    #         cons = confs_nondup_specific_volume(self.fcc_pcell, [[1, 5], [2]], v)
    #         for c in cons:
    #             deg_all += c[1]
    #         print(deg_all)



if __name__ == "__main__":
    import nose2
    nose2.main()
