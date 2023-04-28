from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post

# Create your tests here.
# TestView(TestCase) : TestCase 모듈을 TestView 클래스가 상속.
class TestView(TestCase):
    # def test_post_list(self):
    #     self.assertEqual(2, 2)
    #     #assertEqual() 괄호 안에 있는 것이 같은가 아닌가를 구별함.
    # python manage.py test : tests.py의 구문들을 가지고 문서를 검사함.
    # test를 통과하면 ok. 아닐 경우 fail 표시가 뜸.
    # 왜 하는가? > 문서들끼리 결집도가 너무 높아지면 에러 탐색이 힘들어서 미리미리 알아보려고.

    def setUp(self):
        self.Client = Client
        #Client : 웹사잍 방문 사용자의 브라우저.

    def test_post_list(self):
        #1.1 포스트 목록 페이지를 가져온다
        response = self.client.get('/blog/')
        #1.2 정상적으로 페이지가 로드된다 (200은 응답 성공시 코드)
        self.assertEqual(response.status_code, 200)

        #1.3 post_list 페이지의 이름은 'Blog' 이다
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text, 'Blog')

        #1.4 내비게이션 바가 있다.
        navbar = soup.nav
        #1.5 Blog, About Me란 문구가 네비게이션 바에 있다
        self.assertIn('Blog', navbar.text)
        self.assertIn('About Me', navbar.text)

        #2.1 포스트(개시물)이 하나도 없다면
        self.assertEqual(Post.objects.count(), 0)
        #2.2 main area에 '아직 개시물이 없습니다' 라는 문구가 나타난다
        main_area = soup.find('div', id='main-area')
        self.assertIn('아직 개시물이 없습니다', main_area.text)

        #3.1 post가 2개 있으면
        post_001 = Post.objects.create(
            title='첫 번째 포스트입니다.',
            content='Hello World. We are the world.',
        )
        post_002 = Post.objects.create(
            title='두 번째 포스트입니다.',
            content='1등이 전부는 아니잖아요?',
        )
        self.assertEqual(Post.objects.count(), 2)

        #3.2 포스트 목록 페이지를 새로고침했을때
        response = self.client.get('/blog/')
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(response.status_code, 200)

        #3.3 main area에 포스트 2개의 제목이 존재한다
        main_area = soup.find('div', id='main-area')
        self.assertIn(post_001.title, main_area.text)
        self.assertIn(post_002.title, main_area.text)

        # 3.4 '아직 개시물이 없습니다' 라는 문구는 더 이상 나타나지 않음
        self.assertNotIn('아직 게시물이 없습니다', main_area.text)


