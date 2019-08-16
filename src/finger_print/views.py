from rest_framework import (viewsets, status)
from rest_framework.response import Response
from rest_framework.decorators import action
from .enroll import *
from .serializers import FingerPrintScannerSerializer

class FingerPrintScannerViewset(viewsets.ModelViewSet):
    serializer_class = FingerPrintScannerSerializer
    queryset = Person
    @action(methods=['post'], detail=False, permission_classes=[],
            url_path='enroll', url_name='enroll')
    def enroll(self, request):
        if not request.data.get('name'):
            return Response("Name must be provided.", status=status.HTTP_404_NOT_FOUND)
        data = enroll(request.data['name'])
        if not data['error']:
            p = Person(name=request.data['name'], bio_id=int(data['pos']), credentials=data['cred_hash'])
            p.save()
            return Response(data, status=status.HTTP_200_OK)
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, permission_classes=[],
            url_path='user', url_name='user')
    def search(self, request):
        data = search_person()
        if not data['error']:
            person = Person.objects.get(bio_id=int(data['pos']))
            if person:
                return Response({"id" : person.id, "person_name" : person.name, "bio_id" : person.bio_id,
                             "accuracy_score" : data['accuracy_score']}, status=status.HTTP_200_OK)
            return Response("Data doesn't exist on DB", status=status.HTTP_404_NOT_FOUND)
        return Response(data, status=status.HTTP_404_NOT_FOUND)

    @action(methods=['delete'], detail=True, permission_classes=[],
            url_path='user', url_name='user')
    def delete(self, request, pk):
        person = Person.objects.filter(id=pk).values_list('bio_id', flat=True)
        if person:
            data = delete_person(person[0])
            if not data['error']:
                Person.objects.delete(id=pk)
                return Response("User successfully deleted", status=status.HTTP_200_OK)
            return Response(data, status=status.HTTP_403_FORBIDDEN)
        return Response("No record found with this id", status=status.HTTP_400_BAD_REQUEST)
