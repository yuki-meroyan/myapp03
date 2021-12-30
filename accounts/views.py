from django.shortcuts import render, redirect, resolve_url
from django.http.response import HttpResponseRedirect
from django.views import generic
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model # login
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy

from .forms import LoginForm, SignUpForm, UserUpdateForm, MyPasswordChangeForm

'''トップページ'''
class IndexView(TemplateView):
    template_name = 'accounts/index.html'

'''ログイン'''
class Login(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'

'''ログアウト'''
class Logout(LogoutView):
    template_name = 'accounts/logout.html'

class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        # 今ログインしてるユーザーのpkと、そのマイページのpkが同じなら許可
        user = self.request.user
        return user.pk == self.kwargs['pk']

'''マイページ参照'''
class MyPage(OnlyYouMixin, generic.DetailView):
    model = User
    template_name = 'accounts/my_page.html'

'''ユーザ登録'''
class SignUp(generic.CreateView):
    form_class = SignUpForm
    template_name = "accounts/user_form.html"

    def form_valid(self, form):
        user = form.save()
        return redirect('accounts:signup_done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Sign up"
        return context

'''ユーザ登録完了'''
class SignUpDone(generic.TemplateView):
    template_name = "accounts/signup_done.html"

'''登録情報更新'''
class UserUpdate(OnlyYouMixin, generic.UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'accounts/user_form.html'

    def get_success_url(self):
        return resolve_url('accounts:my_page', pk=self.kwargs['pk'])

    # contextデータ作成
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Update"
        return context

'''パスワード変更'''
class PasswordChange(PasswordChangeView):
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('accounts:password_change_done')
    template_name = 'accounts/user_form.html'

    # contextデータ作成
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Change Password"
        return context

'''パスワード変更完了'''
class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'


