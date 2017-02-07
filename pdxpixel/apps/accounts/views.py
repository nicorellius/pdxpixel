import logging

from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import View
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from core.receivers import on_user_logged_out
from core.util import get_timestamp

from .forms import LoginForm
from .models import UserProfile


logger = logging.getLogger(__name__)


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

                    logger.info(
                        '[{0}] POST user logged in: {1}'.format(
                            get_timestamp(), request.user)
                    )

                    # TODO -- why is this not used rather than above message.
                    # messages.success(request, 'logged in successfully')

                    if user.is_staff:
                        return HttpResponseRedirect('/admin/')

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


class LogoutView(View):

    template_name = 'registration/logged_out.html'

    def get(self, request):

        logger.info('[{0}] {1}'.format(
            get_timestamp(), on_user_logged_out)
        )

        response = logout(request)

        return render(response, self.template_name)


class ProfileView(View):

    model = UserProfile
    template_name = 'accounts/profile.html'

    @method_decorator(login_required)
    def get(self, request):

        if request.user.username:

            profile = get_object_or_404(self.model, user=request.user)

            data_dict = {
                'profile': profile,
            }

            return render(request, self.template_name, data_dict)

