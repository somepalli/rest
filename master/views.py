from django.shortcuts import render
from master.models import MasterRepaymentType, MasterStatus
# Create your views here.
from django.http import Http404

from master.serializers import MasterRepaymentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MasterRepaymentList(APIView):
	def get(self, request, format=None):
		users = MasterRepaymentType.objects.all()
		serializer = MasterRepaymentSerializer(users, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = MasterRepaymentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		user = self.get_object(pk)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class MasterRepaymentDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return MasterRepaymentType.objects.get(pk=pk)
        except MasterRepaymentType.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        user = MasterRepaymentSerializer(user)
        return Response(user.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = MasterRepaymentSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)