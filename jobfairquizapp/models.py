from django.db import models

class UserDetails(models.Model):
    sno = models.AutoField(primary_key=True)  # Serial Number (Auto increment)
    name = models.CharField(max_length=100)  # Name of the participant
    clg_name = models.CharField(max_length=150)  # College name
    phone_number = models.CharField(max_length=10, unique=True)  # Unique phone number (limited to 10 digits)
    email = models.EmailField(unique=True)  # Unique email address

    def __str__(self):
        return self.name

class QuizQuestion(models.Model):  # Renamed to QuizQuestion
    question = models.TextField()  # The quiz question
    answer = models.CharField(max_length=255)  # The correct answer
    option_1 = models.CharField(max_length=255)  # Option 1
    option_2 = models.CharField(max_length=255)  # Option 2
    option_3 = models.CharField(max_length=255)  # Option 3
    option_4 = models.CharField(max_length=255)  # Option 4

    class Meta:
        verbose_name = 'Quiz Question'
        verbose_name_plural = 'Quiz Questions'

    def __str__(self):
        return f"Question: {self.question}"


class UserDetailsMark(models.Model):
    email = models.EmailField(unique=True)  # Unique email address for the user
    total_marks = models.IntegerField(default=0)  # Total marks obtained by the user

    class Meta:
        verbose_name = 'User Detail'
        verbose_name_plural = 'User Details'

    def __str__(self):
        return f"Email: {self.email}, Total Marks: {self.total_marks}"