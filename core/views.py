from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from .serializers import ProposalListSerializer, ProposalSerializer, ProposalCreateSerializer
    
from .models import Proposal



class ProposalListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        proposals = Proposal.objects.all()
        proposals_json = ProposalListSerializer(proposals, many=True)
        return Response(data=proposals_json.data)


class ProposalCreateAPIView(APIView):
    def post(self,request, *args, **kwargs):
        data = request.POST
        serializer = ProposalCreateSerializer(data=data)
        if serializer.is_valid():
            proposal = serializer.save()
            json_data = ProposalSerializer(instance=proposal)
            return Response(json_data.data, 201) 
        return Response(
            data={
                "message":"Data not valid",
                "errors": serializer.errors
            },
            status=400
        )

class ProposalRetreveAPIView(RetrieveAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer








