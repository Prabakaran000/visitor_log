from django.db import models


from django.db import models

class Visitor(models.Model):
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)
    date = models.DateTimeField(auto_now_add=True)
    visiting_reason = models.TextField()
    meet_for = models.CharField(max_length=100)

    def __str__(self):
        return self.name
