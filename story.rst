Dashboard

List of projects, their Trafic analytics, Usage analytics, and Notifications


List of Apps/Manage Apps
Create App:
	Adds an App to a project, an app does one perticular task, an
	app may encapsulate one perticular funcationality,
	Navigate to Apps Management/Models list page by clicking on more button.

Create Models:
	An model represents a data table in database, it stores an perticular set of data, an object.
	Ex: Database of Polls





Create Source code of apps
Write Models for apps
Run MakeMigration
Run Migrate





V 1.1.0

Sequence Of Operation:

	Add Project model by from:
		- Generate a webfaction instance for Django project
		- Setup webfaction Database
		* Generate Django Project source code
		- Run Django Migrations
		- Generate Django superuser

	Add An App model by from:
		* Generate django app source code

	Add ModelObject model by form:

	Add ModelField model by from:
		* Write Django Models
		* Restart the instance
		* Run Django makemigration
		* Run Django migrate
		* Makes API call to project instance to add admin permission(This step is followed for every first field added to Model)


V 1.2.0


Adding custom API and Serializer

	Add Data serializer to data model/models by form
		* Write a serializer codes
	Add QuerySet to you data model by form
	Add Endpoint to by form
		* Write a url
		* Write a view

Improvements
	
	Auto generate created_at and updated_at modelfield for every modelobject model
	Add choices to char and int modelfield




