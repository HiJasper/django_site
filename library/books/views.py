from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Book
from forms import ContactForm
from django.core.mail import send_mail

def hello(request):
	print request.get_host()
	print request.META
	return HttpResponse("Hello world")

def display_meta(request, xx):
	values = request.GET.items()
	print request.GET.keys()
	values.sort()
	html = []
	for k, v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
	return HttpResponse('<table>%s</table>' % '\n'.join(html))
'''
def search_form(request):
	return render_to_response('search_form.html')
'''
def search(request):
	error = False
	if 'q' in request.GET:
		if request.GET['q']:
			q = request.GET['q']
			books = Book.objects.filter(title__icontains = q)
			return render_to_response("search_result.html", {"books": books, 'query': q})
		else:
			error = True
	return render_to_response('search_form.html', {'error': error})

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email', 'noreply@example.com'),
				['siteowner@example.com'],
			)
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm(
			initial={'subject': 'I love your site!'}
		)
	return render_to_response('contact_form.html', {'form': form})

def  named_groups(request, name, age):
	return HttpResponse('<table><tr><td>%s</td><td>%s</td></tr></table>' % (name, age))


def foobar_view(request, template_name):
	name = "Jasper"
	return render_to_response(template_name, {'name': name})
