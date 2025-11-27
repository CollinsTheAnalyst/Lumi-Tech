# File: portfolio/admin.py
from django.contrib import admin
from .models import Profile, Skill, Service, Project, Contact, Category # Import Category

# This configures how the lists look in the admin panel
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email', 'phone')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)


# Register the new Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Update the ProjectAdmin to display the categories field nicely
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # This list_display requires a method to show multiple categories
    list_display = ('title', 'display_categories', 'link')
    
    # Method to display the categories in the admin list view
    def display_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    display_categories.short_description = 'Categories'

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'submitted_at', 'message')
    readonly_fields = ('submitted_at',) # Prevent editing the timestamp