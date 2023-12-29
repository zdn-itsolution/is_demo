import os
import urllib.request
from django.shortcuts import render
from django.contrib import messages
from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth
from .forms import GoogleTableForm
from .utils.upload_crm_entities import upload_crm_entities
from .utils.upload_calls import upload_calls
from .utils.excel_parser import format_excel_data


APP_NAME = 'Загрузка демо-данных из гугл-таблицы'


@main_auth(on_cookies=True)
def upload_form(request):

    but = request.bitrix_user_token
    if request.method == 'POST':
        form = GoogleTableForm(request.POST)
        try:
            if form.is_valid():
                # Получаем ссылку на таблицу.
                url = form.cleaned_data['url'].split('/edit')[0] + '/export?format=xlsx'
                # Сохраняем данные в excel файл.
                urllib.request.urlretrieve(url, filepath := 'table.xlsx')

                # Получаем список желаемых листов таблицы.
                sheets = form.cleaned_data['desired_sheets']
                sheets = [sheet.strip().title() for sheet in sheets.split(',')]

                for sheet_name in sheets:
                    data = format_excel_data(filepath, sheet_name)
                    if sheet_name.lower() != 'звонки':
                        upload_crm_entities(but, data, type_name=sheet_name)
                    else:
                        upload_calls(but, data)

                os.remove(filepath)
                messages.success(request, 'Данные успешно импортированы!')

        except Exception as e:
            print(e)
            messages.error(request, 'Убедитесь, что поля заполнены верно')

    form = GoogleTableForm()
    context = {'app_name': APP_NAME, 'form': form}
    return render(request, 'upload_from_google/main.html', context)
