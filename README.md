# odoo workshop
Strativ Odoo Workshop

## Setup steps
- Download odoo 16 codebase from [Odoo repo](https://github.com/odoo/odoo/tree/16.0)
- Create a directory name `odoo-workshop`
- Go to `odoo-workshop`
- Create a virtualenv
  ```
  pyenv virtualenv 3.10 odoo-workshop-env-16
  pyenv activate odoo-workshop-env-16
  ```
- Install dependencies
  ```
  pip install -r requirements.txt
  ```
- Install postgres and run postgres. [Reference: Postgres docker](https://www.docker.com/blog/how-to-use-the-postgres-docker-official-image/)
  ```
  docker run --name=odoo-workshop-postgres -e POSTGRES_PASSWORD=secret -p 5433:5432 -d postgres
  docker exec --it <container-id> psql -U postgres
  psql -h localhost -p 5433 -U postgres -d postgres
  ```
- Create postgres role
  ```
  CREATE USER workshop WITH PASSWORD 'secret';
  CREATE ROLE admin WITH CREATEDB CREATEROLE LOGIN PASSWORD 'secret_admin';
  ```
- Up and running
  ```
  ./odoo-bin --db_host localhost --db_port 5433 -w secret_admin -r admin
  ```
