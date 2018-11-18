import os

from django.core import serializers


def deserialize():
    with open("../../resources/output.json") as fp:
        objects = serializers.json.Deserializer()
        for obj in objects:
            obj.save()


if __name__ == "__main__":
    deserialize()