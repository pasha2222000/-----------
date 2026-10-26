from django.shortcuts import render,HttpResponse, redirect
from .models import Post, Profile, Category
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import PostForm, RegistrationForm
from django.contrib.auth import login

# Create your views here.
def test(request):
    return HttpResponse('test')


def main(request):
    posts= Post.objects.filter(status=Post.PUBLISHED)
    profiles=Profile.objects.all() 
    return render(request, 'main.html', {
        'posts':posts,
        'users':profiles
    })


def profile(request, id):
    return render(request, 'profile.html')


def sign_up(request):
    return render(request, 'register.html')


def sign_in(request):
    return render(request, 'login.html')


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "new_post.html"
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    model = Post
    form_class = PostForm
    template_name = "new_post.html"
    success_url = reverse_lazy('main')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_superuser


class PostDeleteView(LoginRequiredMixin, DeleteView, UserPassesTestMixin):
    model = Post
    template_name = "post_confirm_delete.html"
    success_url = reverse_lazy('main')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_superuser

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})