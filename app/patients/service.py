# Mock names
names = ['rodrigo', 'rogerio', 'rodney']


def get_patients_by_name(q):
    return [{'name': x} for x in names]