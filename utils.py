import re

from tinydb import Query

from db import forms

re_date_1 = re.compile(r"(0?[1-9]|[12][0-9]|3[01]).(0?[1-9]|1[012]).((19|20)\d\d)")  # DD.MM.YYYY
re_date_2 = re.compile(r"[0-9]{4}-(0[1-9]|1[012])-(0[1-9]|1[0-9]|2[0-9]|3[01])")  # YYYY-MM-DD
re_phone = re.compile(r"^((\+7|7)+([0-9]){10})$")
re_email = re.compile(r'^[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$')


def validate_type(data: dict) -> str | dict[str, str]:
    return_data = {}
    for key, value in data.items():

        if re_date_1.match(value) or re_date_2.match(value):
            value = "date"
            return_data[key] = value

        elif re_phone.match(value.strip()):
            value = "phone"
            return_data[key] = value

        elif re_email.match(value):
            value = "email"
            return_data[key] = value

        else:
            value = "text"
            return_data[key] = value

    if not return_data:
        return {'error': 'Enter data'}

    if results := forms.search(Query().fragment(return_data)):
        return f"Name form: {results[0].get('name')}"

    return return_data
