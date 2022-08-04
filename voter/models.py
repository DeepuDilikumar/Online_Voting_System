from django.db import models

# Create your models here.


class votes(models.Model): #to store the votes for each candidate
    position_id   = models.IntegerField()
    position_name = models.CharField(max_length = 30)
    candidate1    = models.IntegerField(default=0)
    candidate2    = models.IntegerField(default=0)
    candidate3    = models.IntegerField(default=0)
    total_votes   = models.IntegerField(default = 0)

    def __str__(self):
        return self.position_name+' ('+str(self.position_id)+') '




