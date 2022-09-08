from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .form import CustomUserCreationForm

# Create your views here.

User = get_user_model()

def index(request):
    #모든 유저 목록을 보고 싶다? Model.manger.querySet API를 가지고 와야 한다.
    users = User.objects.all()
    context = {
        'users' : users,
    }
    #이 유저라는 값은 어디에서 어떻게 가져와서 써야할까요?
    #내 모든~데이터를 가지고 다룰 수 있는 곳 =  Model 일단 정의부터 다시 하러가자
     #각 app/ 템플릿츠 들에 어카운츠라는 이름 해당 폴더경로 안쪽 탐색
     #html을 사용자에게 render 해서 보내준다.
     #앱 폴더 안에 템플릿 폴더를 자동으로 찾으러가게 만들어줌
    return render(request, 'accounts/index.html', context)


def signup(request):
    #회원가입 로직을 생각해보자
    #회원 정보를 입력해서 요청을 보낼 수  있는 form 태그가 있는 페이지가 필요하다.
    #회원 가입은 사실 생성이다. 사용자가 보내온 요청에 따라서 (함께 보낸 정보 토대로)
    #새 유저 생성
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            auth_login(request, user)
        
            return redirect('accounts:index')
            #인덴테이션 이쪽임. 왜냐하면 유효성검사를 실패하면 인덱스로 보내버림.
        
    else:
        #생성하고자 하는 데이터는 폼에서 왔고 
        
        form = CustomUserCreationForm()


    # 그 외
    context = {
        'form' : form
    }

    #조회가 먼저니 조회를 먼저 만들어 줄 것 생성은 두고 조회를 만들어주자.
    #원래라면? return render(request,'accounts/signup.html',)
    #회원가입을 하기 위한 폼태그는 어떻게 만들어줘야될지 모르겠어...멘붕..이멜은어떻게?
    #firstname lastname 다다 만들어줘야하는데..어떻게함? 장고가 다 만들어준다.
    #장고가 만들어놓은 폼을 뒤적거려 보자.

    return render(request,'accounts/form.html', context)
    
def logout(request):
    auth_logout(request)
    #리퀘스트에 유저정보인 request.user 넣으면 되지 않을까?
    #지우면 할일다함
    return redirect('accounts:index')


def login(request):
    #로그인이란 내 계정정보를 입력하여 내 서버에 나를 인증하는 페이지
    #내 계정정보를 입력할수있는 페이지 먼저 보여주세요.
    #생성. 수정을 해야하는 일이 세트로 따라온다는것을 안다.
    #외워서쓰지말고
    if request.method == 'POST':
        #사용자가 보낸 데이터를 토대로 폼 생성
        #폼에 들어있는 데이터 유효성 검사
        #디비에 저장은 세션아이디만 할거고 그건 로그인 함수가 해줄것 폼 어떻게생성?
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            #노란색이니까 함수겠네 () 해주자..
            return redirect('accounts:index')

    else:
        form = AuthenticationForm() #인증 폼
    
    context = {
        'form' : form
    }
        #인증폼을 쓸 것임.
    return render(request,'accounts/form.html', context)