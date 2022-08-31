from utils.requests_helper import BaseSession


# def base_url():
#     base_url = 'https://reqres.in/api'
#     return BaseSession(base_url=base_url)

def base_url() -> BaseSession:
    root_url = 'https://reqres.in/api'
    return BaseSession(base_url=root_url)
