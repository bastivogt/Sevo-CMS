from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic import FormView

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

from django.views.generic import UpdateView, DeleteView, TemplateView

from django.contrib.auth import get_user_model

User = get_user_model()



from .forms import SignUpForm, SignInForm

# Create your views here.


class IndexView(TemplateView):
    template_name = "sevo_user/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Sevo User index"
        })
        return context



class SignUpView(FormView):
    template_name = "sevo_user/sign_up.html"
    form_class = SignUpForm
    success_url = reverse_lazy("sevo_user:index")



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": _("Sign up"),
            "submit_label": _("Submit")
        })
        return context

    def form_valid(self, form):
        if form.is_valid():
            user = form.save(commit=False)
            form.save()
            login(request=self.request, user=user)
            messages.add_message(self.request, messages.SUCCESS, _("You are signed up and logged in!"))
        return super().form_valid(form)
    


class SignInView(SuccessMessageMixin, LoginView):
    template_name = "sevo_user/sign_in.html"
    next_page = reverse_lazy("sevo_user:index")
    success_message = _("You are signed in!")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": _("Sign in"),
            "submit_label": _("Submit")
        })
        return context



# sign out
# @login_required(login_url="sevo_user:sign_in")
# def sign_out(request):
#     logout(request)
#     messages.add_message(request, messages.SUCCESS, _("You are signed out!"))
#     return redirect("sevo_user:index")



class SignOutView(LoginRequiredMixin, SuccessMessageMixin, LogoutView):
    next_page = reverse_lazy("sevo_user:index")
    success_message = _("You are signed out!")




class ChangePasswordView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("sevo_user:index")
    template_name = "sevo_user/password_change.html"
    title = _("Password change")
    success_message = _("Password changed")

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        #context["submit_label"] = _("Submit")
        context.update({
            "submit_label": _("Submit")
        })
        return context


class ChangeUserData(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = User
    fields = [
        "username",
        "first_name",
        "last_name"
    ]
    template_name = "sevo_user/update.html"
    success_message = _("Userdata changed!")
    success_url = reverse_lazy("sevo_user:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Userdata change",
            "submit_label": _("Submit")
        })
        return context
    

class DeleteUserView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = User
    template_name = "sevo_user/delete.html"
    success_message = _("User deleted!")
    success_url = reverse_lazy("sevo_user:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Delete account",
            "submit_label": _("Delete")
        })
        return context
    



class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'sevo_user/password_reset.html'
    email_template_name = 'sevo_user/password_reset_email.html'
    subject_template_name = 'sevo_user/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('sevo_user:index')
    
