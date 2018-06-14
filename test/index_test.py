import unittest, sys, json
sys.path.insert(0, '..')
from app import app

class HTMLTemplateTestCase(unittest.TestCase):
    testy = app.test_client()

    # --- test API routes ---
    def test_api_pictures_index(self):
        response = self.testy.get('/api/pictures')
        self.assertEqual(response.status_code, 200)

        raw = response.data.decode("utf-8")
        json_data = json.loads(raw)
        result = [{'city': 'Hong Kong', 'country': 'China', 'id': 1, 'picture_url': 'https://learn-verified.s3.amazonaws.com/data-science-assets/hong-kong.png'}, {'city': 'Paris', 'country': 'France', 'id': 2, 'picture_url': 'https://learn-verified.s3.amazonaws.com/data-science-assets/paris.png'}, {'city': 'New York', 'country': 'USA', 'id': 3, 'picture_url': 'https://learn-verified.s3.amazonaws.com/data-science-assets/new-york.png'}, {'city': 'Sydney', 'country': 'Australia', 'id': 4, 'picture_url': 'https://learn-verified.s3.amazonaws.com/data-science-assets/sydney.png'}, {'city': 'San Francisco', 'country': 'USA', 'id': 5, 'picture_url': 'https://learn-verified.s3.amazonaws.com/data-science-assets/san-francisco.png'}]
        self.assertEqual(json_data, result)

    def test_api_pics_by_country(self):
        response = self.testy.get('/api/pictures/usa')
        self.assertEqual(response.status_code, 200)

        raw = response.data.decode("utf-8")
        json_data = json.loads(raw)
        result = [{'city': 'New York', 'country': 'USA', 'id': 3, 'picture_url': 'https://learn-verified.s3.amazonaws.com/data-science-assets/new-york.png'}, {'city': 'San Francisco', 'country': 'USA', 'id': 5, 'picture_url': 'https://learn-verified.s3.amazonaws.com/data-science-assets/san-francisco.png'}]
        self.assertEqual(json_data, result)

    def test_api_pics_by_id(self):
        response = self.testy.get('/api/pictures/1')
        self.assertEqual(response.status_code, 200)

        raw = response.data.decode("utf-8")
        json_data = json.loads(raw)
        result = {'city': 'Hong Kong', 'country': 'China', 'id': 1, 'picture_url': 'https://learn-verified.s3.amazonaws.com/data-science-assets/hong-kong.png'}
        self.assertEqual(json_data, result)


    # --- test HTML routes ---
    def test_pictures_index_html(self):
        response = self.testy.get('/pictures')
        self.assertEqual(response.status_code, 200)

        result = response.data.decode("utf-8")
        hk = '<h3>Hong Kong, China</h3>'
        pf = '<h3>Paris, France</h3>'
        nyc = '<h3>New York, USA</h3>'
        sa = '<h3>Sydney, Australia</h3>'
        sf = '<h3>San Francisco, USA</h3>'
        self.assertTrue(hk in result)
        self.assertTrue(pf in result)
        self.assertTrue(nyc in result)
        self.assertTrue(sa in result)
        self.assertTrue(sf in result)

    def test_pictures_by_id_html(self):
        response = self.testy.get('/pictures/1')
        self.assertEqual(response.status_code, 200)

        result = response.data.decode("utf-8")
        hk = '<h3>Hong Kong, China</h3>'
        self.assertTrue(hk in result)

    def test_pictures_by_country(self):
        response = self.testy.get('/pictures/usa')
        self.assertEqual(response.status_code, 200)

        result = response.data.decode("utf-8")
        nyc = '<h3>New York, USA</h3>'
        sf = '<h3>San Francisco, USA</h3>'
        self.assertTrue(nyc in result)
        self.assertTrue(sf in result)
