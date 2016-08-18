import unittest
import foobar

class foobarTests(unittest.TestCase):
    def setUp(self):
        pass

    def roundtrip(self):
        val= 5
        f= foobar.Foobar(val)
        self.assertEquals(val, f.get())

if __name__ == '__main__':
    unittest.main()
