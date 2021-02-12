from flask import Blueprint, jsonify, request

from data import db_session
from data.users import User

blueprint = Blueprint(
    'users_api', __name__,
    template_folder='templates'
)


@blueprint.route('/api/users')
def get_users():
    session = db_session.create_session()
    users = session.query(User).all()
    return jsonify(
        {
            'users':
                [item.to_dict(only=('id', 'name', 'surname'))
                 for item in users]
        }
    )


@blueprint.route('/api/users/<int:users_id>', methods=['GET'])
def get_one_jobs(users_id):
    session = db_session.create_session()
    users = session.query(User).get(users_id)
    if not users:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'users': users.to_dict(only=('id', 'name', 'surname',
                                         'age', 'position', 'speciality',
                                         'address', 'email', 'city_from'))
        }
    )


@blueprint.route('/api/users', methods=['POST'])
def create_users():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'name', 'surname',
                  'age', 'position', 'speciality',
                  'address', 'email']):
        return jsonify({'error': 'Bad request'})
    session = db_session.create_session()
    user_in_db = session.query(User).filter(
        User.id == request.json['id']).first()
    if user_in_db:
        return jsonify({'error': 'Id already exists'})
    user = User(
        id=request.json['id'],
        name=request.json['name'],
        surname=request.json['surname'],
        age=request.json['age'],
        position=request.json['position'],
        speciality=request.json['speciality'],
        address=request.json['address'],
        email=request.json['email'],
    )
    session.add(user)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:users_id>', methods=['PUT', 'PATCH'])
def edit_users(users_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'name', 'surname',
                  'age', 'position', 'speciality',
                  'address', 'email']):
        return jsonify({'error': 'Bad request'})
    session = db_session.create_session()
    user_in_db = session.query(User).filter(User.id == users_id).first()
    if not user_in_db:
        return jsonify({'error': 'Not found'})
    user_in_db.id = request.json['id']
    user_in_db.name = request.json['name']
    user_in_db.surname = request.json['surname']
    user_in_db.age = request.json['age']
    user_in_db.position = request.json['position']
    user_in_db.speciality = request.json['speciality']
    user_in_db.address = request.json['address']
    user_in_db.email = request.json['email']
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:users_id>', methods=['DELETE'])
def delete_news(users_id):
    session = db_session.create_session()
    users = session.query(User).get(users_id)
    if not users:
        return jsonify({'error': 'Not found'})
    session.delete(users)
    session.commit()
    return jsonify({'success': 'OK'})
