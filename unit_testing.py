import unittest
import os.path
import json

class TestJSONCreation(unittest.TestCase):
	
	def test_JSON_file_exists(self):
		#Pass test.json instead 
		file = 'result.json'
		self.assertTrue(os.path.exists(f'{file}'))

	def test_json_content(self):
		f = open('result.json')
		data = json.load(f)
		f.close()

		self.assertEqual(data['Province_State']['0'], 'Alabama' )

if __name__ == '__main__':
    unittest.main()