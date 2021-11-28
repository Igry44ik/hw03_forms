from django.forms import ModelForm

from django import forms

from .models import Post


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ("text", "group")
        label = {
            "text": "Текст поста",
            "group": "Группа",
        }


def clean_text(self):
    data = self.cleaned_data["text"]
    if data == "":
        raise forms.ValidationError('Введите какой-нибуль текст!')
    return data
