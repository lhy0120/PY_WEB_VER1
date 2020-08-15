from django.shortcuts import render
from django.views.generic import ListView
from bookmark.models import Bookmark
from django.views.generic import DetailView

# Create your views here.
class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark