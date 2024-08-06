<h1 align="center">Spreche Deutsch API</h1>

<h2 align="center">Purpose of the Website/App:</h2>

<h3 align="center"><i>To serve as the API for my Spreche Deutsch application.</i></h3>

<h2 align="center">Technology used</h2>

<div align="center">
  <img align="center" src="/docs/readme/icons/python.svg" alt="HTML" height="50"/>
  <p align="center"><i>Python</i></p>
</div>

<div align="center">
  <img align="center" src="/docs/readme/icons/postgresql.svg" alt="HTML" height="50"/>
  <p align="center"><i>Postgresql</i></p>
</div>

<div align="center">
  <h3><i><a href="https://github.com/WillBorysiak/Spreche-Deutsch-UI">Spreche Deutsch UI</a></i></h3>
</div>

<h2 align="center">How The Application Works</h2>

- The application uses Python FastApi to create the app structure and API routes.
- The database used for the application is Postgresql and I use Sqlalchemy to handle this connection.
- Alembic was used for managing the database structure and migrations.
- Pydantic was used to map out the schemas that contain the data structures for my database.

<h2 align="center">What I Learnt</h2>

- Learnt how to create and deploy a Python application using the Poetry dependency manager.
- Organised the project for scalability with a clean project structure using sub routes, schemas and models.
- Configured the shared settings, database connections and environmental variables for a better dev experience.
- Managed error handling with each API request by returning HTTP expectations if data was missing.
- Ensured that CORS was implemented so that my API can only be accessed via certain domains in production.

<h2 align="center">What Was The Biggest Challenge</h2>

The biggest challenge I faced was setting up the API to work with a Postgresql database and mirror development once
running in production. I had to create a database engine that would use the correct drivers and connection information
using Sqlalchemy and env variables. I hosted the API on Heruko which required custom buildpacks for Poetry along with
various other settings, so the application ran correctly. I also had to ensure that DNS was respected on my domain
provider and that CORS would allow my UI to make requests from its own domain. I ended up hosting my API on a sub domain
of my UI making the experience slightly easier to manage.
