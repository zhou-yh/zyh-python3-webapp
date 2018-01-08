import json,logging,inspect,functools

class APIError(Exception):
    def __init__(self, error, data='',message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message=message

class APIValueError(APIError):
    def __init__(self, field,message=''):
        super(APIValueError,self).__init__('value:invalid', field,message)


class APIResourceError(APIError)
    def __init__(self,field,message=''):
        super(APIResourceError,self).__init__('value:notfound',field,message)


class APIPermissionError(APIError):

    '''
    indicate the api has no permission
    '''
    def __init__(self,message=''):
        super(APIPermissionError,self).__init__('permission:forbidden','permission',message)


        

                                                
