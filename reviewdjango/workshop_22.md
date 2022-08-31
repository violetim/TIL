# Django 03/08 Model

![image-20220309215954657](workshop_0308.assets/image-20220309215954657.png)

![image-20220309221246328](workshop_0308.assets/image-20220309221246328.png)

## code

`crud > urls.py`

```python
from django.contrib import admin
from django.urls import path, include
#from articles import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```

`articles > urls.py`

```python
from django.urls import path
from . import views

app_name='articles'
urlpatterns = [
    # '' 빈문자열로 표현
    path('', views.read, name='read'),
    path('new/', views.create, name='create'),
]
```



`views.py`

```python
from django.shortcuts import render, redirect
from .models import Article
# Create your views here.

def read(request):
    obj = Article.objects.all()
    context={
        'obj':obj
    }
    return render(request, 'articles/read.html', context)
    
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    # DB에 저장하기
    article = Article(title=title, content=content)
    article.save()
    return redirect('articles/read.html')
```



`templates`

`base.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  <title>0308 workshop</title>
</head>
<body>
  {% block content%}
  {% endblock content%}
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</body>
</html>
```



`read.html(index)`

```html
{% extends 'base.html' %}

{% block content%}
<h1> INDEX </h1>
<a href="{% url 'articles:create' %}">NEW </a>
<hr>
{% for o in obj %}
  <p> 글 제목 : {{o.title}} </p>
  <p> 글 내용 : {{o.content}} </p>
{% endfor %}
<a href="{% url 'articles:create' %}">DETAIL </a>
{% endblock content%}
```



`create.html`

```html
{% extends 'base.html' %}

{% block content%}
<h1> NEW </h1>

<form action="{% url 'articles:read' %}" method="POST">
  <!--method="POST", csrf_token은 짝꿍-->
  {% csrf_token %}
  <label for="title"> TITLE :</label>
  <input type="text" name="title" id="title"><br>
  <label for="content"> CONTENT : </label><br>
  <textarea name="content" cols="30" rows="5" id="content"> </textarea>
  <br>
  <input type="submit" value="작성">

</form>
<a href="{% url 'articles:read' %}">BACK </a>
{% endblock content%}
```



`models.py`

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    # id를 생성해주지 않으면 자동으로 만들어짐
    # CharField는 max_length가 필수 인자
    title = models.CharField(max_length=30)
    # TextField는 CharField보다 더 넓은 범위, 제한 없이 적음
    content = models.TextField()
    # auto_now_add는 최초 1번, auto_now는 데이터 수정때마다 갱신
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```





## Article CR (CREATE & READ) 진행 과정

## 1. 가상환경 구축 & project, app 생성 & settings.py 잡기

1. 가상환경 구축하기

```bash
$ python -m venv venv
```





2. 가상환경 실행시키기

```bash
$ source venv/Scripts/activate 
```





3. pip list로 목록 확인하기

```bash
$ pip list
```





4. 버전에 맞는 `django` 설치

```bash
$ pip install django==3.2.10
```

4-1. `requirements.txt` 설치

* 재귀(리컬시브) 사용

``` bash
$ pip install -r requirements.txt
```





5. 프로젝트 시작하기 (프로젝트 이름은 crud)

```bash
$ django-admin startproject crud .
```





6. 앱 생성 (앱 이름은 articles)

```bash
$ python manage.py startapp articles
```





7. 프로젝트의 settings.py 의 `INSTALLED_APPS`에 앱 추가 (순서 주의)

![image-20220309193855728](C:%5CUsers%5Cstar3%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20220309193855728.png)



8. 프로젝트의 settings.py 시간, 언어 설정

![image-20220303164713059](C:/Users/star3/ssafy7/hws/0302/workshop_0302.assets/image-20220303164713059.png)





---

### 2. models.py와 migration

1. 앱의 models.py

![image-20220309200152818](C:/Users/star3/ssafy7/hws/0308/Article%2520CR%2520(CREATE%2520&%2520READ)%2520%25EC%25A7%2584%25ED%2596%2589%2520%25EA%25B3%25BC%25EC%25A0%2595.assets/image-20220309200152818.png)



* models.py를 건들이면 꼭 migrate를 해야하는데, git 처럼 변경사항이 생기고, 그걸 보고하는 시스템임
* 그리고 아무것도 건들지 않아도 model을 사용하기 위해서는 django에 내장된 기본 model을 최초 한 번은 migrate를 해야 사용할 수 있게 된다.

2. migration생성

``` bash
$ python manage.py makemigrations
```

![image-20220309195401306](C:/Users/star3/ssafy7/hws/0308/Article%2520CR%2520(CREATE%2520&%2520READ)%2520%25EC%25A7%2584%25ED%2596%2589%2520%25EA%25B3%25BC%25EC%25A0%2595.assets/image-20220309195401306.png)



3. migrate

``` bash
$ python manage.py migrate
```

![image-20220309195420382](C:/Users/star3/ssafy7/hws/0308/Article%2520CR%2520(CREATE%2520&%2520READ)%2520%25EC%25A7%2584%25ED%2596%2589%2520%25EA%25B3%25BC%25EC%25A0%2595.assets/image-20220309195420382.png)



`[migratie 관련 명령어]`

* orm이 sql로 변환한 것이 나옴

```bash
$ python manage.py sqlmigrate articles 0001
```

![image-20220308103625634](C:/Users/star3/ssafy7/hws/0308/Article%2520CR%2520(CREATE%2520&%2520READ)%2520%25EC%25A7%2584%25ED%2596%2589%2520%25EA%25B3%25BC%25EC%25A0%2595.assets/image-20220308103625634.png)


  *	 migration을 보여달라!

``` bash
$ python manage.py showmigrations
```

노란색 - 앱

초록색 - 마이그래이션

분홍색(X) - 적용된 것

![image-20220308104015090](C:/Users/star3/ssafy7/hws/0308/Article%2520CR%2520(CREATE%2520&%2520READ)%2520%25EC%25A7%2584%25ED%2596%2589%2520%25EA%25B3%25BC%25EC%25A0%2595.assets/image-20220308104015090.png)





### 3. urls.py

1. 프로젝트의 urls.py

![image-20220309201921911](C:/Users/star3/ssafy7/hws/0308/Article%2520CR%2520(CREATE%2520&%2520READ)%2520%25EC%25A7%2584%25ED%2596%2589%2520%25EA%25B3%25BC%25EC%25A0%2595.assets/image-20220309201921911.png)



(원래)18번 줄을 넣어줘야 내가 만든 앱 pages의 views를 쓸 수 있음

```python
from articles import views
```



(앱에 urls.py를 또 만들 때) 17번째 줄에 include를 넣어줌

urlpatterns 21번째 줄 



#### cf) Variable Routing

ex) Variable Routing의 개념을 활용한다. 저녁메뉴는 string, 인원수는 integer이다.

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dinner/<str:menu>/<int:people>', views.dinner),
]
```



