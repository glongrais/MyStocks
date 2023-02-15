from django.db import models

class Stock(models.Model):
    symbol = models.CharField("Symbol", max_length=20, primary_key=True)
    name = models.CharField("Name", max_length=240)
    currentPrice = models.FloatField("CurrentPrice")
    previousClose = models.FloatField("PreviousClose")
    sector = models.CharField("Sector", max_length=50)
    dividendYield = models.FloatField("DividendYield")
    logoUrl = models.CharField("LogoURL", max_length=240)

    def __str__(self):
        return self.name
