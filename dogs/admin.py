from django.contrib import admin

from dogs.models.dogs import Dog, DogGender


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


@admin.register(DogGender)
class DogGenderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
