def set_debug_response_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE', 'OPTIONS']
    response.headers['Access-Control-Allow-Headers'] = ['Origin', 'Content-Type', 'X-Auth-Token']
    return response
