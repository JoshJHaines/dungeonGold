from django.db import models
from datetime import date 
import re

# validator
class UserManager(models.Manager):
    def registerValidator(self, postData):    
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        emailMatch = User.objects.filter(email=postData['email'])
        if len(postData['first_name']) == 0:
            errors['requiredName'] = "Please provide your First Name"
        if len(postData['last_name']) == 0:
            errors['requiredName'] = "Please provide your Last Name"
        if len(postData['email']) == 0:
            errors['requiredEmail'] = "Please provide your Email"
        elif not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['emailInvalid'] = "Invalid email address!"
        elif len(emailMatch) > 0:
            errors['usernameExists'] = "Username address already registered"
        if len(postData['password']) < 7:
            errors['passLen'] = "Password must be at least 8 characters"
        if postData['confirmpw'] != postData['password']:
            errors['passMatch'] = "Passwords must match"
        return errors
    def loginValidator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        emailMatch = User.objects.filter(email=postData['email'])
        if len(postData['email']) == 0:
            errors['requiredEmail'] = "Please provide your Email"
        elif not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['emailInvalid'] = "Invalid email address!"
        elif len(emailMatch) == 0:
            errors['emailNoExist'] = "Email is not registered"
        else:
            if emailMatch[0].password != postData['password']:
                errors["pwmatch"] = "Password incorrect"
        return errors
    # def tripValidator(self, postData):
    #     errors = {}
    #     today = date.today()
    #     destMatch = Destination.objects.filter(name=postData['dest_name'])
        
    #     if len(postData['dest_name']) == 0:
    #         errors['requiredDest'] = "Please provide a destination"
    #     if len(postData['dest_name']) < 3:
    #         errors['requiredDestLen'] = "Destination Name must be longer than 3 characters"
    #     elif len(destMatch) > 0:
    #         errors['destExists'] = "Destination already exists"
    #     if len(postData['description']) == 0:
    #         errors['requiredDesc'] = "Please provide a description"
    #     if postData['trav_start_date'] < str(today):
    #         errors['today'] = "Please select a Start Date after today."
    #     if postData['trav_end_date'] < postData['trav_start_date']:
    #         errors['today'] = "Please select an End Date after The Start Date."
    #     return errors
    # def updateTripValidator(self, postData):
    #     errors = {}
    #     today = date.today()
    #     destMatch = Destination.objects.filter(name=postData['dest_name'])
        
    #     if len(postData['dest_name']) == 0:
    #         errors['requiredDest'] = "Please provide a destination"
    #     if len(postData['dest_name']) < 3:
    #         errors['requiredDestLen'] = "Destination Name must be longer than 3 characters"
    #     if len(postData['description']) == 0:
    #         errors['requiredDesc'] = "Please provide a description"
    #     if postData['trav_start_date'] < str(today):
    #         errors['today'] = "Please select a Start Date after today."
    #     if postData['trav_end_date'] < postData['trav_start_date']:
    #         errors['today'] = "Please select an End Date after The Start Date."
    #     return errors

class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Campaign(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    created_by = models.ForeignKey(User, related_name="creator", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Character(models.Model):
    character_name = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, related_name="user", on_delete = models.CASCADE)
    campaign = models.ForeignKey(User, related_name="campaign", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Transactions(models.Model):
    character = models.ForeignKey(Character, related_name="character", on_delete = models.CASCADE)
    income = models.BooleanField(default=False)
    platinum = models.IntegerField()
    gold = models.IntegerField()
    electrum = models.IntegerField()
    silver = models.IntegerField()
    copper = models.IntegerField()
    notes = models.TextField(max_length=250)
    trans_date = models.DateTimeField(auto_now_add=True)