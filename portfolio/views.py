from django.shortcuts import render, redirect
from .models import Project, Skill, Profile, Service, Contact, Category 
from django.core.mail import send_mail
from django.conf import settings 
from .forms import ContactForm # This assumes you have created the portfolio/forms.py file

def home(request):
    # Fetches skills for the home page display
    skills = Skill.objects.all() 
    # Context processor already handles 'profile'
    return render(request, 'home.html', {'skills': skills})

def services(request):
    # Fetches all services for the services page
    services_list = Service.objects.all()
    return render(request, 'services.html', {'services': services_list})

def projects(request):
    # Fetches all categories for the filter bar
    categories = Category.objects.all()
    
    # 1. Get the category filter from the URL query parameters (e.g., ?category=Web Development)
    selected_category = request.GET.get('category', 'All') # Default to 'All'
    
    # 2. Start with all projects
    projects_list = Project.objects.all()
    
    # 3. Apply filtering if a specific category is selected
    if selected_category != 'All':
        # Filters projects that have the selected category name (case-insensitive match)
        projects_list = projects_list.filter(categories__name__iexact=selected_category)
        
    # Order the projects (optional)
    projects_list = projects_list.order_by('title')
    
    # 4. Pass the current filter state back to the template to highlight the active button
    return render(request, 'projects.html', {
        'projects': projects_list, 
        'categories': categories,
        'selected_category': selected_category 
    })

# --- CORRECT AND FUNCTIONAL CONTACT VIEW ---
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # 1. Save to Database
            contact_instance = form.save()
            
            # 2. Prepare Email Content
            subject = f"Lumi-Tech Portfolio Inquiry from {contact_instance.first_name}"
            body = (
                f"You have received a new message from your portfolio site:\n\n"
                f"Name: {contact_instance.first_name} {contact_instance.last_name}\n"
                f"Email: {contact_instance.email}\n"
                f"Phone: {contact_instance.phone or 'N/A'}\n\n"
                f"Message:\n{contact_instance.message}"
            )
            
            # 3. Send Email
            try:
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.RECIPIENT_ADDRESS], # Send email to your defined address
                    fail_silently=False,
                )
                # Redirect on success to prevent form re-submission
                return redirect('/contact/') 
            except Exception as e:
                # Print email error to the console for debugging
                print(f"Error sending email: {e}")
                
        # If form is invalid or email fails, proceed to render the page with errors
    
    else:
        # GET request: display an empty form
        form = ContactForm()
        
    # Determine if a success message should be shown after a successful POST and redirect
    return render(request, 'contact.html', {'form': form, 'show_success': request.GET.get('success', False)})