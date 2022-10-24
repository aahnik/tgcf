Heroku is a cloud platform that lets companies build, deliver, monitor, and scale apps, it is one of the fastest ways to go from idea to URL, bypassing all those infrastructure headaches.

You can deploy `tgcf` to Heroku very easily. 

## Limitations

- Heroku has an ephemeral file system. 
- Thus you cant store your files here. 
- `tgcf.config.yml` can't be created here. 
- Instead, you can use an environment variable named `TGCF_CONFIG` to store the contents of the configuration file.
- `tgcf` in past mode won't work properly in Heroku, as the environment variable TGCF_CONFIG can't be updated.

## Pros

- `tgcf` will work **perfectly fine** in `live` mode in Heroku.
- Heroku offers a great free tier of 450 hrs/mo

## One-click deploy

1. Make sure you have a Heroku account and then click on this button. 

   <a href="https://heroku.com/deploy?template=https://github.com/aahnik/tgcf">   <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy to Heroku" width=155></a>

2. A Heroku page will open where you can set all the environment variables.

- Set the name of the app whatever you want.

  ![image](https://user-images.githubusercontent.com/66209958/115880520-7287f980-a468-11eb-9bfc-5a72cbe668d9.png)

- Set your API ID and API HASH obtained from [my.telegram.org](https://my.telegram.org). Set the mode to `live`.


- You may keep your `SESSION_STRING` and `TGCF_CONFIG` empty for now.


- Now click the deploy app button.


3. It will take some time to build and deploy. After the deployment is complete, click on the manage app button.
   ![image](https://user-images.githubusercontent.com/66209958/115881849-cb0bc680-a469-11eb-8b35-6bf5c6a5eca4.png)

4. How to get the session string? [Read this](https://github.com/aahnik/tgcf/wiki/Login-with-a-bot-or-user-account#generate-session-string).

5. Now go to the settings tab and click Reveal config vars. Click on the pencil button for the session string and config var, and then paste the session string the value of that.

6. Learn [how to configure tgcf](https://github.com/aahnik/tgcf/wiki/How-to-configure-tgcf-%3F), and then write your configuration in the `TGCF_CONFIG` env var.

7. Go to the resources tab, and turn on the worker and click confirm.

![image](https://user-images.githubusercontent.com/66209958/115882913-dc090780-a46a-11eb-980b-6b0f49ff45f5.png)