# api
Python-based &amp; JS/Probot based API protocols for GitHub/signal-k &amp; github/acord-robotics

<!--Add zsh config later-->

`flask1` -> referring to [signal-k/flask1](https://github.com/signal-k/flask1)

Jira projects:
* [DSP](https://signal-kinetics.atlassian.net/jira/software/projects/DSP/boards/5) - Data science (general), also python-based webapps, machine learning, python libraries, apis
* [RAPIA](https://signal-kinetics.atlassian.net/jira/software/projects/RAPIA) - REST Apis specifically for Arcadia - links in with a sprint for DSP
* [UPK](https://signal-kinetics.atlassian.net/jira/software/projects/UPK) - General unity stuff for first part of first game (soon will create a new project for Unity with sprints, proper use of labels and connections between projects, as well as folders for projects) 

Repository Map

# Django
## Django-Rest
### Example
Trying out the django-rest api to see how it differs and can offer anything that the Flask restful can't (as well as django vs flask in general, but since this is mainly for the game engine it's revolving around the APIs). 

<details><summary>Errors/Problems</summary>
```py
python manage.py makemigrations
Traceback (most recent call last):
  File "manage.py", line 22, in <module>
    main()
  File "manage.py", line 18, in main
    execute_from_command_line(sys.argv)
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/core/management/__init__.py", line 419, in execute_from_command_line
    utility.execute()
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/core/management/__init__.py", line 395, in execute
    django.setup()
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/__init__.py", line 24, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/apps/registry.py", line 91, in populate
    app_config = AppConfig.create(entry)
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/apps/config.py", line 212, in create
    mod = import_module(mod_path)
  File "/usr/lib/python3.8/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 961, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 973, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'library'

django/djangorest/example on 🌱 main [!?] via 👾 pyenv (examplenev) 
❯ python manage.py makemigrations
Traceback (most recent call last):
  File "manage.py", line 22, in <module>
    main()
  File "manage.py", line 18, in main
    execute_from_command_line(sys.argv)
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/core/management/__init__.py", line 419, in execute_from_command_line
    utility.execute()
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/core/management/__init__.py", line 413, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/core/management/base.py", line 354, in run_from_argv
    self.execute(*args, **cmd_options)
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/core/management/base.py", line 393, in execute
    self.check()
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/core/management/base.py", line 419, in check
    all_issues = checks.run_checks(
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/core/checks/registry.py", line 76, in run_checks
    new_errors = check(app_configs=app_configs, databases=databases)
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/core/checks/urls.py", line 13, in check_url_config
    return check_resolver(resolver)
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/core/checks/urls.py", line 23, in check_resolver
    return check_method()
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/urls/resolvers.py", line 412, in check
    for pattern in self.url_patterns:
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/utils/functional.py", line 48, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/urls/resolvers.py", line 598, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/utils/functional.py", line 48, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/urls/resolvers.py", line 591, in urlconf_module
    return import_module(self.urlconf_name)
  File "/usr/lib/python3.8/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 975, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 671, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 779, in exec_module
  File "<frozen importlib._bootstrap_external>", line 916, in get_code
  File "<frozen importlib._bootstrap_external>", line 846, in source_to_code
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/workspaces/api/django/djangorest/example/example/urls.py", line 21
    path('admin/', admin.site.urls),
    ^
SyntaxError: invalid syntax

django/djangorest/example on 🌱 main [✘?] via 👾 pyenv (examplenev) 
❯ python manage.py makemigrations
Traceback (most recent call last):
  File "manage.py", line 22, in <module>
    main()
  File "manage.py", line 18, in main
    execute_from_command_line(sys.argv)
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/core/management/__init__.py", line 419, in execute_from_command_line
    utility.execute()
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/core/management/__init__.py", line 413, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/core/management/base.py", line 354, in run_from_argv
    self.execute(*args, **cmd_options)
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/core/management/base.py", line 393, in execute
    self.check()
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/core/management/base.py", line 419, in check
    all_issues = checks.run_checks(
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/core/checks/registry.py", line 76, in run_checks
    new_errors = check(app_configs=app_configs, databases=databases)
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/core/checks/urls.py", line 13, in check_url_config
    return check_resolver(resolver)
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/core/checks/urls.py", line 23, in check_resolver
    return check_method()
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/urls/resolvers.py", line 412, in check
    for pattern in self.url_patterns:
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/utils/functional.py", line 48, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/urls/resolvers.py", line 598, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/utils/functional.py", line 48, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/urls/resolvers.py", line 591, in urlconf_module
    return import_module(self.urlconf_name)
  File "/usr/lib/python3.8/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 975, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 671, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 783, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/workspaces/api/django/djangorest/example/example/urls.py", line 20, in <module>
    path("", include("library.urls"), name="library"),
  File "/workspaces/api/django/djangorest/examplenev/lib/python3.8/site-packages/django/urls/conf.py", line 34, in include
    urlconf_module = import_module(urlconf_module)
  File "/usr/lib/python3.8/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 975, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 671, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 783, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/workspaces/api/django/djangorest/example/library/urls.py", line 3, in <module>
    from . import views
  File "/workspaces/api/django/djangorest/example/library/views.py", line 4, in <module>
    from .serializers import BookSerializer
  File "/workspaces/api/django/djangorest/example/library/serializers.py", line 4, in <module>
    class BookSerializer(serializer.ModelSerializer):
NameError: name 'serializer' is not defined
```
</details>


[`django/django-rest/example`](https://github.com/signal-k/api/tree/main/django/django-rest/example)

# Flask1
Submodule for [`Github/Signal-k/flask1](https://github.com/signal-k/flask1)

# Heroku
## Example
Attempting (and so far failing) to get Heroku to deploy a simple Flask application

# Flaskrest
Includes PyGithub, and a simple Flask API

See more documentation at [the docs](http://ar.skinetics.tech/stellarios/compass)

Read our log at [`cli`.skinetics.tech](http://cli.skinetics.tech/dc429c856c2d4552bf535a2a763eb44e)

Files:
<details><summary>`flaskapi.py`</summary>
* Contains the parameters and code for a flask-based restful api (in the form of a video sharing database)


```py
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	views = db.Column(db.Integer, nullable=False)
	likes = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f"Video(name = {name}, views = {views}, likes = {likes})"

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video is required")
video_update_args.add_argument("views", type=int, help="Views of the video")
video_update_args.add_argument("likes", type=int, help="Likes on the video")

resource_fields = {
	'id': fields.Integer,
	'name': fields.String,
	'views': fields.Integer,
	'likes': fields.Integer
}

class Video(Resource):
	@marshal_with(resource_fields)
	def get(self, video_id):
		result = VideoModel.query.filter_by(id=video_id).first()
		if not result:
			abort(404, message="Could not find video with that id")
		return result

	@marshal_with(resource_fields)
	def put(self, video_id):
		args = video_put_args.parse_args()
		result = VideoModel.query.filter_by(id=video_id).first()
		if result:
			abort(409, message="Video id taken...")

		video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
		db.session.add(video)
		db.session.commit()
		return video, 201

	@marshal_with(resource_fields)
	def patch(self, video_id):
		args = video_update_args.parse_args()
		result = VideoModel.query.filter_by(id=video_id).first()
		if not result:
			abort(404, message="Video doesn't exist, cannot update")

		if args['name']:
			result.name = args['name']
		if args['views']:
			result.views = args['views']
		if args['likes']:
			result.likes = args['likes']

		db.session.commit()

		return result


	def delete(self, video_id):
		abort_if_video_id_doesnt_exist(video_id)
		del videos[video_id]
		return '', 204


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
	app.run(debug=True)
```

[D](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)[ocumentation](https://www.youtube.com/watch?v=GMppyAPbLYk)
[Jira project - DSP-22, DSP-26](https://signal-kinetics.atlassian.net/browse/DSP-26)

Rest of the file structure: https://github.com/Signal-K/flask1/tree/Simples/Flask/app

</details>




`flaskrest/`