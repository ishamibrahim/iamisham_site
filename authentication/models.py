from django.db import models
from django.contrib.auth.models import AbstractUser
from authentication.manager import UserManager

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Role(BaseModel):
    ADMIN = 'admin'
    EDITOR = 'editor'
    PARTICIPANT = 'participant'

    ROLE_CHOICES = (
        (ADMIN, ADMIN),
        (EDITOR, EDITOR),
        (PARTICIPANT, PARTICIPANT)
    )
    name = models.CharField(choices=ROLE_CHOICES, null=False)

    def __str__(self):
        return self.name


class UserData(AbstractUser, BaseModel):
    url = models.URLField(name="url", null=True)
    full_name = models.CharField(null=False, blank=False, max_length=250)
    email = models.EmailField(unique=True)
    rank = models.IntegerField(null=False, default=0)
    security_id = models.CharField(max_length=155)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    REQUIRED_FIELDS = ['email']
    objects = UserManager()

    def __str__(self):
        return self.full_name

