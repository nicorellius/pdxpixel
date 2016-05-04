from django import forms


# class LoginForm(forms.Form):
#
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):

    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'name': 'username',
                'placeholder': 'Username',
                'autofocus': 'autofocus',
            }
        )
    )

    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'password',
                'name': 'password',
                'placeholder': 'Password',
            }
        )
    )

    # remember = forms.BooleanField(
    #     required=False,
    #     widget=forms.CheckboxInput(
    #         attrs={
    #             'class': 'align-checkbox',
    #             'name': 'remember',
    #         }
    #     )
    # )