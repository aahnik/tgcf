# `tgcf`

tgcf is a powerful tool for forwarding telegram messages or live syncing. Make sure you have API_ID and API_HASH in your .env file inside the current directory.
    

**Usage**:

```console
$ tgcf [OPTIONS]
```

**Options**:

* `-n, --name TEXT`: Name of the bot/userbot you want to run.  [env var: NAME; required]
* `-t, --token TEXT`: Bot Token or Session String  [env var: TOKEN; required]
* `--API_ID INTEGER`: API ID obtained from my.telegram.org  [env var: API_ID; required]
* `--API_HASH TEXT`: API HASH obtained from my.telegram.org  [env var: API_HASH; required]
* `-l, --loud`: Increase output verbosity.  [env var: LOUD]
* `-v, --version`: Show version and exit.
* `--help`: Show this message and exit.
