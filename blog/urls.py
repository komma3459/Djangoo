from django.urls import path
from . import views

urlpatterns = [
    # CBV 기반 path
    # 127.0.0.1:8000 생략 상태
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('create_post/', views.PostCreate.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
    #FBV 기반 path
    path('category/<str:slug>/', views.category_page),
    path('tag/<str:slug>/', views.tag_page),

    # FBV 기반인 views.index는 주석 처리
    # path('',views.index),
    # path('<int:pk>/', views.single_post_page)
]