from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length = 15)

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length = 15)
    isCategory = models.BooleanField(default = False, verbose_name = "is category")
    
    def __unicode__(self):
        return self.name

class Term(models.Model):
    englishVersion = models.CharField(max_length = 30)
    czechVersion = models.CharField(max_length = 30)

    description = models.TextField(blank = True)
    
    tags = models.ManyToManyField(Tag, blank = True)
    subject = models.ForeignKey(Subject)

    def __unicode__(self):
        return self.englishVersion


    
