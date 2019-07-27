from django.contrib import admin
# Register your models here.
from user.models import Activity
from user.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from django.utils.translation import gettext, gettext_lazy as _
from django import forms




class BlogUserCreationForm(UserCreationForm):
	password1 = forms.CharField(label='密码',widget=forms.PasswordInput)
	password2 = forms.CharField(label='确认密码',widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('email',)


	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 != password2:
			raise forms.ValidationError("两次密码不一致")
		return password2

	def save(self,commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user

class BlogUserChangeForm(UserChangeForm):
	password = ReadOnlyPasswordHashField(
		label=_("Password"),
		help_text=_(
			"Raw passwords are not stored, so there is no way to see this "
			"user's password, but you can change the password using "
			"<a href=\"{}\">this form</a>."
		),
	)
	email = forms.EmailField(label="Email", widget=forms.EmailInput)

	class Meta:
		model = User
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

# class BlogUserAdmin(UserAdmin):
# 	form = BlogUserChangeForm
# 	add_form = BlogUserCreationForm
# 	list_display = ('id', 'nickname', 'username', 'email','slogon','gender')
# 	list_display_links = ('id', 'username')
# 	ordering = ('-id',)

admin.site.register(User,admin.ModelAdmin)
admin.site.register(Activity,admin.ModelAdmin)