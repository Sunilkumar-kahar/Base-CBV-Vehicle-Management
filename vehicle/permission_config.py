from .models import Vehicle

PERMISSION_CONFIG = {
    'user' : {
        Vehicle : ['view']
    },
    'admin' : {
        Vehicle : ['view', 'change']
    }
}