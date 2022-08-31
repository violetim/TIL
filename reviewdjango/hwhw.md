# Django Model

## 1번 문제 (Django Model)

![image-20220310165513839](homework_0310.assets/image-20220310165513839.png)

1)

* migrations 파일 생성

```bash
$ python manage.py makemigrations
```

* DB반영(모델과 DB동기화)

```bash
$ python manage.py migrate
```

![image-20220310165545788](homework_0310.assets/image-20220310165545788.png)

3번

![image-20220310165642519](homework_0310.assets/image-20220310165642519.png)

2번 (AssertionError: Negative indexing is not supported.)

![image-20220310165635692](homework_0310.assets/image-20220310165635692.png)

```shell
#In [14]: my_post = Post()

In [15]: my_post.title = "안녕하세요"

In [16]: my_post.content = "반갑습니다"

In [17]: my_post.save()
```

![image-20220310210103291](homework_0310.assets/image-20220310210103291.png)

![image-20220310165620250](homework_0310.assets/image-20220310165620250.png)

(a) objects (b) all