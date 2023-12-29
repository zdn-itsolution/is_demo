import pandas as pd


def format_data(catalog_data, users_data):
    catalog_fields = ['ID', 'NAME', 'DATE_CREATE', 'CREATED_BY', 'PRICE', 'CURRENCY_ID']
    user_fields = ['ID', 'LAST_NAME', 'NAME', 'SECOND_NAME']

    users_data = {user['ID']: ' '.join(user.get(field, '') for field in user_fields) for user in users_data}
    catalog_data = {product['ID']: product for product in catalog_data}

    data = {field: [] for field in catalog_fields}
    for field in catalog_fields:
        for product_data in catalog_data.values():
            if field != 'CREATED_BY':
                data[field].append(product_data[field])
            else:
                data[field].append(users_data[product_data[field]])

    return data


def save_as_excel(data, filepath):
    df = pd.DataFrame(data)
    df.to_excel(filepath)


if __name__ == '__main__':
    TEST_CATALOG_DATA = [
                          {
                            "ID": "373",
                            "NAME": "тест",
                            "CODE": "test",
                            "ACTIVE": "Y",
                            "SORT": "500",
                            "XML_ID": "373",
                            "TIMESTAMP_X": "2023-12-25T16:33:43+03:00",
                            "DATE_CREATE": "2023-12-15T12:49:06+03:00",
                            "MODIFIED_BY": "1",
                            "CREATED_BY": "1",
                            "CATALOG_ID": "25",
                            "DESCRIPTION": "",
                            "DESCRIPTION_TYPE": "html",
                            "PRICE": "123.00",
                            "CURRENCY_ID": "RUB",
                            "VAT_INCLUDED": "N",
                            "MEASURE": "9"
                          },
                          {
                            "ID": "377",
                            "NAME": "тест123",
                            "CODE": "test123",
                            "ACTIVE": "Y",
                            "SORT": "500",
                            "XML_ID": "377",
                            "TIMESTAMP_X": "2023-12-25T16:33:58+03:00",
                            "DATE_CREATE": "2023-12-15T12:49:12+03:00",
                            "MODIFIED_BY": "1",
                            "CREATED_BY": "1",
                            "CATALOG_ID": "25",
                            "DESCRIPTION_TYPE": "text",
                            "PRICE": "9999.00",
                            "CURRENCY_ID": "RUB",
                            "VAT_INCLUDED": "N",
                            "MEASURE": "9"
                          },
                          {
                            "ID": "381",
                            "NAME": "тест 333",
                            "CODE": "test-333",
                            "ACTIVE": "Y",
                            "SORT": "500",
                            "XML_ID": "381",
                            "TIMESTAMP_X": "2023-12-25T16:35:09+03:00",
                            "DATE_CREATE": "2023-12-15T12:49:27+03:00",
                            "MODIFIED_BY": "1",
                            "CREATED_BY": "1",
                            "CATALOG_ID": "25",
                            "DESCRIPTION_TYPE": "text",
                            "PRICE": "444.00",
                            "CURRENCY_ID": "RUB",
                            "VAT_INCLUDED": "N",
                            "MEASURE": "9"
                          },
                          {
                            "ID": "523",
                            "NAME": "ааа",
                            "CODE": "aaa",
                            "ACTIVE": "Y",
                            "SORT": "500",
                            "XML_ID": "523",
                            "TIMESTAMP_X": "2023-12-25T16:34:29+03:00",
                            "DATE_CREATE": "2023-12-21T11:24:02+03:00",
                            "MODIFIED_BY": "1",
                            "CREATED_BY": "1",
                            "CATALOG_ID": "25",
                            "DESCRIPTION_TYPE": "text",
                            "PRICE": "222.00",
                            "CURRENCY_ID": "RUB",
                            "VAT_INCLUDED": "N",
                            "MEASURE": "9"
                          }
                        ]
    TEST_USERS_DATA = [
                          {
                            "ID": "1",
                            "XML_ID": "52791654",
                            "ACTIVE": True,
                            "NAME": "Дмитрий",
                            "LAST_NAME": "Жербин",
                            "SECOND_NAME": "Николаевич",
                            "EMAIL": "zdn@it-solution.ru",
                            "LAST_LOGIN": "2023-12-26T09:50:48+03:00",
                            "DATE_REGISTER": "2023-12-05T03:00:00+03:00",
                            "TIME_ZONE": "",
                            "IS_ONLINE": "Y",
                            "TIME_ZONE_OFFSET": "0",
                            "TIMESTAMP_X": {},
                            "LAST_ACTIVITY_DATE": {},
                            "PERSONAL_GENDER": "M",
                            "PERSONAL_WWW": "",
                            "PERSONAL_BIRTHDAY": "2000-08-05T03:00:00+04:00",
                            "PERSONAL_PHOTO": "https://cdn-ru.bitrix24.ru/b27834032/main/2c5/2c5e1c0e362d576f05277c857d441667/photo_2023-12-06_14-11-13.jpg.png",
                            "PERSONAL_MOBILE": "+79215652518",
                            "PERSONAL_CITY": "",
                            "WORK_PHONE": "",
                            "WORK_POSITION": "Стажер",
                            "UF_EMPLOYMENT_DATE": "",
                            "UF_DEPARTMENT": [
                              1,
                              9,
                              3,
                              17
                            ],
                            "USER_TYPE": "employee"
                          },
                          {
                            "ID": "11",
                            "XML_ID": "44712600",
                            "ACTIVE": True,
                            "NAME": "Елена",
                            "LAST_NAME": "Шибанова",
                            "SECOND_NAME": "",
                            "EMAIL": "shes@it-solution.ru",
                            "LAST_LOGIN": "2023-12-22T14:59:00+03:00",
                            "DATE_REGISTER": "2023-12-06T03:00:00+03:00",
                            "TIME_ZONE": "",
                            "IS_ONLINE": "N",
                            "TIME_ZONE_OFFSET": "0",
                            "TIMESTAMP_X": {},
                            "LAST_ACTIVITY_DATE": {},
                            "PERSONAL_GENDER": "",
                            "PERSONAL_WWW": "",
                            "PERSONAL_BIRTHDAY": "",
                            "PERSONAL_MOBILE": "",
                            "PERSONAL_CITY": "",
                            "WORK_PHONE": "",
                            "WORK_POSITION": "",
                            "UF_EMPLOYMENT_DATE": "",
                            "UF_DEPARTMENT": [
                              9
                            ],
                            "UF_XING": "@shes_its",
                            "USER_TYPE": "employee"
                          },
                          {
                            "ID": "13",
                            "XML_ID": "52792044",
                            "ACTIVE": True,
                            "NAME": "Дмитрий2",
                            "LAST_NAME": "Жербин",
                            "SECOND_NAME": "",
                            "EMAIL": "zherbin.dima@yandex.ru",
                            "LAST_LOGIN": "2023-12-13T16:38:40+03:00",
                            "DATE_REGISTER": "2023-12-06T03:00:00+03:00",
                            "TIME_ZONE": "",
                            "IS_ONLINE": "N",
                            "TIME_ZONE_OFFSET": "0",
                            "TIMESTAMP_X": {},
                            "LAST_ACTIVITY_DATE": {},
                            "PERSONAL_GENDER": "",
                            "PERSONAL_WWW": "",
                            "PERSONAL_BIRTHDAY": "",
                            "PERSONAL_MOBILE": "",
                            "PERSONAL_CITY": "",
                            "WORK_PHONE": "",
                            "WORK_POSITION": "",
                            "UF_EMPLOYMENT_DATE": "",
                            "UF_DEPARTMENT": [
                              9,
                              5,
                              15,
                              17
                            ],
                            "USER_TYPE": "employee"
                          },
                          {
                            "ID": "15",
                            "XML_ID": "52794842",
                            "ACTIVE": True,
                            "NAME": "Дмитрий3",
                            "LAST_NAME": "Жербин",
                            "EMAIL": "dmitrii.zherbin@gmail.com",
                            "LAST_LOGIN": "2023-12-07T14:27:37+03:00",
                            "DATE_REGISTER": "2023-12-06T03:00:00+03:00",
                            "IS_ONLINE": "N",
                            "TIME_ZONE_OFFSET": "0",
                            "TIMESTAMP_X": {},
                            "LAST_ACTIVITY_DATE": {},
                            "PERSONAL_GENDER": "",
                            "PERSONAL_BIRTHDAY": "",
                            "UF_EMPLOYMENT_DATE": "",
                            "UF_DEPARTMENT": [
                              3,
                              17
                            ],
                            "USER_TYPE": "employee"
                          }
                        ]

    data = format_data(TEST_CATALOG_DATA, TEST_USERS_DATA)
    save_as_excel(data, 'example.xlsx')