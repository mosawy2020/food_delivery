from django.db import models


class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)

