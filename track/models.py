from django.db import models

class HoldingType(models.Model):
    name = models.CharField(max_length=20)
    # equity, bond, ...
    EQ = 'EQ'
    BD = 'BD'
    ASSET_CLASS_CHOICES = ((EQ, 'equity'), (BD, 'bond'))
    asset_class = models.CharField(max_length=2,
                                   choices=ASSET_CLASS_CHOICES)
    # CA, US, INTL
    CA = 'CA'
    US = 'US'
    INTL = 'IN'
    COUNTRY_CHOICES = ((CA, 'CA'), (US, 'US'), (INTL, 'IN'))
    country = models.CharField(max_length=2,
                               choices=COUNTRY_CHOICES)
    def __unicode__(self):
        return "[{0.name}] {0.asset_class}/{0.country}".format(self)

class AllocationRule(models.Model):
    percent = models.DecimalField(max_digits=4,decimal_places=2)
    holding = models.ForeignKey('HoldingType')
    def __unicode__(self):
        return "{0} @ {1}%".format(self.holding, self.percent)