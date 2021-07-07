from django.test import TestCase, Client
from django.urls import reverse
from app.models import User, Task, Priority, Status
from django.core import serializers
import json


class TestViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_data  = [  {"model": "app.priority", "pk": 1, "fields": {"name": "Low"}}, 
                        {"model": "app.priority", "pk": 2, "fields": {"name": "Normal"}}, 
                        {"model": "app.priority", "pk": 3, "fields": {"name": "High"}}, 
                        {"model": "app.status", "pk": 1, "fields": {"name": "Complete"}}, 
                        {"model": "app.status", "pk": 2, "fields": {"name": "Working"}}, 
                        {"model": "app.status", "pk": 3, "fields": {"name": "Uninitiated"}}
                     ]
        for obj  in serializers.deserialize("json", json.dumps(test_data)):
            obj .save()

        cls.user_object = User.objects.create(email = 'test@gmail.com', password = '12345')
        cls.priority_object =  Priority.objects.get(pk = 1)
        cls.status_object =  Status.objects.get(pk = 1)
        cls.task_object = Task.objects.create(user = cls.user_object, title = 'my_title', date = '2021-07-04', priority = cls.priority_object, status = cls.status_object)

    def setUp(self):
        self.client = Client()
        self.base = reverse('index')
        self.user = reverse('user')
        self.user_list = reverse('users')
        self.task_list_base = reverse('tasks', kwargs={'user_id': self.user_object.id, 'task_id': 0})
        self.task_list = reverse('tasks', kwargs={'user_id': self.user_object.id, 'task_id': self.task_object.id})
        self.add_task = reverse('add', kwargs={'user_id': self.user_object.id})
        self.delete_task = reverse('delete', kwargs={'user_id': self.user_object.id, 'task_id': self.task_object.id})
        self.edit_task = reverse('edit', kwargs={'user_id': self.user_object.id, 'task_id': self.task_object.id})
    
    def test_user(self):
        response = self.client.get(self.base)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user.html')

        response = self.client.post(self.user, {'email': 'test@gmail.com', 'password': '12345'})
        self.assertEquals(response.status_code, 302)

        response = self.client.post(self.user, {'email': 'test@gmail.com', 'password': '123456'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user.html')

        response = self.client.post(self.user, {'email': 'test_2@gmail.com', 'password': '12345'})
        self.assertEquals(response.status_code, 302)

        response = self.client.post(self.user, {'email': '', 'password': '12345'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user.html')

    def test_user_list(self):
        response = self.client.get(self.user_list)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users.html')
    
    def test_task_list(self):        
        response = self.client.get(self.task_list_base)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks.html')
        
        response = self.client.get(self.task_list)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks.html')
    
    def test_add_task(self):
        response = self.client.post(self.add_task, {'title': 'ADDED', 'date': '', 'priority': self.priority_object.id, 'status': self.status_object.id})
        self.assertEquals(response.status_code, 302)

        response = self.client.post(self.add_task, {'title': 'ADDED', 'date': '2021-07-04', 'priority': self.priority_object.id, 'status': self.status_object.id})
        self.assertEquals(response.status_code, 302)
    
    def test_delete_task(self):
        response = self.client.post(self.delete_task)
        self.assertEquals(response.status_code, 302)
    
    def test_edit_task(self):
        response = self.client.get(self.edit_task)
        self.assertEquals(response.status_code, 302)

        response = self.client.post(self.edit_task, {'title': 'EDITED', 'date': '', 'priority': self.priority_object.id, 'status': self.status_object.id})
        self.assertEquals(response.status_code, 302)    

        response = self.client.post(self.edit_task, {'title': 'EDITED', 'date': '2021-07-04', 'priority': self.priority_object.id, 'status': self.status_object.id})
        self.assertEquals(response.status_code, 302)        
