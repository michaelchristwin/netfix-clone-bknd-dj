from rest_framework import generics, mixins
from .serializers import SignupSerializer
from .models import SignupUser


class UsersView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView,):
    serializer_class = SignupSerializer
    queryset = SignupUser.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
