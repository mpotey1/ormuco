from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import Post

def index(request):
    posts = Post.objects.all()
    template = loader.get_template('ormuco/index.html')
    context = {
     'posts': posts,
    }
    return HttpResponse(template.render(context, request))

def post(request):
    post = Post(name = request.POST["name"], favorite_color = request.POST["favorite_color"], animal = request.POST["animal"])
    post.save()
    posts = Post.objects.all()
    template = loader.get_template('ormuco/index.html')
    context = {
     'posts': posts,
    }
    return HttpResponse(template.render(context, request))
    
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'ormuco/detail.html', {'post': post})

