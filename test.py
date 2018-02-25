#!/usr/bin/python
import unittest
import cpu_data_reader

class test_cpu_desc_parser(unittest.TestCase):
    def test_intel(self):
        input = 'Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz [Family 6 Model 142 Stepping 9]'
        expected = {
            'Make': 'Intel(R)',
            'Name': 'Core(TM) i7-7500U CPU',
            'Frequency': '2.70GHz',
            'Family': '6',
            'Model': '142',
            'Steppping': '9',
            'original_text': input
        }
        found = cpu_data_reader.parse_cpu_description(input)
        self.assertEqual(found, expected)

    def test_amd(self):
        input = 'AMD FX(tm)-9590 Eight-Core Processor [Family 21 Model 2 Stepping 0]'
        expected = {
            'Make': 'AMD',
            'Name': 'FX(tm)-9590 Eight-Core Processor',
            'Frequency': None,
            'Family': '21',
            'Model': '2',
            'Steppping': '0',
            'original_text': input
        }
        found = cpu_data_reader.parse_cpu_description(input)
        self.assertEqual(found, expected)

    def test_trash(self):
        input = 'trash trash trash'
        expected = {
            'Make': None,
            'Name': None,
            'Frequency': None,
            'Family': None,
            'Model': None,
            'Steppping': None,
            'original_text': input
        }
        found = cpu_data_reader.parse_cpu_description(input)
        self.assertEqual(found, expected)

if __name__ == '__main__':
    unittest.main()
