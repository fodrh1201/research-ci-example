import unittest

import main

class MainTest(unittest.TestCase):
    def test_helloworld(self):
        ret = main.hellowworld("Test")
        self.assertEqual(ret, "Hello World! Chris!")

        
if __name__ == "__main__":
    unittest.main()