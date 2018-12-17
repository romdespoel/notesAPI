from database import session
from models import Note
from datetime import datetime
from flask_restful import Resource, reqparse, abort
from flask_restful import marshal_with, fields

note_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'body': fields.String,
    'date': fields.String,
    'archived': fields.Boolean
}

parser = reqparse.RequestParser()
parser.add_argument('title')
parser.add_argument('body')


class NoteResource(Resource):

    @marshal_with(note_fields)
    def get(self, id):
        note = session.query(Note).filter(Note.id == id).first()
        if not note:
            abort(404, message="Note %s doesn't exist" % id)
        return note, 200

    @marshal_with(note_fields)
    def delete(self, id):
        note = session.query(Note).filter(Note.id == id).first()
        if not note:
            abort(404, message="Note %s doesn't exist" % id)
        session.delete(note)
        session.commit()
        return note, 202

    @marshal_with(note_fields)
    def put(self, id):
        args = parser.parse_args()
        note = session.query(Note).filter(Note.id == id).first()
        note.title = args['title']
        note.body = args['body']
        date = datetime.now()
        note.date = date.strftime("%a, %d/%m/%Y")
        note.archived = False
        session.add(note)
        session.commit()
        return note, 201


class Notes(Resource):
    @marshal_with(note_fields)
    def get(self):
        notes = session.query(Note).filter(Note.archived == False).all()
        return notes, 200

    @marshal_with(note_fields)
    def post(self):
        parsed_args = parser.parse_args()
        note = Note(title=parsed_args['title'], body=parsed_args['body'],
                    date= datetime.now().strftime("%a, %d/%m/%Y"),
                    archived = False)
        session.add(note)
        session.commit()
        return note, 201


class Archives(Resource):
    @marshal_with(note_fields)
    def get(self):
        notes = session.query(Note).filter(Note.archived == True).all()
        return notes, 200

    @marshal_with(note_fields)
    def delete(self, id):
        note = session.query(Note).filter(Note.id == id).first()
        if not note:
            abort(404, message="Note %s doesn't exist" % id)
        note.archived = True
        session.add(note)
        session.commit()
        return note, 202