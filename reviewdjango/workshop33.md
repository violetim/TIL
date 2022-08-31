# Django Model

`read`

![](workshop_0310.assets/image-20220310231025570.png)

`create`

![image-20220310231218456](workshop_0310.assets/image-20220310231218456.png)

`detail`

![image-20220310231052840](workshop_0310.assets/image-20220310231052840.png)

`update`

![image-20220310231119731](workshop_0310.assets/image-20220310231119731.png)

![image-20220310231137790](workshop_0310.assets/image-20220310231137790.png)

`urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```

```python
from django.urls import path
from . import views
app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),

]
```

`views.py`

```python
from django.shortcuts import render, redirect
from .models import Post
# Create your views here.
def index(request):
    post = Post.objects.order_by('-pk')
    context={
        'post' : post
    }
    return render(request, 'articles/index.html', context)

def new(request):

    return render(request, 'articles/new.html')

# templates 없어도 동작
def create(request):
    title = request.POST.get('title')
    content=request.POST.get('content')
    #print(f'title : {title}, content: {content}')
    #DB에 데이터 저장하기
    post = Post(title=title, content=content)
    post.save()

    # article.id = article.pk
    # return redirect('articles:detail', article.id)
    return redirect('articles:detail', post.pk)

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {'post': post} 
    return render(request, 'articles/detail.html', context)


def edit(request, pk):
    post = Post.objects.get(pk=pk)
    context= {'post':post}
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    # 1. 수정할 article을 가져온다.
    post = Post.objects.get(pk=pk)

    # 2. request로 부터 사용자가 입력한 데이터를 가져온다
    # edit.html의 input의 name따라서 
    post.title = request.POST.get('title')
    post.content = request.POST.get('content')
    # 3. article을 수정한다
    post.save()
    # 4. article 상세페이지로 보낸다.
    return redirect('articles:detail', post.pk)

def delete(request, pk):
    #1. pk에 해당하는 글을 db에서 가져온다
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        #2. 해당글을 삭제합니다.
        post.delete()
        #3. index페이지로 이동합니다
        return redirect('articles:index')
    else:
        return redirect('articles:detail', post.pk)
```

`templates`

`index.html`

```html
{% extends 'base.html' %}

{% block content%}
<h1> INDEX </h1>
<a href="{% url 'articles:new' %}">NEW </a>
<hr>
{% for o in post %}
  <p> 글 제목 : {{o.title}} </p>
  <p> 글 내용 : {{o.content}} </p>

<a href="{% url 'articles:detail' o.id %}">DETAIL </a>
{% endfor %}
{% endblock content%}
```

`new.html`

```html
{% extends 'base.html' %}

{% block content%}
<h1> NEW </h1>

<form action="{%url 'articles:create' %}" method="POST">

  {% csrf_token %}
  <label for="title"> TITLE :</label>
  <input type="text" name="title" id="title"><br>
  <label for="content"> CONTENT : </label><br>
  <textarea name="content" cols="30" rows="5" id="content"> </textarea>
  <br>
  <input type="submit" value="작성">

</form>
<a href="{% url 'articles:index' %}">BACK </a>
{% endblock content%}
```

`edit.html`

```html
{% extends 'base.html' %}
{% block content %}

  <h1> EDIT </h1>
  <form action="{% url 'articles:update' post.pk%}" method="POST">
    <!--method="POST", csrf_token은 짝꿍-->
    {% csrf_token %}
    <!--lable의 for와, input의 id는 짝꿍-->
    <!--input의 name은 서버로 보낼 때 필요-->
    <label for="title"> Title : </label> 
    <!-- 인풋은 value속성을 넣고, textarea는 속성이없어서 그냥 써줌-->

    <input type="text" id="title" name="title" value={{post.title}}>
    <br> <!--줄바꿈 breaking line-->
    <label for="content"> Content : </label>
    <br>
    <textarea name="content" cols="30" rows="5" id="content">{{post.content}} </textarea>
    <br>
    <input type="submit" value="수정">
  </form>

  <!--<a href="{/articles/index/}">목록보기 </a>-->

  <a href="{% url 'articles:index' %}">BACK </a>
{% endblock content %}
```

`detail.html`

```html
{% extends 'base.html' %}

{% block content %}
  <h1> DETAIL </h1>
  <p> 게시글 제목 : {{post.title}} </p>
  <p> 게시글 내용 : {{post.content}} </p>
  <p> 작성일 : {{post.created_at}} </p>
  <p> 수정일 : {{post.updated_at}} </p>
  <hr>

  <form action="{% url 'articles:delete' post.pk %}" method="post">
    {% csrf_token %}
    <button class="btn btn-danger"> DELETE </button>


  <div class="btn-group" role="group" aria-label="Basic outlined example">
    <button type="button" class="btn btn-outline-primary" onclick="location.href='{% url 'articles:edit' post.pk %}'">EDIT</button>
    <button type="button" class="btn btn-outline-primary" onclick="location.href='{% url 'articles:index' %}'">BACK</button>
  </div>
{% endblock content %}
```

`models.py`

```python
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title    
```
