import json

from django.conf import settings


def json_deserialize(file: str):
    with open(f"{settings.BASE_DIR}/stocks/tests/fixtures/{file}") as f:
        json_response = json.load(f)

    return json_response
