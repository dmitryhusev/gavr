from django.views.generic import ListView, CreateView
from .models import Post
from django.urls import reverse_lazy
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(ListView):
    model = Post
    template_name = "index.html"


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "post.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
