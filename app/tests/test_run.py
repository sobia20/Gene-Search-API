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
        response = self.app.get('/searchgene/?name=tbpl2&species=amphilophus_citrinellus', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_species(self):
        response = self.app.get('/searchgene/?species=amphilophus_citrinellus', follow_redirects=True)
        self.assertEqual(response.status_code, 400)

    def test_name_less_than_three(self):
        response = self.app.get('/searchgene/?name=tb', follow_redirects=True)
        self.assertEqual(response.status_code, 400)

    def test_no_name_and_species(self):
        response = self.app.get('/searchgene/', follow_redirects=True)
        self.assertEqual(response.status_code, 400)

    def test_name_double(self):
        '''Only the first parameter will be considered if double name parameters are entered'''
        response = self.app.get('/searchgene/?name=tbpl2&name=brc', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_name(self):
        response = self.app.get('/searchgene/?name=tbpl2', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_wrong_name(self):
        response = self.app.get('/searchgene/?value=tbpl2', follow_redirects=True)
        self.assertEqual(response.status_code, 400)

    def test_wrong_name_and_correct_species(self):
        response = self.app.get('/searchgene/?value=tbpl2&species=amphilophus_citrinellus', follow_redirects=True)
        self.assertEqual(response.status_code, 400)

    def test_wrong_name_and_species(self):
        response = self.app.get('/searchgene/?value=tbpl2&record=amphilophus_citrinellus', follow_redirects=True)
        self.assertEqual(response.status_code, 400)

    def test_correct_name_and_wrong_species(self):
        response = self.app.get('/searchgene/?name=tbpl2&record=amphilophus_citrinellus', follow_redirects=True)
        self.assertEqual(response.status_code, 400)

    def test_no_matches(self):
        response = self.app.get('/searchgene/?name=brc&species=amphilophus_citrinellus', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        response = self.app.post('/searchgene/', follow_redirects=True)
        self.assertEqual(response.status_code, 405)

    def test_delete(self):
        response = self.app.delete('/searchgene/', follow_redirects=True)
        self.assertEqual(response.status_code, 405)

    def test_put(self):
        response = self.app.put('/searchgene/', follow_redirects=True)
        self.assertEqual(response.status_code, 405)

    def test_patch(self):
        response = self.app.patch('/searchgene/', follow_redirects=True)
        self.assertEqual(response.status_code, 405)

    if __name__ == "__main__":
        unittest.main()
