import datetime

from django.db import models
from django.utils import timezone

choices = (('IT(その他)','IT(その他)'),('Accountant', 'Accountant'),('Everyday', 'Everyday'), ('Eye', 'Eye'), ('ハリネズミ', 'ハリネズミ'), ('Python(Django)','Python(Django)'), ('Swift', 'Swift'))

class Topic(models.Model):

    genre= models.CharField(max_length=100, default='Everyday', choices=choices)
    title= models.CharField(max_length=100, default='')
    topic_text = models.TextField(default='')
    pub_date = models.DateTimeField('date published')
    nice = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)