2. 앱의 urls.py

![image-20220309210139716](C:/Users/star3/ssafy7/hws/0308/Article%2520CR%2520(CREATE%2520&%2520READ)%2520%25EC%25A7%2584%25ED%2596%2589%2520%25EA%25B3%25BC%25EC%25A0%2595.assets/image-20220309210139716.png)

* html에서는 이런 식으로 연결

![image-20220309210503946](C:/Users/star3/ssafy7/hws/0308/Article%2520CR%2520(CREATE%2520&%2520READ)%2520%25EC%25A7%2584%25ED%2596%2589%2520%25EA%25B3%25BC%25EC%25A0%2595.assets/image-20220309210503946.png)



cf) dinner

**![image-20220303191338625](C:/Users/star3/ssafy7/hws/0302/workshop_0302.assets/image-20220303191338625.png)**

request와 함께 Variable Routing을 통해 전달 받은 인자를 html 파일에서 사용할 수 있도록 렌더링 할 때 넘겨준다.

```python
def dinner(request, menu, people):
    context = {
        'menu':menu,
        'people':people
    }
    return render(request, 'dinner.html', context )
```



### 4. veiws.py

참고)

![image-20220309211010907](C:/Users/star3/ssafy7/hws/0308/Article%2520CR%2520(CREATE%2520&%2520READ)%2520%25EC%25A7%2584%25ED%2596%2589%2520%25EA%25B3%25BC%25EC%25A0%2595.assets/image-20220309211010907.png)







### templates

1. 프로젝트의 `BASE_DIR` 설정

![image-20220309203152277](C:/Users/star3/ssafy7/hws/0308/image-20220309203152277.png)



2. BASE_DIR은 프로젝트와 동일선상에 `templates`폴더를 만들면 됨

![image-20220309203238855](C:/Users/star3/ssafy7/hws/0308/Article%2520CR%2520(CREATE%2520&%2520READ)%2520%25EC%25A7%2584%25ED%2596%2589%2520%25EA%25B3%25BC%25EC%25A0%2595.assets/image-20220309203238855.png)

3. 프로젝트 외부 templates 폴더 하위에 base.html을 생성하고 부트스트랩 cdn을 불러옴

* 11, 12번째 줄 

![image-20220309203319702](C:/Users/star3/ssafy7/hws/0308/Article%2520CR%2520(CREATE%2520&%2520READ)%2520%25EC%25A7%2584%25ED%2596%2589%2520%25EA%25B3%25BC%25EC%25A0%2595.assets/image-20220309203319702.png)



4. `앱/templates/앱` 하위에 base.html을 상속받을 템플릿 파일들을 만듦

(여기서는 read.html, create.html 두개 필요)

* read.html

```html
{% extends 'base.html' %}

{% block content%}
<h1> INDEX </h1>
<a href="{% url 'articles:create' %}">NEW </a>
<hr>
{% for article in articles %}
  <p> 글 제목 : {{article.title}} </p>
  <p> 글 내용 : {{article.content}} </p>
{% endfor %}
<a href="{% url 'articles:create' %}">DETAIL </a>
{% endblock content%}
```



* create.html

![image-20220309204304714](C:/Users/star3/ssafy7/hws/0308/Article%2520CR%2520(CREATE%2520&%2520READ)%2520%25EC%25A7%2584%25ED%2596%2589%2520%25EA%25B3%25BC%25EC%25A0%2595.assets/image-20220309204304714.png)



```html
{% extends 'base.html' %}

{% block content%}
<h1> NEW </h1>

<form action="{% url 'articles:read' %}" method="POST">
  <!--method="POST", csrf_token은 짝꿍-->
  {% csrf_token %}
  <label for="title"> TITLE :</label>
  <input type="text" name="title" id="title"><br>
  <label for="content"> CONTENT : </label><br>
  <textarea name="content" cols="30" rows="5" id="content"> </textarea>
  <br>
  <input type="submit" value="작성">

</form>
<a href="{% url 'articles:read' %}">BACK </a>
{% endblock content%}
```



