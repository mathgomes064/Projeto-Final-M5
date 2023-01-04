from django.db import models
import uuid


class Description(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    serviceDescription = models.CharField(max_length=50)
    serviceValue = models.DecimalField(max_digits=5, decimal_places=2)
    atuationArea = models.CharField(max_length=50)
