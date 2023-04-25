from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.

# CBV (장고 제공 클래스 기반 views 제작)
class PostList(ListView):
    model = Post
    ordering = '-pk'
    # template_name = 'blog/index.html'
    # 블로그 경로에 있는 index.html 이름을 post(모델명)_list로 고쳐버리기
    # django.views.generic으로 부르는 ListView는
    # 모델명_list.html을 기본 파일명으로 삼기 때문이다.
    # ListView의 ordering = -pk는 포스트 목록 페이지의 포스트를 역순으로 정렬해줌

class PostDetail(DetailView):
    model = Post
# 상세 페이지를 보여주기 위해 CBV의 DetailView를 불러옴
# class 클래스명(DetailView) : ()안의 DeetailView를 () 밖의 클래스가 상속한다는 뜻
# model = Post여야 하는 이유 : models.py에서 불러올 클래스가 Post이기 때문.
# 이거 작성하고 urls 가서 path('<int:pk>/', views.PostDetail.as_view()) 작성해주기
# 블로그 경로에 있는 single_post_page.html을 post_detail.html로 고치기
# DetailView는 모델명_detail.html을 기본 파일명으로 삼기 때문이다

# FBV(함수 기반 views 제작)
# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts': posts,
#         }
#     )
#
# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post':post
#         }
#     )