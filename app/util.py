import csv

from flask import json


CONTENT_TYPE = {'Content-Type': 'application/json; charset=utf-8'}


def csv_reader(filename):
    data = []
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data += row
    return data


def response_error(error, status):
    return (
        json.dumps(
            {
                'message': error[0],
                'errorCode': error[1]
            }
        ),
        status,
        CONTENT_TYPE
    )


def response_success(result, status):
    return (
        json.dumps(
            {
                'meta': {
                    'version': 'v1.0.0'
                },
                'records': result
            }
        ),
        status,
        CONTENT_TYPE
    )
