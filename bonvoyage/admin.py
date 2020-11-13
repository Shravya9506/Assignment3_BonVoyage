from django.contrib import admin
from .models import Message
from django.http import HttpResponse, HttpResponseRedirect
import csv

class MessageExportCsvMixin:
    def export_as_csv(self, request, queryset):
        # Specify the header field names
        field_names = ['Sender name', 'Email', 'Phone', 'City', 'Message']
        response = HttpResponse(content_type='text/csv')
        # Specify the filename
        response['Content-Disposition'] = 'attachment; filename=Messages_report.csv'
        writer = csv.writer(response)
        writer.writerow(field_names)
        for message in queryset:
            writer.writerow([message.sender_name, message.email, str(message.phone), message.message])

        return response

    export_as_csv.short_description = "Export Selected as CSV"

class MessagesAdmin(admin.ModelAdmin, MessageExportCsvMixin):
    list_display = ('sender_name', 'email', 'phone', 'message')
    actions = ["export_as_csv"]

admin.site.register(Message, MessagesAdmin)