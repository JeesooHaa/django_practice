# 회원정보 수정 필요없음 
# # UserChangeForm
from django.contrib.auth.forms import UserChangeForm
# get_user_model
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        #
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', ]
