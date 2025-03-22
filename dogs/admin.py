from django.contrib import admin

from dogs.models.dogs import Dog


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'gender',
        'breed',
        'color',
        'date_of_birth',
        'photo',
        'owner',
        'extra',
    )
