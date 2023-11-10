from gavr.settings import DEBUG

def app_mode(request):
    return {'app_mode': DEBUG}
