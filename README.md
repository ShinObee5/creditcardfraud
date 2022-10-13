<div id="top"></div>


<!-- PROJECT LOGO -->
<br />
<div align="center">
<img src="imgs/frodo.png" alt="output_dat" >
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

Frodo is a Near Real-Time Credit Card Fraud Detection Simulation. It simulates how a producer ideally a bank or any commercial banking software can make sure the credit card transactions carried out are valid to an extent. The simulation consists for three major components. The producer, the consumer and the dashboard. The producer as mentioned before being the banks, commercial softwares, the consumer being the machine learning model trained on the Credit Card dataset from Kaggle using an XGBoost Classifier and finally an App that displays the result in real-time developed using the Flask microframework.

### Build With

* Python
* RabbitMQ
* PostGreSQL

### Packages Used

* Flask
* SQLAlchemy
* Pika
* XGBoost
* NumPy
* Pandas

### File Structure

- `sample/` - Directory containing code that was used to initially test the XGBoost Model
- `consumer/` - Directory housing the 2 essential components of the whole project, the **consumer** and the **dashboard**
- `producer/` - Directory containing code to emulate data producers like ATM, banking software etc.,

<!-- USAGE EXAMPLES -->
## Components

1. Consumer

This microservice has 2 functinalities or in other words two main purposes to it. The first one being receiving the data and getting the output from the machine learning model and saving the data in the database and the second one being exposing the webapp that will fetch and display the data from the database as it keeps getting updated.
 - `app.py` - Flask Application that renders the UI and keeps it updated with the latest entries in the database
 -  `consumer.py` - Consumer Application that reads from Queue and predicts the output. The consumer program can be run using the `--restart` flag to recreate the tables while working in local system.
 -  `model.py` - Schema definition for the transaction database model
 -  `start.sh` - Bashscript for starting both the listener service and the web service

2. Producer

This microservice emulates the real time data senders. The producer has with it a CSV file consisting of about 700 rows of data which is fed into the queue for the consumption of the consumer. The rate of dispatch is 1 row per 5s.
  

## How to Run
- Setup a virtual environment and then run `pip install -r requirements.txt` in root folder 
- Clone the repository using `git clone <url>`
- Run the command `docker-compose up`
- All services should be running as containers
- Now one can check `127.0.0.1:8000` for updated row entries of creditcard data




