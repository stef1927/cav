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

# class MotherSerializer(serializers.ModelSerializer):
#     children = serializers.PrimaryKeyRelatedField(many=True)
#     #children = serializers.HyperlinkedIdentityField('children', view_name='children-list', lookup_field='children')
#     #donations = serializers.HyperlinkedIdentityField('donations', view_name='donations-list', lookup_field='donations')
#     #income = serializers.ModelSerializer.
#     #'income', 'fixed_expenditures', 'operator',
#
#     class Meta:
#         model = Mothers
#         fields = fields = ('id', 'surname', 'name', 'date_of_birth', 'place_of_birth', 'civil_status',
#                            'residency', 'origin_country', 'highest_academic_achievement', 'job',
#                            'registration_date', 'husband_surname', 'husband_job', 'city', 'address',
#                            'phone_1', 'phone_2', 'notes')


class ChildSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="get_name")
    date_of_birth = serializers.CharField(source="get_date_of_birth")
    sex = serializers.CharField(source="get_sex")
    mother_name = serializers.StringRelatedField(source='mother')
    mother_link = serializers.HyperlinkedRelatedField(source='mother', read_only='True', view_name='mother-details')

    class Meta:
        model = Children
        fields = ('id', 'name', 'date_of_birth', 'sex', 'mother_name', 'mother_link')


class DonationSerializer(serializers.ModelSerializer):
    amount = serializers.FloatField(source='get_amount', read_only=True)
    mother_name = serializers.StringRelatedField(source='mother')
    mother_link = serializers.HyperlinkedRelatedField(source='mother', read_only='True', view_name='mother-details')
    operator = serializers.StringRelatedField()

    class Meta:
        model = Donations
        fields = ('id', 'date_of_donation', 'requested', 'given', 'amount', 'mother_name', 'mother_link', 'operator')


class OperatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Operators
        fields = ('id', 'name')
