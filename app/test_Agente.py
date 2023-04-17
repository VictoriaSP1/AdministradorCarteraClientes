from rest_framework.test import APITestCase, APIRequestFactory
from .models import Agente
from django.urls import reverse
from rest_framework import status

# Create your tests here.

class TestAgente(APITestCase):
   
    
    def URLBase(self):
        url = f'/API/Agente/'
        return url
    
    def URLObjeto(self):
        url = f'/API/Agente/1/'
        return url
    
    def Data (self):
        data= {
            
            "Nombre_Agente":"Esther Arriaga",
            "Email":"EstherArriaga09@outlook.com",
            "Password":"899278123"
        }
        return data
    
    def DataModificada(self):
        data= {
            
            "Nombre_Agente":"Esther Arri",
            "Email":"EstherArri09@outlook.com",
            "Password":"8992781233"
        }
        return data

    def test_API_GET(self):
        response = self.client.get(self.URLBase())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_API_POST(self):
        response = self.client.post(self.URLBase(), self.Data())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_API_PUT(self):

        self.client.post(self.URLBase(), self.Data())
        response = self.client.put(self.URLObjeto(), self.DataModificada())
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_API_DELETE(self):

        self.client.post(self.URLBase(), self.Data())
        response = self.client.delete(self.URLObjeto())
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    