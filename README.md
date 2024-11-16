# goit-pythonweb-hw-06

Database creation and management example with SQLAlchemy and Postgres.

## Setup

Run the following commands to set up the project environment:

```bash
docker-compose up -d
```

## Usage

### Generate fixtures

Run the following command to generate fixtures:

```bash
python main.py --migrate 
python main.py --fixtures
```

### Run predefined queries

Run the following command to run predefined queries:

```bash
python main.py --queries
```

### Run custom queries

Added ability to run CRUD operations on the database.

Running parameters:

```sh
usage: main.py [-h] [-a {create,list,update,remove}] [-m {Teacher,Student,Subject,Group,Mark}] [--id ID] [--group-id GROUP_ID]
               [--student-id STUDENT_ID] [--subject-id SUBJECT_ID] [--teacher-id TEACHER_ID] [-n NAME] [--mark MARK]
               [--fixtures] [--migrate] [--queries] [--setup]

CRUD operations for models.

options:
  -h, --help            show this help message and exit
  -a {create,list,update,remove}, --action {create,list,update,remove}
                        Specify the CRUD action to perform (create, list, update, remove).
  -m {Teacher,Student,Subject,Group,Mark}, --model {Teacher,Student,Subject,Group,Mark}
                        Specify the model to perform the action on.
  --id ID               Specify the ID of the record.
  --group-id GROUP_ID   Specify the group ID.
  --student-id STUDENT_ID
                        Specify the student ID.
  --subject-id SUBJECT_ID
                        Specify the subject ID.
  --teacher-id TEACHER_ID
                        Specify the teacher ID.
  -n NAME, --name NAME  Specify the name for create or update operations.
  --mark MARK           Specify the mark.
  --fixtures            Generate fixtures
  --migrate             Do not run migrations
  --queries             Run predefined queries
  --setup               Run migration and seed database
```

Examples:

```bash
python main.py -a create -m User -name "John Doe"
python main.py -a read -m Teacher
python main.py -a update -m User -id 1 -name "Jane Doe"
python main.py -a delete -m User -id 1
```
