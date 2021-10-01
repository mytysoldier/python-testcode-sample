import unittest
import sample

class SampleTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOk(self):
        self.assertEqual("ゼロです。", sample.fizzbuzz(0))
    
    def testNg(self):
        self.assertNotEquals("ゼロです。", sample.fizzbuzz(1))

if __name__ == "__main__":
    unittest.main()