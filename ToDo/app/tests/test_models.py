from django.test import TestCase
from app.models import User, Task, Priority, Status
from django.core import serializers
import json

class TestModels(TestCase):
    @classmethod
    def setUpTestData(self):
        test_data  = [  {"model": "app.priority", "pk": 1, "fields": {"name": "Low"}}, 
                        {"model": "app.priority", "pk": 2, "fields": {"name": "Normal"}}, 
                        {"model": "app.priority", "pk": 3, "fields": {"name": "High"}}, 
                        {"model": "app.status", "pk": 1, "fields": {"name": "Complete"}}, 
                        {"model": "app.status", "pk": 2, "fields": {"name": "Working"}}, 
                        {"model": "app.status", "pk": 3, "fields": {"name": "Uninitiated"}}
                     ]
        for obj  in serializers.deserialize("json", json.dumps(test_data)):
            obj .save()
        self.priority =  Priority.objects.get(pk = 1)
        self.status =  Status.objects.get(pk = 1)
    
    def setUp(self):
        self.user = User.objects.create(email = 'test@gmail.com', password = '12345')
        self.task = Task.objects.create(user = self.user, title = 'my_title', date = '2021-07-04', priority = self.priority, status = self.status)

    def test_user_creation(self):
        self.assertEqual(self.user.__str__(), 'email=test@gmail.com, password=12345')

    def test_task_creation(self):
        self.assertEqual(self.task.__str__(), 'name=my_title, user_email=test@gmail.com')