"""
Views for the user API.
"""
from django.contrib.auth.decorators import login_required
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import UserSerializer, AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import HttpResponse
from django.utils import timezone
from django.db.models.functions import ExtractYear
from datetime import datetime
import matplotlib.pyplot as plt
import io
from core.models import User
from django.views.generic import TemplateView
import matplotlib
matplotlib.use('Agg')

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""

    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username  
        })

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""

    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user


from rest_framework.decorators import api_view

def generate_age_group_distribution_image():
    current_year = datetime.now().year
    age_groups = {
        "1-20": 0,
        "21-40": 0,
        "41+": 0,
    }

    users = User.objects.annotate(
        age=current_year - ExtractYear('date_of_birth')
    ).filter(date_of_birth__isnull=False)

    for user in users:
        if 1 <= user.age <= 20:
            age_groups["1-20"] += 1
        elif 21 <= user.age <= 40:
            age_groups["21-40"] += 1
        else:
            age_groups["41+"] += 1

    # Generate the bar graph
    fig, ax = plt.subplots()
    ax.bar(age_groups.keys(), age_groups.values(), color='blue')
    ax.set_xlabel('Age Groups')
    ax.set_ylabel('Number of Users')
    ax.set_title('User Distribution by Age Group')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)

    return buf.getvalue()

@api_view(['GET'])
# @login_required
def age_group_distribution_view(request):
    image_data = generate_age_group_distribution_image()
    return HttpResponse(image_data, content_type='image/png')

@api_view(['GET'])
# @login_required
def age_group_distribution_download_view(request):
    image_data = generate_age_group_distribution_image()
    response = HttpResponse(image_data, content_type='image/png')
    response['Content-Disposition'] = 'attachment; filename="age_group_distribution.png"'
    return response