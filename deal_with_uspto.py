import requests

def search_patents(search_string):

    # Build the request string
    request_string = 'https://developer.uspto.gov/ibd-api/v1/patent/application'
    request_string += '?searchText='+search_string+'&start=100&rows=100'
    # print(request_string)
    res = requests.get(request_string)

    res_json = res.json()

    records_found = res_json['response']['numFound']
    print('records_found: ', records_found)

    start_idx = res_json['response']['start']
    print('start index: ', start_idx)

    return res_json['response']['docs']
