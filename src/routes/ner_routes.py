from flask import Blueprint
from flask_restful import Api

from resources.ner_annotation import NER_resources

NER_BLUEPRINT = Blueprint("ner_annotaion_api", __name__)
api = Api(NER_BLUEPRINT)
api.add_resource(NER_resources, "/ner")
