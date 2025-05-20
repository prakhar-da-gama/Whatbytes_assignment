from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Patient
from .serializers import PatientSerializer
from rest_framework import status

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_patient(request):
    data = request.data.copy()
    data['user'] = request.user.id
    serializer = PatientSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_patients(request):
    patients = Patient.objects.filter(user=request.user)
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def patient_detail(request, id):
    try:
        patient = Patient.objects.get(id=id, user=request.user)
    except Patient.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)

    if request.method == 'GET':
        return Response(PatientSerializer(patient).data)

    elif request.method == 'PUT':
        serializer = PatientSerializer(patient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        patient.delete()
        return Response(status=204)
