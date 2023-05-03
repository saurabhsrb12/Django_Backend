from rest_framework import generics, filters
from .models import Work, Artist
from .serializers import WorkSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User 
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

class WorkList(generics.ListAPIView):
    serializer_class = WorkSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['artists__name']
    ordering_fields = ['id', 'link']

    def get_queryset(self):
        queryset = Work.objects.all()
        artist_name = self.request.query_params.get('artist', None)
        work_type = self.request.query_params.get('work_type', None)

        if artist_name is not None:
            queryset = queryset.filter(artists__name__icontains=artist_name)
        if work_type is not None:
            queryset = queryset.filter(work_type=work_type)

        return queryset

class WorkDetail(generics.RetrieveAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer



class RegisterAPI(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
