from django.db import models

class Stock(models.Model):
    symbol = models.CharField("Symbol", max_length=20)
    name = models.CharField("Name", max_length=240)
    currentPrice = models.FloatField("CurrentPrice")
    previousClose = models.FloatField("PreviousClose")
    sector = models.CharField("Sector", max_length=50)
    dividendYield = models.FloatField("DividendYield")
    logoUrl = models.CharField("LogoURL", max_length=240)

    def __str__(self):
        return self.name

class StockHolding(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    shares = models.PositiveIntegerField()
    purchase_date = models.DateField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.stock.name
