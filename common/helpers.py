from django.contrib.auth import get_user_model

User = get_user_model()


def validated(data=[], except_these=[]):
    return {key: value for key, value in data.items() if key not in except_these}
