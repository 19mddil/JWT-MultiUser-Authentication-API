# Local Set Up
(I previously had this project in the <https://github.com/19mddil/Django_Framework/tree/master/api_projects/Medi_Project/jwt_authen_project/backend> repo ,but now the project worth having a repository for itself)  
**Run Following Commands in the Terminal**  
```bash
git clone https://github.com/19mddil/JWT-MultiUser-Authentication-API.git
```
Then move to the directory where you can see manage.py and run following
``bash
python3 -m venv venv
source venv/bin/activate
pip3 install pipenv
pipenv install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
## About
I was creating a medical system project where at a point I had to create two users who are doctor and paitent and I also intended  
to use jwt token authentication system. I was able to do it after some research and logical coding and the details can be found in my  
website.
## WorkFlow
### Register a Paitent

### Sign in the Paitent using Postman with JWT auth token
### Register a Doctor
### Sign in the Doctor using Postman with JWT auth token

