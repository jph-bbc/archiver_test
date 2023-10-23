import unittest
from functions import аrchiver, unpacker


class TestArchiver(unittest.TestCase):
    # Тест функции аrchiver при стандартном поведении
    def test_аrchiver(self):
        compressed_text = аrchiver("TTTTTeeeeeessttt 1")
        self.assertEqual(compressed_text, "T5e6s2t3 1")

    # Тест функции unpacker при стандартном поведении
    def test_unpacker(self):
        uncompressed_text = unpacker("T5e6s2t3 1")
        self.assertEqual(uncompressed_text, "TTTTTeeeeeessttt 1")

    # Тест функции аrchiver при введении одного символа
    def test_аrchiver_single_character(self):
        compressed_text = аrchiver("t")
        self.assertEqual(compressed_text, "t")

    # Тест функции unpacker при введении одного символа
    def test_unpacker_single_character(self):
        uncompressed_text = unpacker("t")
        self.assertEqual(uncompressed_text, "t")

    # Тест функции аrchiver при введении пустой строки
    def test_аrchiver_empty_string(self):
        compressed_text = аrchiver("")
        self.assertEqual(compressed_text, "Введена пустая строка")

    # Тест функции unpacker при введении пустой строки
    def test_unpacker_empty_string(self):
        uncompressed_text = unpacker("")
        self.assertEqual(uncompressed_text, "Введена пустая строка")

    # Тест функции аrchiver при введении целочисленного значения
    def test_аrchiver_non_string_input(self):
        uncompressed_text = аrchiver("123")
        self.assertEqual(uncompressed_text, "Входной текст должен быть строкой")

    # Тест функции unpacker при введении целочисленного значения
    def test_unpacker_non_string_input(self):
        uncompressed_text = unpacker("123")
        self.assertEqual(uncompressed_text, "Входной текст должен быть строкой")


if __name__ == "__main__":
    unittest.main()
