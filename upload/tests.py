from django.test import TestCase
from upload.models import Homework
from django.contrib.auth.models import User,Group
import datetime

# Create your tests here.
class SimpleTest(TestCase):
    def setUp(self):
        print("SetUp")
        User.objects.create_user(username='test',password='test').save()
        Group.objects.create(name='Student').save()

    def test_success_register(self):
        response = self.client.post('/register/',{'Username':'testUser','Password':'password','ConfirmPass':'password'})

    def fail_register_test(self):
        response = self.client.post('/register/',{'Username':'testUser','Password':'password','ConfirmPass':'password1'})
        self.assertEqual(response.content,'Passwords do not match!')

    def success_login_test(self):
        response = self.client.post('',{'Username':'testUser','Password':'password'},follow=True)
        self.assertEqual(response.template,'Account.html')

    def fail_login_test(self):
        response = self.client.post('',{'Username':'testUser','Password':'password'})
        self.assertEqual(response.content,'Login Failed!')

    def upload_success_test(self):
        Homework.objects.create(Description='test',Deadline=datetime.datetime.now(),Status='False',Number='1')
        with open('test.txt') as fp:
            response = self.client.post(('/upload_file/',{'file',fp}))
            self.assertEqual(response.json()['status'],'1')