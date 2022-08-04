from django.db import models

# Create your models here.

class student_detail(models.Model):

    name           = models.CharField(max_length = 30)
    roll_no        = models.IntegerField()
    adm_no         = models.IntegerField()
    department     = models.CharField(max_length = 30)
    year           = models.IntegerField()
    gender         = models.CharField(max_length = 10)
    degree         = models.CharField(max_length = 20)
    phone_no       = models.CharField(max_length = 15)
    staff_adv_username = models.CharField(max_length = 30)
    staff_adv_id       = models.CharField(max_length = 30)

    def __str__(self):
        return self.name + ' ('+str(self.roll_no)+') '


class election_posts(models.Model):

    depts_choices = (
        ('CS', 'Computer Science'),
        ('EC', 'Electronics and Communications'),
        ('BT', 'Biotechnology'),
        ('ME', 'Mechanical'),
        ('MP', 'Mechanical Production'),
        ('All', 'All')
    )

    gender_choices = (
        ('M', 'M'),
        ('F', 'F'),
        ('All', 'All')
    )

    year_choices = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('All', 'All')
    )

    degree_choices = (
        ('M', 'M Tech'),
        ('B', 'B Tech'),
        ('All', 'All')
    )

    post_id = models.CharField(max_length = 30)
    position_name = models.CharField(max_length = 30)
    depts = models.CharField(max_length = 30, choices = depts_choices)
    gender  = models.CharField(max_length = 30, choices = gender_choices)
    year  = models.CharField(max_length = 30, choices = year_choices)
    degree = models.CharField(max_length = 30, choices = degree_choices)

    class meta:
            ordering = ('post_id')

    def __str__(self):
        return self.position_name + '('+str(self.post_id)+')'

        

class candidate(models.Model):
    first_name  = models.CharField(max_length = 30)
    last_name   = models.CharField(max_length = 30)
    adm_no      = models.IntegerField()
    apply_position   = models.CharField(max_length = 30)
    position_id      = models.CharField(max_length = 10)
    candidate_id     = models.IntegerField()

    def __str__(self):
        return self.first_name +' ('+self.apply_position+ ')'



    
