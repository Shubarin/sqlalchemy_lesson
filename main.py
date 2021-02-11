from flask import Flask, render_template, request
from flask_login import LoginManager, login_user, login_required, logout_user, \
    current_user
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

from data import db_session
from data.category import Category
from data.departaments import Departament

from data.users import User
from data.jobs import Jobs
from forms.departament import AddDepartamentForm
from forms.user import LoginForm, RegisterForm
from forms.job import AddJobForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            email=form.email.data,
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/add-job', methods=['GET', 'POST'])
def add_job():
    form = AddJobForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Jobs(
            team_leader=form.team_leader.data,
            job=form.job.data,
            work_size=form.work_size.data,
            collaborators=form.collaborators.data,
            is_finished=form.is_finished.data
        )
        db_sess.add(job)
        db_sess.commit()
        return redirect('/')
    return render_template('job_add.html', title='Добавить работу', form=form)


@app.route('/jobs/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_job(id):
    form = AddJobForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                          (Jobs.user == current_user) | (
                                                      current_user.id == 1)
                                          ).first()
        if jobs:
            form.team_leader.data = jobs.team_leader
            form.job.data = jobs.job
            form.work_size.data = jobs.work_size
            form.collaborators.data = jobs.collaborators
            form.is_finished.data = jobs.is_finished
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                          (Jobs.user == current_user) | (
                                                      current_user.id == 1)
                                          ).first()
        if jobs:
            jobs.team_leader = form.team_leader.data
            jobs.job = form.job.data
            jobs.work_size = form.work_size.data
            jobs.collaborators = form.collaborators.data
            jobs.is_finished = form.is_finished.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('job_add.html',
                           title='Редактирование новости',
                           form=form
                           )


@app.route('/jobs_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def jobs_delete(id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                      (Jobs.user == current_user) | (
                                                  current_user.id == 1)
                                      ).first()
    if jobs:
        db_sess.delete(jobs)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/')
def jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    context = {'jobs': jobs}
    return render_template('jobs.html', **context)


@app.route('/departaments')
def departaments():
    db_sess = db_session.create_session()
    departaments = db_sess.query(Departament).all()
    context = {'departaments': departaments}
    return render_template('departaments.html', **context)


@app.route('/add-departament', methods=['GET', 'POST'])
@login_required
def add_departament():
    form = AddDepartamentForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        departament = Departament(
            title=form.title.data,
            chief=form.chief.data,
            members=form.members.data,
            email=form.email.data,
        )
        db_sess.add(departament)
        db_sess.commit()
        return redirect('/')
    return render_template('departament_add.html', title='Добавить департамент', form=form)


@app.route('/departaments/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_departament(id):
    form = AddDepartamentForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        departaments = db_sess.query(Departament).filter(Departament.id == id,
                                          (Departament.user == current_user) | (
                                                  current_user.id == 1)
                                          ).first()
        if departaments:
            form.title.data = departaments.title
            form.chief.data = departaments.chief
            form.members.data = departaments.members
            form.email.data = departaments.email
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        departaments = db_sess.query(Departament).filter(Departament.id == id,
                                          (Departament.user == current_user) | (
                                                  current_user.id == 1)
                                          ).first()
        if departaments:
            departaments.title = form.title.data
            departaments.chief = form.chief.data
            departaments.members = form.members.data
            departaments.email = form.email.data
            db_sess.commit()
            return redirect('/departaments')
        else:
            abort(404)
    return render_template('departament_add.html',
                           title='Редактирование департамента',
                           form=form
                           )


@app.route('/departaments_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def departaments_delete(id):
    db_sess = db_session.create_session()
    departaments = db_sess.query(Departament).filter(Departament.id == id,
                                      (Departament.user == current_user) | (
                                              current_user.id == 1)
                                      ).first()
    if departaments:
        db_sess.delete(departaments)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/departaments')


def main():
    db_session.global_init("db/mars.db")
    app.run(host='localhost', port=8080)


if __name__ == '__main__':
    main()
