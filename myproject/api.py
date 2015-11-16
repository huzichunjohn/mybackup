#!/usr/bin/python

import json

from flask import flask
app = Flask(__name__)

@app.route('/students', mothods=['GET'])
def get_students():
	students = Students.query.all()

	formatted_students = []
	for s in students:
		formatted_students.append({
			'id': s.id,
			'first_name': s.first_name,
			'last_name': s.last_name,
		})
	return json.dumps({'students': formatted_students}), 200, {'Content-Type': 'appliction/json'}


@app.route('/students', mothods=['POST'])
def create_student():
	kwargs = {}
	for field in ('first_name', 'last_name', '...'):
		kwargs[field] = request.form.get(field)

	student = Student(**kwargs)
	return json.dumps({
		'id': s.id,
		'first_name': s.first_name,
		'last_name': s.last_name,
		})


@app.route('/students/<id>', mothods=['PUT'])
def update_student(id):
	s = Student.query.get(id)
	if not s:
		abort(404)

	for field in ('first_name', 'last_name', '...'):
		setattr(s, field, request.form.get(field, getattr(s, field)))
	db.commit()

	return json.dumps({
		'id': s.id,
		'first_name': s.first_name,
		'last_name': s.last_name,
		})


