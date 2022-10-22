from rest_framework import serializers
from .models import question , choice 


class qSerializer(serializers.ModelSerializer):
    class Meta:
        model=question
        fields=('qText','pupDate')

class chSerializer(serializers.ModelSerializer):
    class Meta:
        model=choice
        fields=('chText','votes','question')