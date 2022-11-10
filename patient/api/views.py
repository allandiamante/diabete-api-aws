from rest_framework import viewsets
from rest_framework.response import Response
from patient.models import Patient
from .serializer import PatientsSerializer, PrototipePatientsSerializer


class PatientsViewSet(viewsets.ModelViewSet):
    serializer_class = PatientsSerializer

    def get_queryset(self):
        patients = Patient.objects.all()
        return patients

    def create(self, request, *args, **kwargs):
        data = request.data

        new_patient = Patient.objects.create(
            subject_name=data["subject_name"], age=data['age'], initials=data["initials"], gender=data["gender"], weight=data["weight"], height=data["height"], phone=data["phone"], state=data["state"], city=data["city"], bmi=data["bmi"], bsa=data["bsa"], smoker=data["smoker"], alcohol=data["alcohol"], atividade_fisica=data["atividade_fisica"], dm=data["dm"], type_dm=data["type_dm"], age_dm_diagnosis=data["age_dm_diagnosis"], dm_duration=data["dm_duration"], hipo_mes=data["hipo_mes"], internacao_dm=data["internacao_dm"], sbp_repous=data["sbp_repous"], dbp_repous=data["dbp_repous"], sbp_empe=data["sbp_empe"], dbp_empe=data["dbp_empe"], sbp_change=data["sbp_change"], dbp_change=data["dbp_change"], postural_drop=data["postural_drop"], mean_hr=data["mean_hr"], rr_resting=data["rr_resting"], rr_db=data["rr_db"], rr_valsalva=data["rr_valsalva"], rr_standing=data["rr_standing"], obrienc_cs=data["obrienc_cs"], can_status=data["can_status"], brs_status=data["brs_status"], collected_data=data["collected_data"], observations=data["observations"])

        new_patient.save()
     

        serializer = PatientsSerializer(new_patient)

        return Response(serializer.data)

class PrototipePatientsViewSet(viewsets.ModelViewSet):
    serializer_class = PrototipePatientsSerializer

    def get_queryset(self):
        patients = Patient.objects.all()
        return patients

    def create(self, request, *args, **kwargs):
        data = request.data

        new_patient = Patient.objects.create(
            subject_name=data["subject_name"], age=data['age'], initials=data["initials"], gender= 1, weight= 300, height= 300, phone='99999-9999', state='PR', city='Prototipe-city', bmi= 100, bsa= 10, smoker=True, alcohol=True, atividade_fisica= 10, dm= True, type_dm= 2, age_dm_diagnosis= 100, dm_duration= 100, hipo_mes= 100, internacao_dm=True, sbp_repous=1000, dbp_repous= 1000, sbp_empe=1000, dbp_empe= 1000, sbp_change= 10, dbp_change= 10, postural_drop= True, mean_hr= 100, rr_resting=10, rr_db= 10, rr_valsalva= 10, rr_standing= 10, obrienc_cs= 10, can_status = 0,brs_status='prototipe', collected_data='prototipe', observations ='prototipe')

        new_patient.save()
     

        serializer = PrototipePatientsSerializer(new_patient)

        return Response(serializer.data)