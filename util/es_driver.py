from string import Template
from fin_data_crawler.config import es_base_url, index, type
import requests
import json


class ESdriver(object):
    def __init__(self, _es_base_url=es_base_url, _index=index, _type=type):
        self.url = Template("${es_base_url}/${index}/${type}")
        self.url = self.url.substitute(es_base_url=_es_base_url, index=_index, type=_type)

    def post_to_es(self, _data):
        r = requests.post(self.url, data=json.dumps(_data, ensure_ascii=False))
        response = r.text
        return response
