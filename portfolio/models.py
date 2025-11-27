from django.db import models

# 1. HOME PAGE DATA
class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, help_text="e.g. Full Stack Developer")
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='profile/')
    about_text = models.TextField(blank=True, help_text="Short bio for the home page")

    # NEW: Social Media Links (Optional)
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=50)
    # You can use an icon class (like FontAwesome) or upload an image
    icon_image = models.ImageField(upload_to='skills/', blank=True, null=True)
    
    def __str__(self):
        return self.name


# 2. SERVICES PAGE
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # NEW FIELD ADDED: Image for the service card
    service_image = models.ImageField(upload_to='services/', help_text="Image outlining the service", null=True, blank=True)
    
    def __str__(self):
        return self.title


# NEW MODEL: Category for Project Tags (e.g., Websites, UI/UX)
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

# 3. PROJECTS PAGE (UPDATED)
class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/')
    short_description = models.TextField()
    link = models.URLField(blank=True)
    
    # NEW FIELD: Allows projects to be assigned multiple categories/tags
    categories = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.title

# 4. CONTACTS PAGE (Form Submissions)
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
