from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from users.models import CustomUser
from rest_framework import generics, status
from .serializers import CustomUserSerializer
from rest_framework.response import Response
from .permissions import IsOwner


from drf_yasg.utils import swagger_auto_schema

# class RegisterAPIView(generics.CreateAPIView):
#     serializer_class = CustomUserSerializer
#     queryset = CustomUser.objects.all()
#     permission_classes = [AllowAny]

class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=CustomUserSerializer)
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveUpdateDeleteAPIView(APIView):
    permission_classes = [IsOwner]


    def get_object(self, id):
        try:
            user = CustomUser.objects.get(id=id)
            return user
        except CustomUser.DoesNotExist:
            return Response({'message': "Not Found"}, status=status.HTTP_404_NOT_FOUND)


    def get(self, request, id):
        user = self.get_object(id)

        self.check_object_permissions(request, user)

        serializer = CustomUserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @swagger_auto_schema(request_body=CustomUserSerializer)
    def put(self, request, id):
        user = self.get_object(id)

        self.check_object_permissions(request, user)

        serializer = CustomUserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            user.set_password(request.data['password'])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(request_body=CustomUserSerializer)
    def patch(self, request, id):
        user = self.get_object(id)

        self.check_object_permissions(request, user)

        serializer = CustomUserSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            if 'password' in request.data:
                user.set_password(request.data['password'])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        user = self.get_object(id)

        self.check_object_permissions(request, user)

        user.delete()
        return Response({'message': 'Successfully deleted user'}, status=status.HTTP_204_NO_CONTENT)


# class UserAPIView(generics.ListAPIView):
#     serializer_class = CustomUserSerializer
#     queryset = CustomUser.objects.all()
#     permission_classes = [IsAuthenticated, IsAdminUser]

