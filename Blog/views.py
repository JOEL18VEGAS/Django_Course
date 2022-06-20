from django.shortcuts import render , redirect , get_object_or_404
from django.views.generic import View , UpdateView , DeleteView

from .forms import CreatePostForm
from .models import Post
from django.urls import reverse_lazy


# Create Posts List View
class BlogListView(View):
    
    def get( self , request , *args , **kwargs ):

        posts = Post.objects.all()

        context = {
            'posts': posts
        }

        return render( request , 'blog_list.html' , context )

#Create a new post view
class BlogCreateView(View):

    def get( self , request , *args , **kwargs ):

        form = CreatePostForm()

        context = {
            'form': form
        }


        return render( request , 'blog_create.html' , context )

    def post( self , request , *args , **kwargs ):

        if request.method == 'POST':
            form = CreatePostForm( request.POST )
            if form.is_valid():
                title = form.cleaned_data['title']
                content = form.cleaned_data['content']

                p, created = Post.objects.get_or_create( title = title , content = content )
                p.save()

                return redirect('Blog:home')
        context = {

        }
        return render( request , 'blog_create.html' , context )


class DetailView(View):

    def get( self , request , pk , *args , **kwargs ):

        post = get_object_or_404( Post , pk = pk )

        context = {
            'post': post
        }
        return render( request , 'detail.html', context )


class UpdateView(UpdateView):

    model = Post
    fields = ['title', 'content']
    template_name = 'blog_update.html'

    def get_success_url(self):
        
        pk = self.kwargs['pk']

        return reverse_lazy('Blog:detail', kwargs={'pk': pk})


class DeleteView(DeleteView):

    model = Post
    template_name = 'blog_delete.html'

    def get_success_url(self):
        return reverse_lazy('Blog:home')

    
    