from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer
from rest_framework import status

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assign_doctor(request):
    serializer = PatientDoctorMappingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_mappings(request):
    mappings = PatientDoctorMapping.objects.all()
    serializer = PatientDoctorMappingSerializer(mappings, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_doctors_for_patient(request, patient_id):
    mappings = PatientDoctorMapping.objects.filter(patient_id=patient_id)
    serializer = PatientDoctorMappingSerializer(mappings, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_mapping(request, id):
    try:
        mapping = PatientDoctorMapping.objects.get(id=id)
    except PatientDoctorMapping.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)
    mapping.delete()
    return Response(status=204)
