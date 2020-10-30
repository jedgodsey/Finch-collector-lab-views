from django.db import models

INJURIES = (
    ('BL', 'Blindness'),
    ('BS', 'Brain Stab'),
    ('ED', 'Ear Drum Piercing'),
    ('PT', 'Post Traumatic Stress Disorder')
)
 
class Client(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    social = models.IntegerField(null=True, blank=True)
    final_determination = models.DateField(null=True, blank=True)
    payment_issued = models.DateField(null=True, blank=True)
    payment_received = models.DateField(null=True, blank=True)
    total_award = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    def __str__(self):
        return self.name

class Claim(models.Model):
    claim_type = models.CharField(
        max_length=2,
        choices=INJURIES,
        default=INJURIES[0][0]
    )
    valid = models.BooleanField(null=True, blank=True)
    value = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.claim_type} number {self.id}'
