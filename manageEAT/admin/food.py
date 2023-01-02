from django.contrib import admin

from manageEAT.models.food import Food


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}
