The application `tgcf` is configured using a simple `YAML` file. If you are new to the `YAML` syntax, don't worry, it's easy, and you will learn it.

## Introducing YAML

Tutorials on YAML syntax:
- [Article by Tutorial Point](https://www.tutorialspoint.com/yaml/yaml_basics.htm) 
- [Article by W3 Schools](https://www.w3schools.io/file/yaml-cheatsheet-syntax) 
- [YouTube video by Nana](https://youtu.be/1uFVr15xDGg?t=73)

## Where to write

You may write your configuration in the `tgcf.config.yml` file. (when running on your own computer)

When you are deploying on a cloud platform where you can't edit files, you may configure tgcf using environment variables. The contents of `tgcf.config.yml` can be put inside the environment variable called `TGCF_CONFIG`. Read the wiki for platform-specific guides on how to set environment variables in different platforms.


## Example Configuration

- For the `source` and `dest` fields use the username of the channel/bot/person/group. (omit the `@` symbol at the start). 
- If the private entity does not have a username, you may use the link of the private channel/group.

Below is an example configuration. Don't copy-paste this. Understand what each part does.

```yaml
admins: [yourUserName,AnotherPerson] 
# when tgcf is run in live mode, the admins can run commands to change the configuration

forwards:
  - source: channelName
    dest: [anotherChannel,https://t.me/channelLink]
    # use username or link of the entity


show_forwarded_from: false

plugins:
  filter:
    text:
      blacklist: ["nope"]
  replace:
    text:
      god: devil
      tokyo: delhi
      
```

## Schema

Here is the complete schema for the configuration file.

- `admins` (the list of usernames or ids of the admins)
    > - setting admins is not compulsory
    > - if no admins are set, and you run tgcf in live mode, then no one can run commands to change the configuration. 
    > - the bot/user bot **will work perfectly fine** as per your configuration file
- `forwards` (a list of forward objects)
    - forward ( contains a `source` (string), a `dest` (list of strings) and an `offset`(optional integer) )
- `show_forwarded_from` (boolean: true/false)
- `live`
   - `delete_sync` : bool (true or false)
- `past`
   - `delay`: int (between 1 to 100 )(seconds) (time to wait after every message is sent)


- `plugins` contain the name of the plugin and the data to be passed to that plugin.
   - What data to pass to plugins? is defined in the documentation for that plugin. Here is the [list of all plugins](https://github.com/aahnik/tgcf/wiki/Plugins).

