from django.contrib.auth.models import User,update_last_login
from rest_framework import serializers



class userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields=['url','username','email','last_login','date_joined']