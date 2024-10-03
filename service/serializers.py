from rest_framework import serializers

from service.models import Customer


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:

        model = Customer

        fields = "__all__"

        read_only_fields = ["id","service_advisor","created_date","updated_date","is_active"]

        