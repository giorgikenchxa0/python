from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm 

from django.contrib.auth.forms import UsernameField
from users.models import User

class UserCreationForm(DjangoUserCreationForm):

    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}
