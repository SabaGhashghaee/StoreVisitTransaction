from elasticsearch import Elasticsearch
from flask import jsonify, request

from Service.General import Service

es = Elasticsearch()


class ElasticSearchAPI(Service):

    def initial_services(self, app):
        @app.route("/searchName", methods=['POST'])
        def search():
            self.request_validation()

            if request.is_json:
                data = request.get_json()
                keyword = data['keyword']

                body = {
                    "query": {
                        "multi_match": {
                            "query": keyword,
                            "fields": ["content", "title"]
                        }
                    },
                    "fields":
                        ["title", "index"]

                }

                res = es.search(index="onlinestore", body=body)
                result = [
                    {
                        "Title": doc['fields']['title'],
                        "ID": doc['fields']['index']
                     }for doc in res['hits']['hits']]

                return {"count": len(result), "hits": result}

