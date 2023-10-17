from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['Get','Post'])
def user_list_api(request):
    all_users = User.objects.all()
    data = UserSerializer(all_users, many=True).data
    return Response({'data': data})