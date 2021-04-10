from rest_framework import serializers
from .models import createpost


class serialization(serializers.ModelSerializer):
    class Meta:
        model = createpost
        fields = '__all__'
