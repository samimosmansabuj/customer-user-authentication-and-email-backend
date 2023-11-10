from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .form import LoginForm
from django.contrib.auth import authenticate, login, logout
from .mixins import LogoutRequiredMixin
from django.views.decorators. cache import never_cache
from django.utils.decorators import method_decorator


@method_decorator(never_cache, name='dispatch')
class index(LoginRequiredMixin, generic.TemplateView):
    login_url = 'login'
    template_name = "home/index.html"

class blog(LoginRequiredMixin, generic.TemplateView):
    login_url = 'login'
    template_name = "home/blog.html"

@method_decorator(never_cache, name='dispatch')
class Login(LogoutRequiredMixin, generic.View):
    def get(self, *args, **kwargs):
        form = LoginForm()
        context = {
            'form': form
        }
        return render(self.request, 'home/login.html', context)

    def post(self, *args, **kwargs):
        form = LoginForm(self.request.POST)

        if form.is_valid():
            user = authenticate(
                self.request, username = form.cleaned_data.get('username'), password = form.cleaned_data.get('password')
            )
            if user:
                login(self.request, user)
                return redirect('index')
            else:
                messages.warning(self.request, "Wrong Information")

        return render(self.request, 'home/login.html', {'form':form})

class Logout(generic.View):
    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect('login')