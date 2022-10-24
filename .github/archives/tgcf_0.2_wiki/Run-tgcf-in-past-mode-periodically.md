You can set up cron jobs!

for free using GitHub Actions scheduled workflows.

Or, you may even trigger the workflow manually!

How to do ?

Step1. Go to https://github.com/aahnik/tgcf-on-gh-action

Step2. Click on the "use this template" button

![image](https://user-images.githubusercontent.com/66209958/117601342-b880d500-b16b-11eb-91a2-2f1bf1ccec6a.png)

Step3. Give any interesting name to your repo, and make it public (unlimited free) or private (limited to action minutes per month).

![image](https://user-images.githubusercontent.com/66209958/117601415-f251db80-b16b-11eb-85ca-24ebc28ec3f5.png)

If your repo is public, only your configuration file will be visible to others. Your secrets such as API_ID, API_HASH,SESSION_STRING, are stored safe in github secrets.

Step4. Go to settings -> secrets of the repo

Create the following secrets

1. API_ID
2. API_HASH
3. SESSION_STRING (get it from [here](https://github.com/aahnik/tgcf/wiki/Login-with-a-bot-or-user-account#generate-session-string) )

![image](https://user-images.githubusercontent.com/66209958/117601591-62f8f800-b16c-11eb-8b9f-a45d69afca2c.png)

Step5. Edit the `tgcf.config.yml` file according to your needs,


Step6. Go to the Actions tab -> Select tgcf-past -> Run workflow

![image](https://user-images.githubusercontent.com/66209958/117601708-a0f61c00-b16c-11eb-9f2b-c525b24a4064.png)

To run periodically, set a schedule for `on` param in your workflow file

for cron syntax use https://crontab.guru/ or https://cron.help/

