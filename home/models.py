from django.db import models

# Create your models here.
class Film (models.Model):

    id = models.CharField('id', primary_key=True, max_length = 12)
    original_title = models.CharField('titre original', max_length = 255)
    french_title = models.CharField('titre français', max_length = 255)
    romanized_title = models.CharField('titre romanisé', max_length = 255)
    country = models.CharField('Pays d\'origine', max_length = 255)
    language = models.CharField('langue', max_length = 20)
    release_year = models.IntegerField('date de sortie', default = 0)
    runtime = models.IntegerField('durée', default = 0)
    genres = models.CharField('genres', max_length = 255)
    prod_comp = models.TextField('société de production', default = 'inconnu')
    prod_countries = models.CharField('pays de production', default = 'inconnu', max_length = 255)
    avg_rating = models.DecimalField('note moyenne', max_digits=2, decimal_places=1)
    count_rating = models.BigIntegerField('nombre vote')
    directors = models.CharField('réalisateurs', default = 'inconnu', max_length = 255)
    writers = models.CharField('scénaristes', default = 'inconnu', max_length = 255)
    poster = models.CharField('poster_path', max_length = 255)
    plot = models.TextField('résumé',default = 'inconnu')

    def __str__(self):
        return self.french_title