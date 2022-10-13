<div id="top"></div>


<!-- PROJECT LOGO -->
<br />
<div align="center">
<h3 align="center">Frodo</h3>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

<div align="center">
<img src="imgs/frodo.png" alt="output_dat" >
</div>

Frodo is a Near Real-Time Credit Card Fraud Detection Simulation. It simulates how a producer ideally a bank or any commercial banking software can make sure the credit card transactions carried out are valid to an extent. The simulation consists for three major components. The producer, the consumer and the dashboard. The producer as mentioned before being the banks, commercial softwares, the consumer being the machine learning model trained on the Credit Card dataset from Kaggle using an XGBoost Classifier and finally an App that displays the result in real-time developed using the Flask microframework.

### Build With

* Python
* RabbitMQ
* PostGreSQL

### Packages Used


* Flask
* Flask-SQLAlchemy
* Psycopg2
* Flask-Mail
* Flask-Login
* Flask-Migrate
* Pika
* APScheduler

### File Structure
/root -> Houses the Main API and the Mailing and Scheduler Services as 2 different folders 

/root/mailer -> Mailing Service 

/root/scheduler -> Schduler CRON Job that Checks the PostGresQL database for triggering any alerts 



<!-- USAGE EXAMPLES -->
## Usage

To run the code as of now first start the PostGres and RabbitMQ services. After that start the Main API followed by the scheduler and mailer services.

Requests to the API will create alerts: 
 
 * `/auth/register` - To create a user. `email` and `password` have to be passed in.
 * `/auth/login` - Logs in valid users and returns `token`.
 * `/alerts/create` - Creates a new alert
 * `/alerts/delete` - Deletes an alert
 * `/alerts/fetch_all` - Returns list of all alerts created so far
 * `/alerts/fetch_all/<FILTER>` - Returns the list filtered by status, which can be one of "TRIGGERED", "CREATED", "DELETED"
 

## Examples


 Making an invalid login request
   
 

<div align="center">
<img src="imgs/invalidlog.png" alt="output_dat" >
</div>

<br>
<br>


 Making an account and retrieving the token
   
   
<div align="center">
<img src="imgs/register.png"  >
</div>

Making the Alert
<div align="center">
<img src="imgs/createalert.png" >
</div>

Fetching Alerts
<div align="center">
<img src="imgs/fetch.png"  >
</div>

Email Triggered for Alert
<div align="center">
<img src="imgs/email Triggered by scheduler.png"  >
</div>

Email Triggered By Mailing Service which was received from RabbitMQ
<div align="center">
<img src="imgs/emailreceivedatmailer.png"  >
</div>

Updated Database
<div align="center">
<img src="imgs/updateddb.png"  >
</div>

## How to Run
- Setup a virtual environment and then run `pip install -r requirements.txt` in root folder 
- Start PostgreSQL service with username as user and password as pass. If you have an existing server then just create an environment variable `DB_URI` as  `postgres://user:password@localhost:port`
- For running main server set environment variable `FLASK_APP` as `Krypto.py`, while running the first time run the following commands `flask db init`, `flask db migrate`, `flask db upgrade`
- Now use `python Krypto.py` the server will start and the API is accessible at port 8000
- Start the RabbitMQ service using `docker run -d --hostname my-rabbit --name some-rabbit -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=password rabbitmq:3-management`
- Now cd into scheduler service and start that service using `python scheduler.py`, this service wil fetch untriggered alerts and check if they have to be triggered, in that case a request is placed on the rabbit mq broker.
- Now cd into mailer folder and start the flask_mail.py service. This service listens to the RabbitMQ broker and processes or consumes the requests as they come in.
- The request is then printed onto the console.

<!-- ROADMAP -->
## Tasks Done

- [x] Create API Endpoint for creating an alert
- [x] Creating API Endpoint for deleting an alert
- [x] Creating API Endpoint for fetching all alerts
- [x] Creating API Endpoint to return alerts filtered by status
- [ ] Paginate the response
- [x] Add User Authentication with JWT
- [x] Make use of coingecko API for price checking
- [x] Printing the mail procedure to console as google removed access to less secure apps for my account
- [ ] Adding a cache layer for the fetch_all endpoint
- [x] Use PostGres
- [x] Use RabbitMQ
- [ ] Bundle in Docker-Compose





## Contact

Adithya Narayan - [@a.dity.a_n.araya.n](https://www.instagram.com/a.dity.a_n.araya.n/?hl=en) - adithyanarayan1234@gmail.com





[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/adithya-narayan-3747081a3/
[product-screenshot]: images/screenshot.png
