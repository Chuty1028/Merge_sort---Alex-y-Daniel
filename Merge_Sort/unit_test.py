import unittest
from merge_of_TwoLists import merge_sort, merge

class TestMerge(unittest.TestCase):

    def test_merge_normal(self):
        self.assertEqual(merge([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])

    def test_merge_izquierda_vacia(self):
        self.assertEqual(merge([], [1, 2, 3]), [1, 2, 3])

    def test_merge_derecha_vacia(self):
        self.assertEqual(merge([1, 2, 3], []), [1, 2, 3])

    def test_merge_ambas_vacias(self):
        self.assertEqual(merge([], []), [])

    def test_merge_un_elemento_cada_una(self):
        self.assertEqual(merge([1], [2]), [1, 2])


class TestMergeSort(unittest.TestCase):

    def test_lista_normal(self):
        self.assertEqual(merge_sort([5, 2, 8, 1, 9]), [1, 2, 5, 8, 9])

    def test_lista_vacia(self):
        self.assertEqual(merge_sort([]), [])

    def test_un_elemento(self):
        self.assertEqual(merge_sort([7]), [7])

    def test_duplicados(self):
        self.assertEqual(merge_sort([3, 1, 3, 2]), [1, 2, 3, 3])

    def test_ya_ordenada(self):
        self.assertEqual(merge_sort([1, 2, 3, 4]), [1, 2, 3, 4])

if __name__ == "__main__":
    unittest.main()