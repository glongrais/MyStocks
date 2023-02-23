from django.db import models

class Stock(models.Model):
    symbol = models.CharField("Symbol", max_length=20)
    name = models.CharField("Name", max_length=240)
    currentPrice = models.DecimalField(max_digits=10, decimal_places=2)
    previousClose = models.DecimalField(max_digits=10, decimal_places=2)
    sector = models.CharField("Sector", max_length=50)
    dividendYield = models.DecimalField(max_digits=10, decimal_places=2)
    logoUrl = models.CharField("LogoURL", max_length=240)

    def __str__(self):
        return self.name

class StockHolding(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    shares = models.PositiveIntegerField()
    purchasePrice = models.DecimalField(max_digits=10, decimal_places=2)
    desiredPercentage = models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self):
        return self.stock.name
    
class Transaction(models.Model):

    class transactionType(models.TextChoices):
        BUY = 'BUY'
        SELL = 'SELL'
        DIVIDEND = 'DIVIDEND'

    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    type = models.CharField(max_length=10,choices=transactionType.choices,default=transactionType.BUY)
    shares = models.PositiveIntegerField()
    pricePerShare = models.DecimalField(max_digits=10, decimal_places=2)
    priceTotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.stock.name
