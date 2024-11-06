from django.db import models
class CurdPro(models.Model):
    roll_no=models.IntegerField(default=0)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.BigIntegerField()
    percentage=models.IntegerField()
    year=models.IntegerField()
    location=models.CharField(max_length=50)
    college=models.CharField(max_length=50)
    university=models.CharField(max_length=50)

