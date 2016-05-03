from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.views.generic.base import View
from django.contrib import messages

from .forms import LoginForm


class LoginView(View):

    form_class = LoginForm
    template_name = 'registration/login.html'
    success_url = '/blog/'
    context_object_name = 'form'

    def get(self, request):

        form = self.form_class()

        return render(request, self.template_name, {
            'form': form
        })

    def post(self, request):

        error = ''
        form = self.form_class(request.POST)

        if form.is_valid():

            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])

            if user is not None:

                if user.is_active:

                    login(request, user)

                    messages.add_message(
                        request,
                        messages.INFO,
                        'User {0} successfully logged in.'.format(user)
                    )

                    return HttpResponseRedirect(self.success_url)

                else:
                    error = "User is valid, but not active. " \
                            "Contact the administrator to enable your account."

            else:
                error = "Incorrect username or password. Please try again."

        return render(request, self.template_name, {
            'form': form,
            'error': error,
        })

