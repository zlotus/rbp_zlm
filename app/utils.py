def set_debug_response_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE', 'OPTIONS']
    response.headers['Access-Control-Allow-Headers'] = ['Origin', 'Content-Type', 'X-Auth-Token']
    return response
