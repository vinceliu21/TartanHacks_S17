import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1
 
 
url = 'https://developer.ibm.com/watson/blog/2015/11/03/price-reduction-for-watson-personality-insights/'
# operations to perform
extract = ['page-image', 'entity', 'keyword', 'title', 'author', 'taxonomy', 'concept', 'doc-emotion']
 
alchemy_language = AlchemyLanguageV1(api_key='13664dcfce096de46a48a7173869a25bd140fc9e')
results = alchemy_language.combined(url=url, extract=extract)
 
# print the results
print(json.dumps(results, indent=2))