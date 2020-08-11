from django.core.validators import URLValidator
from djongo import models


# classe permettant d'ajouter un circuit sur le site
class Accueil(models.Model):
    # données pour la page d'accueil
    title = models.CharField(max_length=100, default="", verbose_name="Nom du parcours")
    resume = models.TextField(verbose_name="Petit résumé")
    # données pour la page du circuit
    description = models.TextField(verbose_name="Description générale")
    map_url_data = models.TextField(validators=[URLValidator()])
    # , path="/img"
    image = models.ImageField(blank=True)
    qr_code = models.ImageField(blank=True)

    # nom du champ dans l'interface d'admin
    class Meta:
        # abstract = True
        verbose_name = "Parcours"
        verbose_name_plural = "Parcours"

    def __unicode__(self):
        return self.title
