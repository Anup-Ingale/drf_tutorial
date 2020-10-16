from django.conf.urls import include
from django.urls import path
from api_base.views import GenericViewsets
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import  DefaultRouter


router = DefaultRouter()
router.register(r'article',GenericViewsets,basename='article')
# router.register(r'article',ArticleViewSet,basename='article')

urlpatterns = [
    # normal api_views.
    # path('article/',views.article_list),
    # path('article/<int:pk>/',views.article_details),

    # function based api_view
    # path('article/', views.article_list),
    # path('article/<int:pk>/', views.article_details),

    # class-base api_views
    # path('article/', views.ArticleList.as_view()),
    # path('article/<int:pk>/', views.ArticleDetails.as_view()),

    # class-base api_views plus Mixins
    # path('article/',views.ArticleList.as_view()),

    # class-base api_views plus GenericView
    # path('article/', views.ArticleList.as_view()),
    # path('article/<int:pk>/', views.ArticleDetails.as_view()),

    # Basic and Session Authentication Class Base View.
    # path('article/<int:pk>/', views.ArticleAPIView.as_view()),

    #Token Authentication
    # path('article/<int:pk>/', views.ArticleAPIView.as_view()),

    # ViewSets & Routers
    # path('viewsets/',include(router.urls)),
    # path('viewsets/<int:pk>/',include(router.urls)),

    # Generic Viewsets .
    # path('viewsets/',include(router.urls)),

    #Viewsets and ModelViewsets
    path('viewsets/',include(router.urls)),

]

# urlpatterns = format_suffix_patterns(urlpatterns)
# urlpatterns = router.urls
