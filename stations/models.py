from django.db import models

class IssPassenger(models.Model):
    passenger_name = models.TextField()
    
    def __str__(self):
        return self.passenger_name
    
