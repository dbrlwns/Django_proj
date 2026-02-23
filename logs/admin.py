from django.contrib import admin
from django.http import HttpResponse

from logs.models import Log
from django.utils import timezone
from datetime import timedelta

import csv

# Register your models here.
# Admin 페이지 요청 시 ModelAdmin 클래스가 바로 호출되어 나타남.
@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ("created_at", "level", "logger_name", "message")
    list_filter = ("level", "logger_name") # 우측에 필터링 UI를 생성
    search_fields = ["message"]
    ordering = ("-created_at",)
    actions = ["export_as_csv"]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        since = timezone.now() - timedelta(days=30)
        return qs.filter(created_at__gte=since)

    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="logs.csv"'

        writer = csv.writer(response)
        writer.writerow(["Date", "Level", "Logger", "Message"])
        for log in queryset:
            writer.writerow([
                log.created_at, log.level,
                log.logger_name, log.message,
            ])
        return response

    export_as_csv.short_description = "선택한 로그를 CSV로 다운로드"