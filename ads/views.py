from django.db.models import Q
from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from .models import Ad
from .serializers import AdSerializer
from rest_framework import status
from .pagination import StandardResultSetPagination
from rest_framework.permissions import IsAuthenticated
from .permissions import IsPublisherOrReadOnly


class AdListView(APIView, StandardResultSetPagination):
    serializer_class = AdSerializer

    def get(self, request):
        queryset = Ad.objects.filter(is_public=True)
        result = self.paginate_queryset(queryset, request)
        serializer = AdSerializer(instance=result, many=True)
        return self.get_paginated_response(serializer.data)


class AdCreateView(APIView):
    serializer_class = AdSerializer
    parser_classes = (MultiPartParser,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = AdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['publisher'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdDetailView(APIView):
    serializer_class = AdSerializer
    permission_classes = (IsAuthenticated, IsPublisherOrReadOnly)
    parser_classes = (MultiPartParser,)

    def get_object(self):
        obj = get_object_or_404(Ad.objects.all(), id=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, pk):
        obj = self.get_object()
        serializer = AdSerializer(instance=obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        obj = self.get_object()
        serializer = AdSerializer(data=request.data, instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = self.get_object()
        obj.delete()
        return Response({'response': 'Deleted'}, status=status.HTTP_200_OK)


class AdSearchView(APIView, StandardResultSetPagination):
    serializer_class = AdSerializer
    def get(self, request):
        q = request.GET.get('q')
        queryset = Ad.objects.get(Q(title=q | Q(caption=q)))
        result = self.paginate_queryset(queryset, request)
        serializer = AdSerializer(instance=result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
