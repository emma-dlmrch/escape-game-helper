# Escape Game Help

## About

This project is a tool used to create escape games. It includes an admin section where, as a game maker, the user can create and organise games, riddles, clues, and different scenarios, and
a play section where players can follow a game scenario and submit their answers to unlock game steps.

An instance is deployed and accessible here:
https://escapegamehelper.ovh 

## Built with
* Django REST Framework
* Vue.JS 3

## Contributing

Anyone willing to improve this project is welcome to fork the repo and create a pull request !

1. Fork the project
2. Create a feature branch (git checkout -b feature/YourFeature)
3. Commit your changes (git commit -m 'Add some feature')
4. Push to the Branch (git push origin feature/YourFeature)
5. Open a Pull Request

You are also welcome to open issues on the project to suggest improvements or report bugs.

## Local installation 

Prerequisites:
- Node.js 17.4.0 / npm 8.3.1
- Python 3.11.4

1. Clone the repository
`git clone https://github.com/emma-dlmrch/escape-game-helper.git`

2. Backend
    - Create a python environment
    (Windows: )
    ```
    py -m venv env
    source env/Scripts/activate
    ```

    - Install the requirements
    ```
    pip install django
    pip install -r requirements.txt
    ```
    - Apply the migrations
    ```
    cd backend/
    py manage.py migrate
    ```
    - Create /escapegameapi/local_settings.py according to /escapegameapi/local_settings.py_sample
    - Run the backend
    ```
    py manage.py runserver
    ```

3. Frontend
    - Install packages
    ```
    cd frontend/
    npm install
    ```
    - Create /src/settings.js according to /src/settings.js_sample
    - Run the frontend
    ```
    npm run serve
    ```

## License

AGPL v3


