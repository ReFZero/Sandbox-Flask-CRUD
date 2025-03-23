from flask import Blueprint, request, jsonify, render_template
from .models import Person
from . import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    persons = Person.query.all()
    return render_template("index.html", persons=persons)


@main.route('/persons', methods=['GET'])
def get_persons():
    persons = Person.query.all()
    return jsonify([person.to_dict() for person in persons])


@main.route('/persons/<int:id>', methods=['GET'])
def get_person(id):
    person = Person.query.get_or_404(id)
    return jsonify(person.to_dict())


@main.route('/persons', methods=['POST'])
def create_person():
    data = request.json
    new_person = Person(name=data['name'], surname=data.get('surname'))
    db.session.add(new_person)
    db.session.commit()
    return jsonify(new_person.to_dict()), 201


@main.route('/persons/<int:id>', methods=['PUT'])
def update_person(id):
    person = Person.query.get_or_404(id)
    data = request.json
    person.name = data.get('name', person.name)
    person.surname = data.get('surname', person.surname)
    db.session.commit()
    return jsonify(person.to_dict())


@main.route('/persons/<int:id>', methods=['DELETE'])
def delete_person(id):
    person = Person.query.get_or_404(id)
    db.session.delete(person)
    db.session.commit()
    return '', 204
