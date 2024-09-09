
# How to run the application on your computer

- First download it using 
    ```
    git clone https://github.com/kunal763/model.git
    ```
- Clone this and then make a virtual env
    ```
    python -m venv .venv

    ```
    before doing this python should be installed in your system
- activate this virtual env by running
    ```
    .venv\Scripts\activate
    ```
- now go into the directory which you have cloned using
    ```
    cd model
    ```
- Install all the requirements
    ```
    pip install -r requirements.txt
    ```
- Now just run this project using 
    ```
    cd Mlapi
    python manage.py runserver 8000
    ```
    This will start the project at port 8000
- Now access this project by clicking the link 
    [http://127.0.0.1:8000/api](http://127.0.0.1:8000/api)

