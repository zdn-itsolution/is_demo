def upload_crm_entities(but, data: list[dict], type_name: str):
    """Загружает данные на портал Битрикса."""
    types = {'лиды': 1,
             'сделки': 2,
             'контакты': 3,
             'компании': 4}
    type_id = types[type_name.lower()]
    methods = []
    # Группируем данные по 20 за раз, т.к. стоит ограничение.
    grouped_data = []
    for count, entity_data in enumerate(data):
        grouped_data.append(entity_data)
        if (count + 1) % 20 == 0 or count == (len(data) - 1):
            methods.append(('crm.item.batchImport',
                           {'entityTypeId': str(type_id), 'data': grouped_data}))
            grouped_data = []
    for method in methods:
        but.call_api_method(*method)
