from django.db import models

class StockPrice(models.Model):
    close = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    last = models.FloatField()
    ttq = models.FloatField()
    turnover = models.FloatField()
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.close}, {self.high}, {self.low}, {self.last},\
        {self.ttq}, {self.turnover}, {self.date}"
