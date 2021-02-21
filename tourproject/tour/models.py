from django.db import models

# Create your models here.

class TrekDestination(models.Model):
    DESTINATIONS = (
        ('Langtang', 'Langtang'),
        ('Annapurna Circuit', 'Annapurna Circuit'),
        ('Everest Base Camp', 'Everest Base Camp'),
        ('Ghorepani Poon Hill', 'Ghorepani Poon Hill'),
        ('Upper Mustang', 'Upper Mustang'),
    )
    name = models.CharField(max_length=200, null=True, choices=DESTINATIONS)

    def __str__(self):
        return self.name
