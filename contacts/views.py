from django.shortcuts import render

def contact_form(request):
    context = {
        'test': 'hello'
    }

    return render(request, 'pages/contacts.html', context)

def send_success(request):
    pass