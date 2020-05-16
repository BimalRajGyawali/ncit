# NCIT - Nepal College of Information Technology
Unofficial College website with django. Live at https://bimalrajgyawali.pythonanywhere.com/

Documentation for this project is at https://bimalrajgyawali.github.io/ncit-docs/index.html

# Setting up the project in your local machine

- ```Fork``` and `clone` the repo into your local machine

- create a virtual environment : ``` virtualenv venv ```

- activate the virtual environment : ` source venv/bin/activate `

- install projects requirements : ` (venv) pip install -r requirements.txt `

- makemigrations : ` (venv) python manage.py makemigrations `

- migrate : ` (venv) python manage.py migrate `

- finally, run the server : ` (venv) python manage.py runserver `


# Creating the pull request 

- set the `upstream` to `https://github.com/BimalRajGyawali/ncit.git`

- ` create ` and `check out` to new `branch`

- `add` your features to the branch

- `push` the branch to origin 

-  issue a `pull request` to the `upstream`

- keep your repo sync with upstream : ` git pull upstream master `
