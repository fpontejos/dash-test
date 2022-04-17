## Test deploy Dash app to Render.com

1. Sign up for render.com account

1. Verify your email 
 
![Screenshot](01.png)

1. Create a new web service

![Screenshot](02.png)

1. Click on the GitHub link to connect your GitHub account 

![Screenshot](03.png)

1. Allow all the things

![Screenshot](04.png)

1. Choose the repo you want it to see (or allow all)

![Screenshot](05.png)

1. Select the repo 

![Screenshot](07.png)

1. Configure some settings. 

**Important:**  

- Environment (Python 3)

- start command

```
gunicorn app:server
```

(Or whatever the equivalent is to your Heroku Procfile)

**Click Advanced**

![Screenshot](08.png)


Add Environment Variables: Python Version (whichever one you are using that works)