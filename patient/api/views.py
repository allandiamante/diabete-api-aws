from rest_framework import viewsets
from rest_framework.response import Response
from patient.models import Patient
from .serializer import PatientsSerializer


class PatientsViewSet(viewsets.ModelViewSet):
    serializer_class = PatientsSerializer

    def get_queryset(self):
        patient = Patients.objects.all()
        return patient

    def create(self, request, *args, **kwargs):
        data = request.data

        new_patient = Patients.objects.create(
            subject_name=data["subject_name"], age=data['age'], initials=data["initials"], gender=data["gender"], weight=data["weight"], height=data["height"], phone=data["phone"], state=data["state"], city=data["city"], bmi=data["bmi"], bsa=data["bsa"], smoker=data["smoker"], alcohol=data["alcohol"], atividade_fisica=data["atividade_fisica"], dm=data["dm"], type_dm=data["type_dm"], age_dm_diagnosis=data["age_dm_diagnosis"], dm_duration=data["dm_duration"], hipo_mes=data["hipo_mes"], internacao_dm=data["internacao_dm"], sbp_repous=data["sbp_repous"], dbp_repous=data["dbp_repous"], sbp_empe=data["sbp_empe"], dbp_empe=data["dbp_empe"], sbp_change=data["sbp_change"], dbp_change=data["dbp_change"], postural_drop=data["postural_drop"], mean_hr=data["mean_hr"], rr_resting=data["rr_resting"], rr_db=data["rr_db"], rr_valsalva=data["rr_valsalva"], rr_standing=data["rr_standing"], obrienc_cs=data["obrienc_cs"], can_status=data["can_status"], brs_status=data["brs_status"], collected_data=data["collected_data"], observations=data["observations"])

        new_patient.save()
     

        serializer = PatientsSerializer(new_patient)

        return Response(serializer.data)

