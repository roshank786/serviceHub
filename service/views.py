from django.shortcuts import render

from rest_framework import generics,authentication,permissions

from service.models import Customer,Work

from service.serializers import CustomerSerializer,WorkSerializer

# Create your views here.


class CustomerListCreateView(generics.ListCreateAPIView):

    queryset = Customer.objects.all()

    serializer_class = CustomerSerializer

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]


    def perform_create(self, serializer):

        return serializer.save(service_advisor = self.request.user)



class CustomerRetreiveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Customer.objects.all()

    serializer_class = CustomerSerializer

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]



class WorkCreateView(generics.CreateAPIView):

    serializer_class = WorkSerializer

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]



    def perform_create(self, serializer):
        
        id = self.kwargs.get("pk")

        customer_obj = Customer.objects.get(id=id)

        return serializer.save(customer_object = customer_obj)

