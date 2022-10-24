An environment variable is a dynamic-named value that can affect the way running processes will behave on a computer. They are part of the environment in which a process runs.

The secret credentials like `API_ID` and `API_HASH` are stored as environment variables.

## All env vars

| Env Var          | Value                                                        | Requirement                                                  |
| ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **`API_ID`**     | obtain it from [my.telegram.org](https://my.telegram.org)    | always required                                              |
| **`API_HASH`**   | obtain it from [my.telegram.org](https://my.telegram.org)    | always required                                              |
| `TGCF_MODE`      | [`past` or `live`](https://github.com/aahnik/tgcf/wiki/Past-vs-Live-modes-explained) | only required if you don't have interactive shell while running `tgcf`. |
| `BOT_TOKEN`      | obtained from [@BotFather](https://telegram.me/BotFather)    | required if you are running`tgcf`with a bot account.         |
| `SESSION_STRING` | obtained after [login](https://github.com/aahnik/tgcf/wiki/Login-with-a-bot-or-user-account#generate-session-string) | only required if you are using `tgcf`with user account.      |
| `TGCF_CONFIG`    | contents of [`tgcf.config.yml`](https://github.com/aahnik/tgcf/wiki/How-to-configure-tgcf-%3F) | only required if you cant edit files in your cloud deploy (digital ocean app or heroku dyno) |




## Setting env vars

There are various methods to set env vars

### `.env` File

You can easily set environment variables for `tgcf` using a `.env` file in the directory from which `tgcf` is invoked.

```shell
API_ID=543213
API_HASH=uihfuiwruiw28490238huawfiuhf
# put your real values here
```

### Cloud Deploys

When you are deploying to a cloud platform, and you cant create files (Heroku or digital ocean apps), you can set environment variables using the GUI provided by the platforms. Please read platform-specific guides in the wiki for more details.

When you are deploying on a cloud platform, you can configure tgcf using environment variables. The contents of `tgcf.config.yml` can be put inside the environment variable called `TGCF_CONFIG`.