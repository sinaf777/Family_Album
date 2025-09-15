from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.auth.forms import AuthenticationForm

USERNAME_VALIDATOR = RegexValidator(
    regex=r'^[\w.@+-]+$',
    message="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
)

INPUT_CLASS = "w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-yellow-500"

class SignUpForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        validators=[USERNAME_VALIDATOR],
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': INPUT_CLASS})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': INPUT_CLASS})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': INPUT_CLASS})
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': INPUT_CLASS}),
        label="Confirm Password"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('password_confirm'):
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data

# Optional: Login form with same styling
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': INPUT_CLASS})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': INPUT_CLASS})
    )
