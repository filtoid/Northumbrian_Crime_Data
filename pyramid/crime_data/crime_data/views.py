""" Cornice services.
"""
from cornice import Service
import csv

hello = Service(name='hello', path='/', description="Simplest app")
csv_file = Service(name='csv', path='/csv',
                   description="Get CSV of Data",
                   cors_origins=('*',))

@hello.get()
def get_info(request):
    """Returns Hello in JSON."""
    return {'Hello': 'World'}

@csv_file.get(renderer='json')
def get_csv_file(request):
    with open('data/2014-06-northumbria-street.csv', newline='') as csvfile:
        op = csv.reader(csvfile, delimiter=',')
        out = []
        heads = []

        offset = 25
        if 'off' in request.GET:
            offset=int(request.GET['off'])

        MAX_COUNT = 25
        if 'lim' in request.GET:
            MAX_COUNT = int(request.GET['lim'])

        count = 0
        for row in op:
            if offset > 0:
                offset -=1
                continue

            if count > MAX_COUNT:
                return {'heads': heads, 'values': out }

            if heads == []:
                heads.append(row)
            else:
                out.append(row)

            count += 1

        return {'heads': heads, 'values': out }


