def app(env, start_response):
    str= '/?a=1&a=2&b=3'
    str= str.replace('/', '')
    str= str.replace('?', '')
    str=str.replace('&', '\n')
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return  str;

#for s in str.split('&'):
