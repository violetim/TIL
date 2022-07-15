# CLI INTRO

- GUI는 CLI에 비해 사용하기 쉽지만 단계가 많고 컴퓨터의 성능을 더 많이 소모
- 수 많은 서버/개발 시스템이 CLI를 통한 조작 환경을 제공
- 무슨 파일이 삭제되었나? 명령어를 보고 있음. 개발시스템이 CLI로 제공이 될 것
- 나중에 복잡한 개발과정을 거칠 때도 사용 가능.



---



## 각종명령어들

### 파일 생성

####  touch

 

```bash
$ touch {파일명} : 생성하는 것
```



#### mkdir

파일은 터치로 만들었다면?

폴더는 `mkdir`로 만들기

mkdir my_folder



---

#### 파일 목록 확인

#### ls

. 쩜은 현재 폴더

..여기의 상위의 폴더 가 있다!를 확인할 수 있음.

숨긴 파일들을 확인하기 위해 사용함

ls -a

ls -l (작성자까지 구체적으로 확인가능)

```bash
$ ls
```



---

`ctrl`+`l` 화면을 깔끔하게 만들 수 있다.

---

`pwd` 현재 작업위치 확인 가능

---

### 작업하는 위치 바꾸기

`cd`+ 폴더이름

cd my_folder / 깃 쓸 때 특히 많이 사용

상위폴더로 가고 싶으면

cd ..

데스크탑까지 가고 싶으면

cd .. cd .. 쭉~~~~ 



체인지디렉토리 : 상대경로 내 현재경로를 기준점으로 어디로 가겠다가 있음.



cd lectures/startcamp

le누르고 탭 하면 자동완성되기도함.. 이 폴더안에 초기 스펠링 두개만!

`Tab`키를 잘 활용하세요~!~ 명령어들은 자동완성 사용하세요

코드는 손으로 치시고 

---



#### 필요가없는 파일 및 폴더 지우기

`rm` : 파일을 지우기 위해 사용

`rm -r` : 폴더를 지우기 위해 사용



---



절대경로 / 상대경로 이야기

- 절대경로
  - 루트 디렉토리부터 목적 지검까지 거치는 모든 경로를 전부 작성
  - 윈도우 바탕 화면의 절대경로 C:/Users/ssafy/Desktop
- 상대 경로
  - 현재 작업하고 있는 디렉토리 (.) 기준으로 계산된 상대적인 위치
  - 현재 작업하고 있는 디렉토리가 C:/Users일 때
  - 윈도우 바탕화면의상대 경로는 ssafy/Desktop
- ./ : 현재 작업하고 있는 폴더 
- ../ 현재 작업하고 있는 폴더의 부모 폴더
- 

---

   

Git이 도대체 뭐길래?????

- Readme.
- Repository 레포지토리 (저장소) 특정 디렉토리를 관리
  - 이 저장소안에 뭘 다루냐? 우리가 다룬 문서들! 관리를 깃이 해준다.
  - 깃이 어떤 폴더, 작업공간을 기준으로 해주냐 파악할수있도록 하는게
  - git init 로컬저장소 생성
  - .git 디렉토리에 버전 관리에 필요한 모든 것이 들어있음.
  - 명령어? git bash라는 터미널에서 쓸 것임



- 작업하는 위치 / 데스크탑 아님. 코드 모여있는 lectures 폴더에서 git bash here에서

  - git init을 해보자! ls -a하면 볼수있습니당.
  - git staus 깃아! 현재 상태를 알려줘
    Untracked files: 스타트캠프 안에 폴더가 나랑 같이 존재하고 있는데 나는 아직 이 폴더안에 있는 변동사항들을 신경쓰지 않고 있다. 지금상태에서는 어떤 변동사항이 있어도 안남는다
  - 커밋committe
  - 트래킹track
  - 애드add

- Readme 생성하기

  - Lectures//  (실제로 작업 - working directory) 내가 작업하고 있는 실제 디렉토리

    신발을 만드는 것

  - Staging Area(우리 눈에는 안보이고 깃 안에서- 우리가 워킹디렉토리에 썼던 것들이 똑같이들어옴. ) 커밋으로 남기고 싶은. 특정 버전으로 관리하고 싶은 파일이 있는 곳

  ​       검은색 신발을 사진대 위에 올리는 것

  - Repository 커밋들이 저장되어있는 곳 = 깃 이닛	

    검은색 신발들을 찍어내는 것 

    





untracked <- git add

staged <- git commit // 얘는 커밋으로 버전남김

commited <- +AB라는 내용이 들어간 것이 추가로 들어감



---

우리는 왜 Staging area를 거쳐서 커밋으로 버전을 남겨야하나?

---



```bash
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        startcamp/
        
        SSAFY@DESKTOP-KVCQHCD MINGW64 ~/Desktop/lectures/startcamp (master)
$ git add hello.py

SSAFY@DESKTOP-KVCQHCD MINGW64 ~/Desktop/lectures/startcamp (master)
$ git status

On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   hello.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        CLI.md
        __pycache__/
        age.py
        lotto.py
        lunch.py
        test.py
        
        
        $ git add lunch.py age.py test.py


---



SSAFY@DESKTOP-KVCQHCD MINGW64 ~/Desktop/lectures/startcamp (master)
$ git commit -m "SC Day7 python intro"
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.
 
fatal: unable to auto-detect email address (got 'SSAFY@DESKTOP-KVCQHCD.(none)')



---

SSAFY@DESKTOP-KVCQHCD MINGW64 ~/Desktop/lectures/startcamp (master)
$ git commit -m "SC Day7 python intro"
[master (root-commit) ed3eb59] SC Day7 python intro
 4 files changed, 39 insertions(+)
 create mode 100644 startcamp/age.py
 create mode 100644 startcamp/hello.py
 create mode 100644 startcamp/lunch.py
 create mode 100644 startcamp/test.py

SSAFY@DESKTOP-KVCQHCD MINGW64 ~/Desktop/lectures/startcamp (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        CLI.md
        __pycache__/
        lotto.py

nothing added to commit but untracked files present (use "git add" to track)

SSAFY@DESKTOP-KVCQHCD MINGW64 ~/Desktop/lectures/startcamp (master)
$ git log
commit ed3eb5933cbf1afe79aee62c304298ac28c32af6 (HEAD -> master)
Author: purpleim <brlimdev@gmail.com>
Date:   Fri Jul 15 14:40:06 2022 +0900

    SC Day7 python intro

SSAFY@DESKTOP-KVCQHCD MINGW64 ~/Desktop/lectures/startcamp (master)
$ git log --oneline
ed3eb59 (HEAD -> master) SC Day7 python intro



```



이거는 워킹에어리어에만 있음

$깃아런치랑 테스트랑 다 스테이징에리어에 넣어줘!!!

git config --global user.email "brlimdev@gmail.com"
git config --global user.name "purpleim"



컨트롤씨는 복사 아니고 copy 누르고

`shift`+`insert` 하면 붙여넣기가 된다.

---



