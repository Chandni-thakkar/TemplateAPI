from rest_framework import serializers
from .models import Template, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TemplateSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)




    class Meta:
        model = Template
        fields = '__all__'

    def create(self, validated_data):
        users_data = validated_data.pop('users')
        template = Template.objects.create(**validated_data)
        for user_data in users_data:
            user = User.objects.create(**user_data)
            template.users.add(user)
        return template

    def update(self, instance, validated_data):
        users_data = validated_data.pop('users')
        instance.template_version = validated_data.get('template_version', instance.template_version)
        instance.channel = validated_data.get('channel', instance.channel)
        instance.save()

        instance.users.clear()
        for user_data in users_data:
            user = User.objects.create(**user_data)
            instance.users.add(user)

        return instance
