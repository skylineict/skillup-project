from django.template.loader import render_to_string
from django.shortcuts import render, HttpResponse
from user.models import Profile
from .home import login_required_homepage
import pdb
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa





@login_required_homepage
def pdfexportfiles(request):
    
    template_path = 'ticket_profiles.html'
    profile = Profile.objects.get(user=request.user)

    context = {'profile': profile}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="products_report.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    
 
  

@login_required_homepage
def Ticketfile(request):
    user = request.user
    profiles = Profile.objects.get(user=user)
    # pdb.set_trace()
    return render(request, 'ticket.html', {'profile': profiles})
