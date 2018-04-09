from django.shortcuts import render
from django.core.mail import EmailMessage
from contactform.forms import ContactForm
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template

def contactform(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')
            
            template = get_template('contactform/contact_template.txt')
            context = Context({'contact_name': contact_name, 'contact_email': contact_email, 'form_content': form_content})
            content = template.render({'contact_name': contact_name, 'contact_email': contact_email, 'form_content': form_content})

            email = EmailMessage("New contact form submission", content, "Your website" + '', ['vietnamezul@gmail.com'], headers = {'Reply-To': contact_email})
            email.send()
            return redirect('thanks')

    return render(request, 'contactform/contactform.html', {'form': form_class})
    
def thanks(request):
    return render(request, "contactform/thanks.html")