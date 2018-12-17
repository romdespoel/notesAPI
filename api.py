from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from models import Note
from resource_notes import Notes, NoteResource, Archives

app = Flask(__name__)
api = Api(app)

api.add_resource(Notes, '/notes/', endpoint='notes')
api.add_resource(Archives, '/archives/', endpoint='archives')
api.add_resource(Archives, '/archives/<string:id>', endpoint='archive')
api.add_resource(NoteResource, '/notes/<string:id>', endpoint='note')

app.run()