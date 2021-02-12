import flask
from flask import jsonify, request

from data import db_session
from data.jobs import Jobs

blueprint = flask.Blueprint('jobs_api', __name__,
                            template_folder='templates')


@blueprint.route('/api/jobs')
def get_jobs():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('team_leader', 'job', 'user.name'))
                 for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['GET'])
def get_one_jobs(jobs_id):
    session = db_session.create_session()
    jobs = session.query(Jobs).get(jobs_id)
    if not jobs:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'jobs': jobs.to_dict(only=('team_leader', 'job', 'work_size',
                                       'collaborators', 'category',
                                       'user.name'))
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'team_leader', 'job', 'work_size',
                  'collaborators', 'is_finished']):
        return jsonify({'error': 'Bad request'})
    session = db_session.create_session()
    job_in_db = session.query(Jobs).filter(Jobs.id == request.json['id']).first()
    if job_in_db:
        return jsonify({'error': 'Id already exists'})
    jobs = Jobs(
        id=request.json['id'],
        team_leader=request.json['team_leader'],
        job=request.json['job'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        is_finished=request.json['is_finished'],
    )
    session.add(jobs)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['PUT', 'PATCH'])
def edit_jobs(jobs_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'team_leader', 'job', 'work_size',
                  'collaborators', 'is_finished']):
        return jsonify({'error': 'Bad request'})
    session = db_session.create_session()
    job_in_db = session.query(Jobs).filter(Jobs.id == jobs_id).first()
    if not job_in_db:
        return jsonify({'error': 'Not found'})
    job_in_db.id=request.json['id']
    job_in_db.team_leader=request.json['team_leader']
    job_in_db.job=request.json['job']
    job_in_db.work_size=request.json['work_size']
    job_in_db.collaborators=request.json['collaborators']
    job_in_db.is_finished=request.json['is_finished']
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['DELETE'])
def delete_news(jobs_id):
    session = db_session.create_session()
    jobs = session.query(Jobs).get(jobs_id)
    if not jobs:
        return jsonify({'error': 'Not found'})
    session.delete(jobs)
    session.commit()
    return jsonify({'success': 'OK'})
