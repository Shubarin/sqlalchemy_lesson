from requests import get, post, delete, put, patch

def test_jobs_api():
      print(get('http://localhost:5000/api/jobs').json())

      # print(get('http://localhost:5000/api/jobs/1').json())
      # print(get('http://localhost:5000/api/jobs/999').json())
      #
      # print(get('http://localhost:5000/api/jobs/q').json())
      #
      # запрос без параметров
      # print(post('http://localhost:5000/api/jobs').json())
      # запрос с неверным количеством параметрами
      # print(post('http://localhost:5000/api/jobs',
      #            json={'team_leader': 1}).json())
      # print(post('http://localhost:5000/api/jobs',
      #            json={'id': 5,
      #                  'team_leader': 1,
      #                  'job': 'Текст работы',
      #                  'work_size': 1,
      #                  'collaborators': '1, 2',
      #                  'is_finished': True}).json())
      # Запись с таким id уже существует
      print(put('http://localhost:5000/api/jobs/',
                json={'id': 2,
                      'team_leader': 1,
                      'job': 'Новый работы',
                      'work_size': 1,
                      'collaborators': '1, 2',
                      'is_finished': True}).json())
      print(put('http://localhost:5000/api/jobs/999',
                json={'id': 2,
                      'team_leader': 1,
                      'job': 'Новый работы',
                      'work_size': 1,
                      'collaborators': '1, 2',
                      'is_finished': True}).json())
      print(put('http://localhost:5000/api/jobs/2',
                 json={'id': 2,
                       'team_leader': 1,
                       'job': 'Новый работы',
                       'work_size': 1,
                       'collaborators': '1, 2',
                       'is_finished': True}).json())
      print(patch('http://localhost:5000/api/jobs/2',
                json={'id': 2,
                      'team_leader': 1,
                      'job': 'Новый',
                      'work_size': 1,
                      'collaborators': '1, 2',
                      'is_finished': True}).json())
      # print(delete('http://localhost:5000/api/jobs/999').json())
      # новости с id = 999 нет в базе

      # print(delete('http://localhost:5000/api/jobs/5').json())

      print(get('http://localhost:5000/api/jobs').json())


print(get('http://localhost:5000/api/users').json())


print(get('http://localhost:5000/api/users/1').json())
print(get('http://localhost:5000/api/users/999').json())

# запрос без параметров
print(post('http://localhost:5000/api/users').json())
# запрос с неверным количеством параметрами
print(post('http://localhost:5000/api/users',
           json={'id': 1}).json())
print(post('http://localhost:5000/api/users',
           json={'id': 2,
                 'name': 'Test',
                 'surname': 'Testing',
                 'age': 42,
                 'position': 'position',
                 'speciality': 'speciality',
                 'address': 'Воронеж',
                 'email': 'b@b.com'}).json())

print(put('http://localhost:5000/api/users/',
          json={'id': 2,
                'name': 'Test1',
                'surname': 'Testing',
                'age': 43,
                'position': 'position',
                'speciality': 'speciality',
                'address': 'Воронеж',
                'email': 'b@b.com'}).json())
print(put('http://localhost:5000/api/users/999',
          json={'id': 2,
                'name': 'Test1',
                'surname': 'Testing',
                'age': 43,
                'position': 'position',
                'speciality': 'speciality',
                'address': 'Воронеж',
                'email': 'b@b.com'}).json())
print(put('http://localhost:5000/api/users/2',
          json={'id': 2,
                'name': 'Test1',
                'surname': 'Testing',
                'age': 43,
                'position': 'position',
                'speciality': 'speciality',
                'address': 'Воронеж',
                'email': 'b@b.com'}).json())
print(patch('http://localhost:5000/api/users/2',
            json={'id': 2,
                  'name': 'Test12345',
                  'surname': 'Testing',
                  'age': 43,
                  'position': 'position',
                  'speciality': 'speciality',
                  'address': 'Воронеж',
                  'email': 'b@b.com'}).json())
print(delete('http://localhost:5000/api/users/999').json())
# новости с id = 999 нет в базе

print(delete('http://localhost:5000/api/users/1').json())

print(get('http://localhost:5000/api/users').json())
