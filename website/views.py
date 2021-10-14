#python -m smtpd -n -c DebuggingServer localhost:1025
#$ git config --global user.name "Your Name"
#$ git config --global user.email "you@youraddress.com"
#$ git config --global push.default matching
#$ git config --global alias.co checkout
#$ git init
from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        name = request.POST['contact_name']
        email = request.POST['contact_email']
        message = request.POST['contact_message']

        contacting = "Name: " + name + \
                  " - Message:" + message + \
                  " - Email:" + email

        # send an email
        send_mail(
            'Contact',  # subject
            contacting, # message
            email, # from email
            ['ibehjohnweb@gmail.com'], # to email
            fail_silently=False,
            )



        return render(request, 'contact.html', {'name': name})

    else:
        return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})


def dj(request):
    return render(request, 'dj.html', {})



def bookings(request):
    if request.method == "POST":
        name = request.POST['contact_name']
        email = request.POST['contact_email']
        number = request.POST['contact_number']
        services = request.POST['contact_services']
        address = request.POST['contact_address']
        message = request.POST['contact_message']


        booking ="Name: " + name +  \
                 " - Phone: " + number + \
                 " - Service: " + services + \
                 " - Address: " + address +\
                 " - Message: " + message +\
                 " - Email:" + email
        # send an email
        send_mail(
            'Booking Request', # subject
            booking, # message
            email,  # from email
            ['ibehjohnweb@gmail.com'], # to email
            fail_silently=False,
            )

        return render(request, 'bookings.html', {
            'name': name,
            'email': email,
            'number': number,
            'services': services,
            'address': address,
            'message': message,
            })

    else:
        return render(request, 'bookings.html', {})


def engineering(request):
    return render(request, 'ee.html', {})


def web(request):
    return render(request, 'web.html', {})


def eeservices(request):
    return render(request, 'eeservices.html', {})



def djservices(request):
    return render(request, 'djservices.html', {})


def webservices(request):
    return render(request, 'webservices.html', {})