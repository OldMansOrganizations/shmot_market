from django.contrib import admin
from catalog.models import Products, Categories, SubCategories


@admin.register(Products)
class PersonAdmin(admin.ModelAdmin):
	pass


@admin.register(Categories)
class PersonAdmin(admin.ModelAdmin):
	pass


@admin.register(SubCategories)
class PersonAdmin(admin.ModelAdmin):
	pass
