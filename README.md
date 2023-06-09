# My App

My App is a Python application that uses Kafka and MongoDB to process data.

## Building and Running the Containers

To build and run the containers for My App, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the root directory of the repository.
3. Run the following command to build the containers:


` docker-compose build `

4. Run the following command to start the containers:

`docker-compose up`


This will start the Kafka and MongoDB containers, as well as the `consumer` and `producer` containers for My App.

5. Once the containers are running, you can access the application at `http://localhost:5000`.

The `producer` container will generate data and send it to the Kafka topic. The `consumer` container will consume the data from the Kafka topic and store it in the MongoDB database.

You can view the data in the MongoDB database by connecting to the `mongo1` container and running the `mongo` command-line tool.

`docker exec -it mongo1 mongo`

This will open the MongoDB shell, where you can run commands to view the data.

## License

My App is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

### In order to scale the consumer you can use the following command:

`docker-compose up --scale consumer=3`