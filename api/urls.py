from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('articles', views.ArticleViewSet, basename='articles')
router.register('users', views.UserViewSet)

urlpatterns = [
    path('', views.Index),
    
    # path('articles/', views.article_list),
    # path('articles/<int:pk>', views.article_detail),
    
    # path('articles/', views.ArticleList.as_view()),
    # path('articles/<int:id>', views.ArticleDetails.as_view()),
    
    path('api/', include(router.urls)),
]