from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from .models import EventDetails
from EventParticipant_module.models import EventApplication

# Create your views here.
def Eventpost(request):
    return render(request, 'EventManager_module/eventpost.html')

from django.http import HttpResponseBadRequest

def add_event_details(request):
    if request.method == 'POST':
        event_title = request.POST.get('EventTitle')
        event_type = request.POST.get('EventType')
        event_location = request.POST.get('EventLocation')
        required_skills = request.POST.get('RequiredSkills')

        # Check if all required fields are provided
        if not all([event_title, event_type, event_location, required_skills]):
            return HttpResponseBadRequest("All required fields must be provided.")

        # Optional fields
        benefits = request.POST.get('benefits', 'Your Default Value')
        registration_amount = request.POST.get('RegistrationAmount', 0.00)

        event_details = EventDetails(
            event_title=event_title,
            event_type=event_type,
            benefits=benefits,
            event_location=event_location,
            required_skills=required_skills,
            registration_amount=registration_amount,
        )
        event_details.save()
        return render(request, 'EventManager_module/Eventdatainserted.html')
    return render(request, 'EventManagerHomepage.html')

def view_event_details(request):
    event_details_list = EventDetails.objects.all()
    return render(request, 'EventManager_module/view_event_details.html', {'event_details_list': event_details_list})

def edit_event_details(request, event_id):
    event_details = get_object_or_404(EventDetails, id=event_id)
    if request.method == 'POST':
        event_details.event_title = request.POST.get('eventTitle')
        event_details.registration_amount = request.POST.get('registrationAmount')
        event_details.event_type = request.POST.get('eventType')
        event_details.benefits = request.POST.get('benefits')
        event_details.event_location = request.POST.get('EventLocation')
        event_details.required_skills = request.POST.get('requiredSkills')
        event_details.save()
        return redirect('EventManager_module:view_event_details')
    return render(request, 'EventManager_module/edit_event_details.html', {'event_details': event_details})

def delete_event_details(request, event_id):
    event_details = get_object_or_404(EventDetails, id=event_id)
    if request.method == "POST":
        event_details.delete()
        return redirect('EventManager_module:view_event_details')
    return render(request, 'EventManager_module/delete_event_details.html', {'event_details': event_details})

def event_application_list(request):
    event_applications = EventApplication.objects.all()
    return render(request, 'EventManager_module/event_application_list.html', {'event_applications': event_applications})

def KLU(request):
    return render(request, 'KLU.html')

def KLH(request):
    return render(request, 'KLH.html')

def vitap(request):
    return render(request, 'vitap.html')

def vitchennai(request):
    return render(request, 'vitchennai.html')

def srm(request):
    return render(request, 'srm.html')

def gitam(request):
    return render(request, 'gitam.html')

def gmrit(request):
    return render(request, 'gmrit.html')

def AU(request):
    return render(request, 'AU.html')

def accept_application(request, event_application_id):
    event_application = get_object_or_404(EventApplication, id=event_application_id)

    # Update the application status
    event_application.status = 'Accepted'
    event_application.save()

    # Retrieve associated EventDetails
    event_details = event_application.event_details

    # Get additional information (username and registered event)
    user_email = event_application.email  # Assuming email is used for identifying the user

    # Send acceptance email with user email and registered event details
    send_mail(
        'Application Accepted',
        f'Congratulations! "{event_application.name}" Your application for the event "{event_details.event_title}" has been accepted.',
        'sakethkunuku205@gmail.com',  # Sender's email address
        [user_email],  # Recipient's email address
        fail_silently=False,
    )

    # Remove the application from the list
    event_application.delete()

    return redirect('EventManager_module:event_application_list')

def reject_application(request, event_application_id):
    event_application = get_object_or_404(EventApplication, id=event_application_id)

    # Update the application status
    event_application.status = 'Rejected'
    event_application.save()

    # Retrieve associated EventDetails
    event_details = event_application.event_details

    # Send rejection email
    send_mail(
        'Application Rejected',
        f'Dear "{event_application.name}", We regret to inform you that your application for the event "{event_details.event_title}" has been rejected.',
        'sakethkunuku205@gmail.com',  # Sender's email address
        [event_application.email],  # Recipient's email address
        fail_silently=False,
    )

    # Remove the application from the list
    event_application.delete()

    return redirect('EventManager_module:event_application_list')

