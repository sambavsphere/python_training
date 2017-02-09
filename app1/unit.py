from app import operations
import unittest
class test1(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print "Log in to app/product"
		cls.user="samba"
	@classmethod
	def tearDownClass(cls):
		print "Logout fromt the product/app"
		cls.user=None


	def setUp(self):
		print "pre configuration for every test case"
	def tearDown(self):
		print "post configuration for every test case"

	def test_1_10_20(self):
		print "test_10_20",self.user
		obj = operations(10,20)
		exp_res = 200
		act_res = obj.mul()
		error = "test_10_20 failed: expecting:{0} got :{1}".format(exp_res,act_res)
		self.assertTrue(exp_res==act_res, error)

	def test_2_str_4(self):
		print "test_str_4"
		obj = operations("s",4)
		exp_res = "ssss"
		act_res = obj.mul()
		error = "test_str_4 failed: expecting:{0} got :{1}".format(exp_res,act_res)
		self.assertTrue(exp_res==act_res, error)
	def test_3_s1_s2(self):
		print "test_s1_s2"
		obj = operations('s1','s2')
		exp_res = None
		act_res = obj.mul()
		error = "test_s1_s2 failed: expecting:{0} got :{1}".format(exp_res,act_res)
		self.assertTrue(exp_res==act_res, error)
if __name__ == "__main__":	
	unittest.main()