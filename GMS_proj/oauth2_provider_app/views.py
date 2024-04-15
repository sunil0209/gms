from oauth2_provider.models import get_application_model
from django.http import HttpResponseRedirect
from django.urls import reverse

def google_login(request):
    Application = get_application_model()
    app = Application.objects.get(name="Google OAuth2")
    redirect_uri = reverse('oauth2_provider:authorize')
    url = app.authorization_url(redirect_uri)
    return HttpResponseRedirect(url)

def google_callback(request):
    code = request.GET.get('code')
    # Exchange code for access token
    # Handle user authentication and creation
    ...
