import os
import urllib.request

from django.conf import settings
from django.utils.timezone import make_aware
import requests
from callsuploader.models import CallInfo
from pathlib import Path
from django.core.files.base import ContentFile


def upload_calls(but, calls_data: dict):
    for call_data in calls_data:

        call = CallInfo(
            user_phone=call_data['user_phone'],
            user_id=int(call_data['user_id']),
            phone_number=call_data['phone_number'],
            call_date=make_aware(call_data['call_date']),
            type=int(call_data['type']),
            add_to_chat=int(call_data['add_to_chat'])
        )
        call.save()

        drive_id = call_data['file'].split('/')[-2]
        url = 'https://drive.google.com/uc?id=' + drive_id + '&export=download'
        response = requests.get(url, allow_redirects=True)

        call.file.save(f'{call.id}.mp3', ContentFile(response.content))
        call.save()

        call.telephony_externalcall_register(but)
        call.telephony_externalcall_finish(but)

