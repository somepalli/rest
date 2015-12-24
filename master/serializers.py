from master.models import MasterRepaymentType,MasterStatus

from rest_framework import serializers
from rest_framework.compat import six

class MasterRepaymentSerializer(serializers.ModelSerializer):
	# fk_status = serializers.Field(source='master_status.type', read_only=True)
	fk_status = serializers.PrimaryKeyRelatedField(queryset=MasterStatus.objects.all())
	# fk_status = serializers.RelatedField(many=True,read_only=True)

	# fk_status = serializers.ChoiceField(queryset=MasterStatus.objects.all(), default='None')
	class Meta:
		model = MasterRepaymentType
		# fields = ('id', 'repayment_type_name', 'fk_status', 'last_modified_date', 'last_modified_by')
		# depth = 2
