from app import app
import unittest


class TestMyGeneSearch(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_name_and_species(self):
        """Tests the name and species"""
        response = self.app.get('/searchgene/?name=tbpl2&species=amphilophus_citrinellus', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_species(self):
        """Tests if only species is given"""
        response = self.app.get('/searchgene/?species=amphilophus_citrinellus', follow_redirects=True)
        self.assertEqual(response.status_code, 400)

    def test_name_less_than_three(self):
        """Tests if the number of letters are less than three in name"""
        response = self.app.get('/searchgene/?name=tb', follow_redirects=True)
        self.assertEqual(response.status_code, 400)

    def test_no_name_and_species(self):
        """Tests if no query strings are given"""
        response = self.app.get('/searchgene/', follow_redirects=True)
        self.assertEqual(response.status_code, 400)

    def test_name_double(self):
        """Only the first parameter will be considered if double name parameters are entered"""
        response = self.app.get('/searchgene/?name=tbpl2&name=brc', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_name(self):
        """Tests if only name is given"""
        response = self.app.get('/searchgene/?name=tbpl2', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_wrong_name(self):
        """Tests if name query string is wrong only"""
        response = self.app.get('/searchgene/?value=tbpl2', follow_redirects=True)
        self.assertEqual(response.status_code, 400)

    def test_wrong_name_and_correct_species(self):
        """Tests if name query string is wrong and species is correct"""
        response = self.app.get('/searchgene/?value=tbpl2&species=amphilophus_citrinellus', follow_redirects=True)
        self.assertEqual(response.status_code, 400)

    def test_wrong_name_and_species(self):
        """Tests if name and species query strings are wrong"""
        response = self.app.get('/searchgene/?value=tbpl2&record=amphilophus_citrinellus', follow_redirects=True)
        self.assertEqual(response.status_code, 400)

    def test_correct_name_and_wrong_species(self):
        """Tests if name query strings is correct and species query string is wrong"""
        response = self.app.get('/searchgene/?name=tbpl2&record=amphilophus_citrinellus', follow_redirects=True)
        self.assertEqual(response.status_code, 400)

    def test_no_matches(self):
        """Tests if there are no matches found in the database"""
        response = self.app.get('/searchgene/?name=brc&species=amphilophus_citrinellus', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        """Tests if method is post"""
        response = self.app.post('/searchgene/', follow_redirects=True)
        self.assertEqual(response.status_code, 405)

    def test_delete(self):
        """Tests if method is delete"""
        response = self.app.delete('/searchgene/', follow_redirects=True)
        self.assertEqual(response.status_code, 405)

    def test_put(self):
        """Tests if method is put"""
        response = self.app.put('/searchgene/', follow_redirects=True)
        self.assertEqual(response.status_code, 405)

    def test_patch(self):
        """Only the first parameter will be considered if double name parameters are entered"""
        response = self.app.patch('/searchgene/', follow_redirects=True)
        self.assertEqual(response.status_code, 405)

    if __name__ == "__main__":
        unittest.main()
