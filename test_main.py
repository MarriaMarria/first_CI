import unittest
# !!! all functions in test must start with TEST
# from reverse_nmb import reverse_nmb
# from reverse_str import reverse
# from num_words import count_words
from average import average
from pal import pal
# from reverse_chiffre import reverse_chiffre

class TestingFunctions(unittest.TestCase):

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

    # def test_palindrome(self):
    #     y = "elle"
    #     self.assertTrue(pal(y), False)
    #     self.assertTrue(pal(y), True)

    def test_palindrome(self):
        self.assertFalse(pal("hell"))
        self.assertTrue(pal("alla"))


    # #Test que le fichier exist
    # def test_check_file_exist_main(self):
    #     directory_path = './main.py' # somepath
    #     self.assertTrue(os.path.exists(directory_path)) 

    # def test_number_of_words(self):
    # self.assertEqual(num_of_words("Jojo is the best"), "4 words")
    # self.assertEqual(num_of_words(1), "Not an valid word")

if __name__ == '__main__':
    unittest.main(verbosity=2)