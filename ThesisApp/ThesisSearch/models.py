from django.db import models

class Thesis(models.Model):
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    author = models.CharField(max_length=100)
    supervisor = models.CharField(max_length=100)
    year_published = models.IntegerField()
    keywords = models.ManyToManyField('Keyword', related_name='theses')

    def __str__(self):
        return self.title
    
class Keyword(models.Model):
    word = models.CharField(max_length=50)

    def __str__(self):
        return self.word