from django.views.generic import ListView
from blog.models import Post
from django.views.generic import ListView, DetailView


# Create your views here.
class PostLV(ListView):
    model = Post
class PostDV(DetailView):
    model = Post