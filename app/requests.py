# import urllib.request,json
# from .models import Quotes

import requests,json
def get_quotes():
    response=requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    if response.status_code == 200:
        quote=response.json()
        return quote



# getting the quotes api
quotes_url=None

def configure_request(app):
    global quotes_url

    quotes_url=app.config['QUOTES_API']


# def get_quotes():
#     '''
#     Function that gets the json response to the url request
#     '''
#     get_quotes_url="http://quotes.stormconsultancy.co.uk/random.json"

#     with urllib.request.urlopen(get_quotes_url) as url:
#         get_quotes_data=url.read()
#         get_quotes_response=json.loads(get_quotes_data)
#         print(get_quotes_response)

#         quotes_results= None

#         get_quotes_response=[]

#         for quote_item in get_quotes_response:
#             id=quote_item.get('id')
#             print(id)
#             author=quote_item.get('author')
#             quote=quote_item.get('quote')
#             permalink=quote_item.get('permalink')

#         # quote_object=Quotes(id, author, quote, permalink)
#         # quotes_results.append(quote_object)


#         # if get_quotes_response:
#         #     quotes_results_list=get_quotes_response
#         #     quotes_results=process_results(quotes_results_list)

#     return quotes_results

# # def process_results(quotes_list):
# #     '''
# #     Function that processes the quotes result and transforms it to a list of objects

# #     Args:
# #     quotes_list: A list of dictionaries that contain quotes

# #     Returns:
# #     quotes_results: A list of quote objects
# #     '''
# #     quotes_results=[]
# #     for quote_item in quotes_list:
# #         id=quote_item.get('id')
# #         author=quote_item.get('author')
# #         quote=quote_item.get('quote')
# #         permalink=quote_item.get('permalink')

# #         quote_object=Quotes(id, author, quote, permalink)
# #         quotes_results.append(quote_object)

# #     return quotes_results


        
