import datetime

from django.db import models
from django.utils import timezone

class Topic(models.Model):
    topic_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.topic_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)