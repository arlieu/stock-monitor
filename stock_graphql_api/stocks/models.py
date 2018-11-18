from django.db import models


class Stock(models.Model):
    symbol = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    bid = models.DecimalField(null=True, max_digits=7, decimal_places=2)
    ask = models.DecimalField(null=True, max_digits=7, decimal_places=2)
    target = models.DecimalField(null=True, max_digits=7, decimal_places=2)
    day_high = models.DecimalField(null=True, max_digits=7, decimal_places=2)
    day_low = models.DecimalField(null=True, max_digits=7, decimal_places=2)
    share_volume = models.BigIntegerField(null=True)
    average_volume = models.BigIntegerField(null=True)
    previous_close = models.DecimalField(null=True, max_digits=7, decimal_places=2)
    year_high = models.DecimalField(null=True, max_digits=7, decimal_places=2)
    year_low = models.DecimalField(null=True, max_digits=7, decimal_places=2)
    market_cap = models.BigIntegerField(null=True)
    pe = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    forward_pe = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    eps = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    dividend = models.DecimalField(null=True, max_digits=7, decimal_places=2)
    ex_dividend_date = models.DateField(null=True)
    dividend_date = models.DateField(null=True)
    current_yield = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    beta = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    open_price = models.DecimalField(null=True, max_digits=7, decimal_places=2)
    close_price = models.DecimalField(null=True, max_digits=7, decimal_places=2)