# beyond-us-hackathon

## Server setup

1. Clone this repo
   ```console
   git clone https://github.com/sabithbskumar/beyond-us-hackathon.git
   ```
2. Install requirements
   ```console
   cd beyond-us-hackathon
   pip install -r requirements.txt
   ```
3. Make database migrations
   ```console
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Create database manager
   ```console
   python manage.py createsuperuser
   ```
5. Start the server
   ```console
   python manage.py runserver
   ```

## Usage
Open web app by opening the url in the terminal and login with admin credentials.
