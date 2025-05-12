from django.test import TestCase
from django.urls import reverse
import json

class PredictDiseaseTestCase(TestCase):
    def test_predict_disease(self):
        url = reverse('predict_disease')

        data = {
            'age': 30,
            'gender': 1,
            'diabetes': 0,
            'diabetes_type': 1,
            'diarrhoea': 0,
            'short_stature': 0,
            'sticky_stool': 0,
            'weight_loss': 0,
            'iga': 0,
            'igg': 0,
            'igm': 0
        }

        response = self.client.post(url, json.dumps(data), content_type='application/json')
        
        # Verifica que el código de estado sea 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Verifica que la predicción esté en el cuerpo de la respuesta
        self.assertIn('prediction', response.json())
