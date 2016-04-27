from django.shortcuts import render
from master.models import MasterRepaymentType, MasterStatus,MasterAuthor
# Create your views here.
from django.http import Http404

from master.serializers import MasterRepaymentSerializer,MasterAuthorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render,render_to_response,get_object_or_404
from django.template import RequestContext
from rest_framework.parsers import JSONParser
from rest_framework import viewsets, filters

class MasterRepaymentList(APIView):
    parser_classes = (JSONParser,)
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
    parser_classes = (JSONParser,)
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
def home(request):
    return render_to_response('master/home.html',context_instance=RequestContext(request))

class ChildDetailViewSet(viewsets.ModelViewSet):
    queryset = MasterAuthor.objects.all()
    serializer_class = MasterAuthorSerializer
    filter_backends = (filters.SearchFilter,)
    