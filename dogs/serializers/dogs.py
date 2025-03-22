from crum import get_current_user
from django.db import transaction
from rest_framework import serializers
from dogs.models.dogs import Dog


class DogListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = (
            'id',
            'owner',
            'name',
        )


class DogRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = (
            'id',
            'owner',
            'name',
            'gender',
            'breed',
            'date_of_birth',
            'photo'
        )


class DogCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = (
            'id',
            'name',
            'gender',
            'breed',
            'color',
            'date_of_birth',
            'photo',
            'extra',
        )

    def validate_name(self, value):
        value = value[0].upper() + value[1:].lower()
        return value

    def validate_gender(self, value):
        return value.upper()

    def validate_breed(self, value):
        value = value[0].upper() + value[1:].lower()
        return value

    def date_of_birth(self, value):
        return value

    def validate_color(self, value):
        value = value[0].upper() + value[1:].lower()
        return value

    def validate_extra(self, value):
        return value.lower()

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['owner'] = user
        return super().create(validated_data)


class DogPartialUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = (
            'id',
            'photo',
            'extra',
        )


class DogDestroySerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = (
            'id',
        )