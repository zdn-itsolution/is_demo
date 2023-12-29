import os
from django.http import FileResponse
from django.shortcuts import render
from django.conf import settings
from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth
from .utils.save_catalog import format_data, save_as_excel


APP_NAME = 'Каталог товаров в excel-файле'


@main_auth(on_cookies=True)
def get_form(request):
    context = {'app_name': APP_NAME}
    return render(request, 'catalog_to_excel/main.html', context)


@main_auth(on_cookies=True)
def get_excel(request):
    but = request.bitrix_user_token
    file_name = 'example'

    products = but.call_list_method('crm.product.list')
    users = but.call_list_method('user.get')
    # "Склеиваем" данные товаров с данными пользователей.
    data = format_data(products, users)

    file_path = os.path.join(settings.BASE_DIR, f'media/{file_name}.xlsx')
    save_as_excel(data, file_path)

    with open(file_path, 'rb') as file:
        excel_data = file.read()

    response = FileResponse(excel_data)
    response['Content-Disposition'] = f'attachment; filename="{file_name}.xlsx"'

    return response
