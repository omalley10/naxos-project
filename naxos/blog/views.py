from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.core.urlresolvers import reverse_lazy

from .models import BlogPost
from .forms import PostForm


class TopView(ListView):
    model = BlogPost
    paginate_by = 5


class NewPost(CreateView):
    model = BlogPost
    form_class = PostForm
    success_url = reverse_lazy('blog:top')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPost(UpdateView):
    model = BlogPost
    form_class = PostForm
    success_url = reverse_lazy('blog:top')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
