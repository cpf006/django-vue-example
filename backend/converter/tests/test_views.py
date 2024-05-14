from django.test import TestCase
from django.urls import reverse

class NumToEnglishAPITests(TestCase):
    def test_get_num_to_english(self):
        response = self.client.get(reverse('num_to_english') + '?number=123')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {"status": "ok", "num_in_english": "one hundred twenty three"})

    def test_post_num_to_english(self):
        response = self.client.post(reverse('num_to_english'), {'number': '123'}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {"status": "ok", "num_in_english": "one hundred twenty three"})

    def test_invalid_input_get(self):
        response = self.client.get(reverse('num_to_english') + '?number=abc')
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {"status": "error", "message": "Invalid input"})

    def test_invalid_input_post(self):
        response = self.client.post(reverse('num_to_english'), {'number': 'abc'}, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {"status": "error", "message": "Invalid input"})

    def test_missing_number_post(self):
        response = self.client.post(reverse('num_to_english'), {}, content_type='application/json')
        self.assertEqual(response.status_code, 405)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {"status": "error", "message": "Method not allowed or number parameter missing"})
