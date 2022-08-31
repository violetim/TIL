# Django 03/03 Django Web Framework

## 1번 문제 (lotto)

* 뭐가 문제일까?! 번호가 안나옴..

1. `urls.py`

```python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lotto/', views.lotto),
]
```





2. `views.py`

```python
from django.shortcuts import render
import random
# Create your views here.
def lotto(request):
    number = set()
    while len(number) < 6: 
        number.add(random.randint(1, 45))
    lottonumbers = list(number)
    context= {
        'lottonumbers' :lottonumbers
    }
    return render(request, 'lotto.html', context)

```





3. `lotto.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>lotto</title>
</head>
<body>
  <h1>제 000회 로또 번호 추천</h1>
  <p> SSAFY님께서 선택하신 로또 번호는 [{{lottonumber|join:', '}}]입니다. </p>
</body>
</html>
```






