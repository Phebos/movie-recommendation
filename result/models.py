from django.db import models

# Create your models here.
class Vote (models.Model):

    id = models.CharField('id', primary_key=True, max_length = 12)
    original_title = models.CharField('titre original', max_length = 255)
    french_title = models.CharField('titre français', max_length = 255)
    vote_count = models.IntegerField('vote', default = 0)

    def __str__(self):
        return self.french_title