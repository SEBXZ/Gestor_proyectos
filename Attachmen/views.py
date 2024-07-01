from rest_framework import viewsets
from .models import Attachment
from .serializers import AttachmentSerializer
from rest_framework.permissions import IsAuthenticated 
# Create your views here.
class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [IsAuthenticated]