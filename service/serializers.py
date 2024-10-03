from rest_framework import serializers

from service.models import Customer,Work


class CustomerSerializer(serializers.ModelSerializer):

    service_advisor = serializers.StringRelatedField(read_only=True)
    class Meta:

        model = Customer

        fields = "__all__"

        read_only_fields = ["id","service_advisor","created_date","updated_date","is_active"]


        
class WorkSerializer(serializers.ModelSerializer):

    customer_object = serializers.StringRelatedField(read_only=True)

    class Meta:

        model = Work

        fields = "__all__"

        read_only_fields = ["id","customer_object","created_date","updated_date","is_active"]


