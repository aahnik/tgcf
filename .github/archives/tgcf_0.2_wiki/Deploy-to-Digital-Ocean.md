DigitalOcean infrastructure is a leading cloud service provider based in the United States of America. Their headquarter operates from New York City, and their data centers are prevalent in every corner of the world in order to provide seamless cloud services across the globe.


## App Platform


![create-app](https://user-images.githubusercontent.com/66209958/113475188-aab3a200-9491-11eb-8649-9c4111d05a1b.png)

Click **Create** -> *Apps*


![source-is-docker-hub](https://user-images.githubusercontent.com/66209958/113475207-c1f28f80-9491-11eb-84d1-5b90e6a4ee3c.png)

Choose **Docker Hub** as the source.
Choose the **type** as _"Worker"_ (as we are not making any web app).

In the next step,the **repository** path is _"aahnik/tgcf"_.

![type-worker](https://user-images.githubusercontent.com/66209958/113475243-fbc39600-9491-11eb-9c2e-96fb0487d43d.png)

You can now set the values of the [environment variables](https://github.com/aahnik/tgcf/wiki/Environment-Variables) from this beautiful interface provided by Digital Ocean.


Give any name to your app. After this, you will be lead to a pricing page. Choose a pricing plan suitable for you and click "Launch basic app".



## Ubuntu Droplet

If you want more control, you may run `tgcf` on a VPS like DigitalOcean's ubuntu droplets.

Steps:
- Create a Droplet
- SSH into it
- Update packages
- Install python
- Install `tgcf`
- Use `tgcf` CLI

Details coming soon!