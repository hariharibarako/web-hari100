import datetime

from django.db import models
from django.utils import timezone

class Topic(models.Model):
    genre= models.CharField(max_length=100, default='Everyday', choices=(('IT','IT'),('Accountant', 'Accountant'),('Everyday', 'Everyday'), ('Eye', 'Eye')))
    title= models.CharField(max_length=100, default='')
    topic_text = models.TextField(default='')
    pub_date = models.DateTimeField('date published')
    nice = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)