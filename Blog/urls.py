from django.urls import path
from .views import BlogListView, BlogCreateView , DetailView , UpdateView , DeleteView

app_name = 'Blog'

urlpatterns = [

    path('', BlogListView.as_view(), name='home'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/update/', UpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', DeleteView.as_view(), name='delete'),

]