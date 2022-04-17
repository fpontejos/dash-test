## Test deploy Dash app to Render.com

1. Sign up for render.com account

1. Verify your email 
 
![Screenshot](https://raw.githubusercontent.com/fpontejos/dash-test/main/imgs/01.png)

1. Create a new web service

![Screenshot](https://raw.githubusercontent.com/fpontejos/dash-test/main/imgs/02.png)

1. Click on the GitHub link to connect your GitHub account 

![Screenshot](https://raw.githubusercontent.com/fpontejos/dash-test/main/imgs/03.png)

1. Allow all the things

![Screenshot](https://raw.githubusercontent.com/fpontejos/dash-test/main/imgs/04.png)

1. Choose the repo you want it to see (or allow all)

![Screenshot](https://raw.githubusercontent.com/fpontejos/dash-test/main/imgs/05.png)

1. Select the repo 

![Screenshot](https://raw.githubusercontent.com/fpontejos/dash-test/main/imgs/07.png)

1. Configure some settings. 

**Important:**  

- Environment (Python 3)

- start command

```
gunicorn app:server
```

(Or whatever the equivalent is to your Heroku Procfile)

**Click Advanced**

![Screenshot](https://raw.githubusercontent.com/fpontejos/dash-test/main/imgs/08.png)


Add Environment Variables: Python Version (whichever one you are using that works)