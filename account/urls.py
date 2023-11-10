from django.urls import path
from .views import index, Login, blog, Logout

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('blog/', blog.as_view(), name='blog'),
    path('logout/', Logout.as_view(), name='logout')
]