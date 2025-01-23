# URL Shortening Service

1. Create a Python environment:
```commandline
python -m venv url_shortener_pyenv
```

2. Activate the Python environment:
```commandline
source activate url_shortener_pyenv/bin/activate
```

3. Install the necessary packages to run the web service:
```commandline
pip install -r requirements.txt
```

4. Start the Flask server:
```commandline
python app.py
```

5. Start Redis:
```commandline
docker compose up 
```

6. Open Postman.

7. Send a POST request to shorten a URL using the information shown in the below screenshot:

![Deeban Ramalingam - URL Shortener - Get Short URL Screenshot.png](README-screenshots/Deeban%20Ramalingam%20-%20URL%20Shortener%20-%20Get%20Short%20URL%20Screenshot.png)

8. Send another POST request to retrieve the original URL using the information shown in the below screenshot:

![Deeban Ramalingam - URL Shortener - Get Long URL Screenshot.png](README-screenshots/Deeban%20Ramalingam%20-%20URL%20Shortener%20-%20Get%20Long%20URL%20Screenshot.png)
