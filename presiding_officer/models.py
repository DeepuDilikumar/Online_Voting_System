from django.db import models

# Create your models here.
class presiding_officer(models.Model):
    gender_choices = (
        ('M', 'male'),
        ('F', 'female'),
        ('O', 'other')
    )

    employee_id = models.CharField(max_length = 20, unique = True)
    #election_id = models.ForeignKey(upcoming_election.election_id, on_delete = models.CASCADE)
    election_id = models.CharField(max_length = 20)
    first_name  = models.CharField(max_length = 30)
    last_name   = models.CharField(max_length = 30)
    gender      = models.CharField(max_length = 1, choices = gender_choices)
    email       = models.CharField(max_length = 50, null = True, unique = True)   #change null value option later
    password    = models.CharField(max_length = 50, null = True)   #change null value option later

   
    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ('+ self.employee_id+') '

    