from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 내가 필드들을 다 만들거 아니고 장고가 원래 가지고 있는 유저 모델을 쓸 것임
# 왜 장고가 가지고 있는거 쓸 것이냐? 클래스 유저라는게 이미 장고에 있다.
#우리 가상환경 설치하고 거기에서 장고를 설치했었잖아? 그걸 가져와서 어카운츠의 모델로
#얘가 들어있는 폴더가 auth에 있음.
# from django.contrib.auth.models import AbstractUser 을 위에다가 추가해주자
#class User(models.Model):에서
class User(AbstractUser):
    pass
