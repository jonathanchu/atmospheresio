from django.http import HttpResponse

import json
import requests


def traffic(request):
    """A request to Gauges traffic API to retrieve the visitors and views
    for a given API key and Gauges ID.
    """
    api_key = '3dc6c88ceef523a8a46ad0a866468426'
    gauge_id = '4ff13d5ef5a1f535d0000003'

    # preparing the request URL
    url = 'https://secure.gaug.es/gauges/%s/traffic' % gauge_id
    headers = {'X-Gauges-Token': '%s' % api_key}

    # make the actual request
    gauges_data = requests.get(url, headers=headers)

    # setup some defaults for the json graph
    display_graph = {'title': 'Jontourage', 'type': 'line'}
    views = {'title': 'Views', 'datapoints': []}
    visitors = {'title': 'People', 'datapoints': []}

    display_graph = {
        'title': 'Jontourage Visitors',
        'color': 'blue',
        'type': 'line',
        'yAxis': {
            'minValue': 0,
        },
        'datasequences': [
            {
                'title': 'Visitors',
                'datapoints': [],
            },
        ]
    }

    # process json so we can parse it
    data = json.loads(gauges_data.content)

    # iterate over the data and pick out what we need to make into
    # a new dictionary
    for item in data['traffic']:
        # TODO format date before appending
        views['datapoints'].append({'title': item['date'],
                                    'value': item['views']})

    # setup the graphs
    display_graph['datasequences'] = views
    data = json.dumps(display_graph)

    return HttpResponse(data, 'application/json')
