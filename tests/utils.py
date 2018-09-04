import unittest, os
from utils import utils

class MultiParamsTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(MultiParamsTest, self).__init__(*args, **kwargs)
        self.params = utils.MultiParams(os.path.join(os.path.dirname(__file__), 'params.json')).params

    def test_is_list(self):
        self.assertTrue(isinstance(self.params, list))
        self.assertEqual(len(self.params), 2)

    def test_multi_gpu(self):
        for i in range(len(self.params)):
            self.assertEqual(self.params[i]['multi_gpu'], i)
            self.assertEqual(self.params[i].multi_gpu, i)

    def test_exp_name(self):
        for i in range(len(self.params)):
            self.assertTrue(isinstance(self.params[i]['exp_name'], str))
            self.assertTrue(isinstance(self.params[i].exp_name, str))

if __name__ == '__main__':
    unittest.main()