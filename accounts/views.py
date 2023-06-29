from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from .forms import (
    UserAuthenticationForm,
    UserRegistrationForm,
    UserForm,
    UserProfileForm,
    UserChangePasswordForm

)
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


class LoginView(View):
    form_class = UserAuthenticationForm
    template_name = 'accounts/login.html'

    def get(self, request):
        next_url = request.GET.get('next')
        form = self.form_class(initial={
            'next_url': next_url
        })
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            next_url = form.cleaned_data.get('next_url')
            if next_url:
                return redirect(next_url)
            return redirect('home_page')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


class RegistrationView(View):
    form_class = UserRegistrationForm
    template_name = 'accounts/registration.html'

    def get(self, request):
        form = self.form_class()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('LoginView')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('home_page')


@method_decorator(login_required, name="dispatch")
class ProfileView(View):
    """ User Profile View """
    form_class = UserForm
    profile_form_class = UserProfileForm
    change_password_class = UserChangePasswordForm
    template_name = 'accounts/profile.html'

    def get(self, request):
        user = User.objects.get(id=request.user.id)
        user_form = self.form_class(instance=user)
        user_profile_form = self.profile_form_class(instance=user.user_detail)
        user_change_password = self.change_password_class(user)
        context = {
            'user_form': user_form,
            'user_profile_form': user_profile_form,
            'user_change_password': user_change_password

        }
        return render(request, self.template_name, context)

    def post(self, request):
        print(request.POST)
        user = User.objects.get(id=request.user.id)
        user_form = self.form_class(request.POST, instance=user)
        user_profile_form = self.profile_form_class(
            request.POST, instance=user.user_detail)
        user_change_password = self.change_password_class(
            request.user, request.POST)
        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()

        """Change Password"""
        if user_change_password.is_valid():
            user_change_password.save()
            update_session_auth_hash(request, user)
            messages.success(
                request, "Your password was successfully updated!")
            return redirect("home_page")
        context = {
            'user_form': user_form,
            'user_profile_form': user_profile_form,
            'user_change_password': user_change_password

        }
        return render(request, self.template_name, context)
