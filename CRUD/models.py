from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.


CITY = (
    ('New Delhi', 'New Delhi'),
    ('Bangalore', 'Bangalore'),
    ('Mumbai', 'Mumbai'),
    ('Chennai', 'Chennai'),
    ('Kolkata', 'Kolkata'),
    ('Patna', 'Patna'),
    ('Pune', 'Pune '),
    ('Hyderabad', 'Hyderabad'),
    ('Bhubaneswar', 'Bhubaneswar'),
    ('Kochi', 'Kochi'),
    ('Lucknow', 'Lucknow'),
    ('Ahmedabad', 'Ahmedabad'),
)

class Employees(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=100)
    Address = models.TextField()
    Phone = models.BigIntegerField()
    City = models.CharField(max_length=20, choices=CITY)
    Gender = models.CharField(max_length=100)
    Images = models.FileField(upload_to="image/%Y/%m/", validators=[FileExtensionValidator(['pdf', 'doc', 'svg', 'jpg', 'png','jpeg'])])
    Resume = models.FileField(upload_to="resume/%Y/%m/", validators=[FileExtensionValidator(['pdf', 'doc', 'svg', 'jpg', 'png','jpeg'])])
    

    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;" >'.format(self.Images))

    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;" >'.format(self.Resume))

    def __str__(self):
        return '%s' % (self.Name)