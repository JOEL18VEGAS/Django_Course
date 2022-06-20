#Imports
from django.contrib import admin
from django.urls import path , include
from .views import HomeView

#UrlsPatterns
urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    path('', HomeView.as_view(), name='home'),

    path('blog/', include('Blog.urls', namespace='Blog')),

    # path("__reload__/", include("django_browser_reload.urls")),

]
 