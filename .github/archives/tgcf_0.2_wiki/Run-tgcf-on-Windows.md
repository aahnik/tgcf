Windows is a mess! In Linux or Mac, a terminal and python are generally pre-installed. But that's not the case with windows.

Here goes the complete guide to set up and use `tgcf` on a Windows machine.

## Pre-requisites

1. Open Microsoft Store

   ![image](https://user-images.githubusercontent.com/66209958/115837680-7a2eaa80-a436-11eb-9cca-11e12694e8b3.png)

2. Install [Powershell]() , [Windows Terminal](), and Python 3.9


   ![image](https://user-images.githubusercontent.com/66209958/115838965-d0e8b400-a437-11eb-818a-652951ae44ee.png)

   ![image](https://user-images.githubusercontent.com/66209958/115839446-49e80b80-a438-11eb-9149-b93d6218e0dc.png)
    
   ![image](https://user-images.githubusercontent.com/66209958/115839540-608e6280-a438-11eb-91e6-9285cc6301ee.png)
   

   ![image](https://user-images.githubusercontent.com/66209958/115959754-644ee180-a52b-11eb-8ff7-a55692beb853.png)

3. By default windows has Notepad. Its a   horrible text editor. Windows file explorer is also shitty. It appends `.txt` to every text file. For a better experience, Install VS Code from [code.visualstudio.com](https://code.visualstudio.com/) for easy editing of text files.
When you will be writing the `tgcf.config.yml` VS code will automatically provide syntax highlighting and type checking.
   ![Screenshot (7)](https://user-images.githubusercontent.com/66209958/115840953-e4951a00-a439-11eb-9db4-b87733e2dd98.png)

## Install tgcf

 Open Powershell in Windows Terminal and run pip install tgcf

   ![image](https://user-images.githubusercontent.com/66209958/115841408-6127f880-a43a-11eb-92fd-215ab3a4c8aa.png)


## Configure and Run

1. You should create a new folder to store `tgcf` configuration files. Every time you run `tgcf` you should run from inside this folder. 

2. Open the folder with VS Code and create the files `.env` and `config.tgcf.yml`. 
You will be required to login to your Telegram account only for the first time. The session files will be stored in this folder. Don't delete them, and keep them secret.
, go inside it, create .env and tgcf.config.yml, run tgcf
![Screenshot (12)](https://user-images.githubusercontent.com/66209958/115847554-b5ce7200-a440-11eb-93e0-55de40a611e5.png)
![Screenshot (13)](https://user-images.githubusercontent.com/66209958/115847567-b8c96280-a440-11eb-8540-34dd89c273c9.png)
![Screenshot (14)](https://user-images.githubusercontent.com/66209958/115847578-bbc45300-a440-11eb-8dff-6e9f163885ba.png)
![Screenshot (15)](https://user-images.githubusercontent.com/66209958/115847590-be26ad00-a440-11eb-9879-b78cabef0d2d.png)
![Screenshot (17)](https://user-images.githubusercontent.com/66209958/115847693-d5659a80-a440-11eb-9e3e-fcdff16c3c97.png)

3. Open terminal in VS Code and run tgcf

![Screenshot (19)](https://user-images.githubusercontent.com/66209958/115848550-9f74e600-a441-11eb-92bb-ee014a9639c7.png)
![Screenshot (20)](https://user-images.githubusercontent.com/66209958/115848561-a1d74000-a441-11eb-87c7-731be1bcbca9.png)

Every time, run tgcf from the same folder.

