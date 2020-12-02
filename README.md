# Local Set Up
(I previously had this project in the <https://github.com/19mddil/Django_Framework/tree/master/api_projects/Medi_Project/jwt_authen_project/backend> repo, but now the project worth having a repository for itself.Also I implemented the same criteria using djangos rest-auth which can be found in this repo
<https://github.com/19mddil/Django_Framework/tree/master/api_projects/Medi_Project/rest_auth_project/backend> )  
**Run Following Commands in the Terminal**  
```bash
git clone https://github.com/19mddil/JWT-MultiUser-Authentication-API.git
```
Then move your cloned directory where you will see manage.py and run following
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install pipenv
pipenv install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
## About
I was creating a medical system project where at a point I had to create two users who are doctor and paitent and I also intended to use jwt token authentication system for both users authentication in same project. I was able to do it after some research and logical coding and how I did that the details can be found in my website where I tried to explain.
## User as Doctor or Paitent Authentication JWT(Signup and Login)
### Register a Paitent
<http://127.0.0.1:8000/api/signup/paitent/>
![paitent registration input](/assets/pr.png)
![registration success](/assets/prs.png)
### Sign in the Paitent using Postman
Open Postman and create new request
![postman create new request](/assets/postman_new.png)
Make sure you select POST and enter <http://127.0.0.1:8000/api/signin/>,  
then in the body part select raw and json format and enter data like following  
image  
![postman sign in for jwt token](/assets/postman_p_2.png)
### Retrieve Paitent JWT token
On success you will recieve a jwt token with which you will retrieve your paitent profile
![postman retrieve jwt token](/assets/postman_p_3.png)
### Use the token to retrieve Paitent Profile Using Postman
Copy the token, in postman select GET method and enter <http://127.0.0.1:8000/api/profile/>  
then select authorization and select Bearer Token and enter the copied token like  
following image  
![postman token input for paitent profile](/assets/postman_p_4.png)
on success you now retrieve your paitent profile  
![success response ](/assets/postman_p_5.png)
### Register a Doctor
<http://127.0.0.1:8000/api/signup/doctor/>
![doctor registration input](/assets/pd.png)
![registration success](/assets/pds.png)
### Sign in the Doctor using Postman
Make sure you select POST and enter <http://127.0.0.1:8000/api/signin/>,  
then in the body part select raw and json format and enter data like following  
image  
![postman sign in for jwt token](/assets/postman_d_2.png)
### Retrieve Doctor JWT token
On success you will recieve a jwt token with which you will retrieve your doctor profile
![postman retrieve jwt token](/assets/postman_d_3.png)
### Use the token to retrieve Doctor Profile Using Postman
Copy the token, in postman select GET method and enter <http://127.0.0.1:8000/api/profile/>  
then select authorization and select Bearer Token and enter the copied token like  
following image  
![postman token input for doctor profile](/assets/postman_d_4.png)
on success you now retrieve your doctor profile  
![success response ](/assets/postman_d_5.png)

The detail behind the workflow which is code has been tried to explained by me in my webpage <http://www.19mddilshad.xyz/django.php>.
