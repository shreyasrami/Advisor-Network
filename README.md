# Advisor-Network

An Advisor Network where admin can add new advisors and users can view all the advisors. Users can also book calls with advisors on the desired time and can view details of all the calls booked by them.
API endpoints created for all these functionalities.

## Installation Instructions

1. Clone the project.
    ```shell
    $ git clone https://github.com/shreyasrami/Advisor-Network.git
    ```

2. Create a new virtual environment activate it.
    ```shell
    $ python3 -m venv env
    $ source env/bin/activate
    ```
3. Install dependencies from requirements.txt:
    ```shell
    (env)$ pip install -r requirements.txt
    ```
     
4. Migrate the database.
    ```shell
    (env)$ python manage.py migrate
    ```

5. Run the local server via:
    ```shell
    (env)$ python manage.py runserver
    ```

### Done!
The local application will be available at <a href="http://localhost:8000" target="_blank">http://localhost:8000</a>.

### Detailed API Documentation can be viewed at <a href="http://localhost:8000/docs/" target="_blank">http://localhost:8000/docs/</a>.

## Contributing
Pull requests are welcome. For major
changes, please open an issue first 
to discuss what you would like to change.