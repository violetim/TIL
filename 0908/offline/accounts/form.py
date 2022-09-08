from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields

#원래거를 상속받아서 수정해서 데이터를 집어넣어서 쓰기