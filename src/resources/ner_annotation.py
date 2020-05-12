import os
from repositories.sc_judgment_header_ner_eval import SC_ner_annotation
import json
from flask_restful import reqparse, Resource
from flask.json import jsonify

# ner annotation
parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('sentences',action = 'append', required = True)

class NER_resources(Resource):
    
    def post(self):
        args    = parser.parse_args()
        print()
        if 'sentences' not in args or args['sentences'] is None or not isinstance(args['sentences'],list):
             return jsonify({
                'status': {
                    'code' : 400,
                    'message' : 'data missing'
                }
            })
        else:
            output_ner = list()
            for text in args['sentences']:
                mix_model_dir = '/opt/share/python/upload/models/exp_3_mix/'
                model_dir_order = '/opt/share/python/upload/models/exp_3_order/'
                model_dir_judgment = '/opt/share/python/upload/models/exp_3_judgment/'
                tagged_text_result = SC_ner_annotation(model_dir_judgment, model_dir_order, mix_model_dir, text).main()
                if tagged_text_result is None or mix_model_dir is None:
                    return jsonify({
                        'status': {
                            'code' : 400,
                            'message' : 'either tagged text result or model dir not found'
                        }
                    }) 
                else: 
                    output_ner.append(tagged_text_result)
            return jsonify({
                'status' : {
                    'code' : 200,
                    'message' : 'api successful'
                },
                'ner_result' : output_ner
            })
