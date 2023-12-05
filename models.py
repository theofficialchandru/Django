from django.db import models

# Create your models here.

class Book_management(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    genre=models.CharField(max_length=100)
    ISBN=models.IntegerField()
    availabity=models.BooleanField()
    def __str__(self):
        return f'{self.title}'

class Patron_management(models.Model):
    library_id=models.IntegerField()
    name=models.CharField(max_length=50)
    contact_information=models.IntegerField()
    membership_details=models.BooleanField()
    def __str__(self):
        return f'{self.name}'


class Book_Borrowing(models.Model):
    title=models.ForeignKey(Book_management,on_delete=models.CASCADE)
    name=models.ForeignKey(Patron_management,on_delete=models.CASCADE)
    borrowing_date=models.DateField()
    due_dates=models.DateField()
    def __str__(self):
        return f'{self.title}===>{self.name} ===>>{self.borrowing_date}===>{self.due_dates}'

