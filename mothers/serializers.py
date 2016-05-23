from rest_framework import serializers

from models import Mothers, Children, Donations, Operators


class MotherSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    absolute_url = serializers.CharField(source='get_absolute_url', read_only=True)
    num_children = serializers.IntegerField(source='get_num_children', read_only=True)

    class Meta:
        model = Mothers
        fields = ('full_name', 'absolute_url', 'num_children',
                  'name', 'surname', 'date_of_birth', 'place_of_birth',
                  'registration_date', 'civil_status','origin_country', 'residency')


class ChildSerializer(serializers.ModelSerializer):
    mother_name = serializers.StringRelatedField(source='mother', read_only='True')

    class Meta:
        model = Children
        lookup_field = 'id'
        fields = ('id', 'name', 'date_of_birth', 'sex', 'mother', 'mother_name')


class DonationSerializer(serializers.ModelSerializer):
    mother_name = serializers.StringRelatedField(source='mother')
    operator_name = serializers.StringRelatedField(source='operator')

    class Meta:
        model = Donations
        lookup_field = 'id'
        fields = ('id', 'date_of_donation', 'requested', 'given', 'amount',
                  'mother', 'mother_name', 'operator', 'operator_name')


class OperatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Operators
        fields = ('id', 'name')


class MotherDetailsSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    absolute_url = serializers.CharField(source='get_absolute_url', read_only=True)
    children = ChildSerializer(read_only=True, many=True)
    donations = DonationSerializer(read_only=True, many=True)
    operator = OperatorSerializer(read_only=True, many=False)

    class Meta:
        model = Mothers
        fields = fields = ('full_name',  'absolute_url', 'children', 'donations', 'operator',
                           'id', 'surname', 'name', 'date_of_birth', 'place_of_birth', 'civil_status',
                           'residency', 'origin_country', 'highest_academic_achievement', 'job',
                           'registration_date', 'husband_surname', 'husband_job', 'city', 'address',
                           'phone_1', 'phone_2', 'notes')
