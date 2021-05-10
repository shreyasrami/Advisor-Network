from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer, AdvisorSerializer, BookingSerializer
from django.contrib import auth
from .models import User, Advisor, BookedCalls
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK

# Create your views here.


class RegisterUserView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self,request,*args,**kwargs):
        
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            data = {
                'token': str(refresh.access_token),
                'user_id':user.id
            }
            return Response(data,status=HTTP_200_OK)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)
        
class LoginUserView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self,request,*args,**kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = auth.authenticate(email=email,password=password)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                data = {
                    'token': str(refresh.access_token),
                    'user_id':user.id
                }
                return Response(data,status=HTTP_200_OK)
            else:                                                                                                    
                return Response({"status":"401_AUTHENTICATION_ERROR"})

        else:
            return Response(status=HTTP_400_BAD_REQUEST)


class AdvisorView(generics.GenericAPIView):
    
    serializer_class = AdvisorSerializer
    queryset = Advisor.objects.all()
    permission_classes = [AllowAny,]


    def get(self,request,*args,**kwargs):
        advisors = Advisor.objects.all()
        serializer = AdvisorSerializer(advisors,many=True)
    
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):

        serializer = AdvisorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"200_OK"},status=HTTP_200_OK)
        else:
            return Response({"status":"400_BAD_REQUEST"},status=HTTP_400_BAD_REQUEST)



    
class AllBookingsView(generics.GenericAPIView):
    
    serializer_class = BookingSerializer
    queryset = BookedCalls.objects.all()
    permission_classes = [AllowAny,]

    def get(self,request,*args,**kwargs):
        bookings = list(BookedCalls.objects.filter(user=kwargs['user_id']).values())

        for booking in bookings:
            advisor = Advisor.objects.get(id=booking['advisor_id'])
            del booking['user_id']
            del booking['advisor_id']
            booking['advisor_name'] = advisor.advisor_name
            booking['advisor_profile_pic'] = advisor.photo_url 
            booking['advisor_id'] = advisor.id
        
        return Response(bookings,status=HTTP_200_OK)


class MakeBookingView(generics.GenericAPIView):
    serializer_class = BookingSerializer
    queryset = BookedCalls.objects.all()
    permission_classes = [AllowAny,]

    def post(self,request,*args,**kwargs):

        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(id=kwargs['user_id'])
            advisor = Advisor.objects.get(id=kwargs['advisor_id'])
            serializer.save(user=user,advisor=advisor)
            return Response({"status":"200_OK"},status=HTTP_200_OK)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)



    
    

