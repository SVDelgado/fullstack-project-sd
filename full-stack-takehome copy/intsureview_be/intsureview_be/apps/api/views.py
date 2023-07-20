from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from intsureview_be.apps.api.serializers import UserSerializer, GroupSerializer, ReactSerializer
from . models import *
from . serializers import *



#class UserViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint that allows users to be viewed or edited.
#    """
#
#    queryset = User.objects.all().order_by("-date_joined")
#    serializer_class = UserSerializer
#    permission_classes = [permissions.IsAuthenticated]


#class GroupViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint that allows groups to be viewed or edited.
#    """
#
#    queryset = Group.objects.all()
#    serializer_class = GroupSerializer
#    permission_classes = [permissions.IsAuthenticated]

class ReactView(APIView):
    serializer_class = ReactSerializer

    def get(self, request):
        detail = [ {"name": detail.name, "detail": detail.detail}
        for detail in React.objects.all()]
        return Response(detail)
    
    def post(self, request):
        serializer = ReactSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)