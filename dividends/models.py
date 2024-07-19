from django.db import models

class Dividens(models.Model):
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    number_of_promotion = models.FloatField(blank=True, null=True)
    price_of_promotion = models.FloatField(blank=True, null=True)
    total_sum_of_promotions = models.FloatField(blank=True, null=True)
    percent_of_dividends = models.FloatField(default=3, blank=True, null=True)
    calculated_dividend = models.FloatField(blank=True, null=True)
    holded_dividends = models.FloatField(blank=True, null=True)
    payable_dividens = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):

        if self.number_of_promotion is not None and self.price_of_promotion is not None:
            self.total_sum_of_promotions = self.number_of_promotion * self.price_of_promotion

        if self.total_sum_of_promotions is not None and self.percent_of_dividends is not None:
            self.calculated_dividend = (self.total_sum_of_promotions * self.percent_of_dividends) / 100
            self.holded_dividends = self.calculated_dividend * 10 / 100
            self.payable_dividens = self.calculated_dividend - self.holded_dividends

        super(Dividens, self).save(*args, **kwargs)


    def __str__(self):
        return f"Shareholder's full name - {self.first_name} {self.last_name}"
    
