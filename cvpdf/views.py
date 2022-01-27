from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration

from about.models import About, Tech, TechType
from education.models import Education, Certificate
from carreer.models import Carreer

def cv_completo(request):
    """ Genera el CV completo """

    url = request.build_absolute_uri().replace("/cvpdf/cv_completo", "")
    print(url)
    about = About.objects.all()[0]
    tech_types = TechType.objects.all()
    technologies = Tech.objects.filter(profesional_use=True)
    educations = Education.objects.all()
    certificates = Certificate.objects.all()
    carreers = Carreer.objects.all()
    
    context = {
        'url': url,
        'about': about,
        'tech_types': tech_types,
        'technologies': technologies,
        'educations': educations,
        'certificates': certificates,
        'certificates_length': len(certificates),
        'carreers': carreers
    } 

    html = render_to_string("cvpdf/cv_completo.html", context)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "inline; cv-guillermo-granados-gomez.pdf"

    font_config = FontConfiguration()

    HTML(string=html).write_pdf(response, font_config=font_config)

    return response
