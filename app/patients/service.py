from app import db


def get_patients_by_name(q):
    return [{'name': x} for x in db.get_dataset('patients').search(q)]