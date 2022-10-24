Filters allow you to selectively forward some messages while excluding others.



For an intro to configuration [read this](https://github.com/aahnik/tgcf/wiki/How-to-configure-tgcf-%3F) page.

## Example

```yaml
plugins:
  filter:

    text:
      case_sensitive: true # default is false if you don't write this line
      # the case_sensitive param has no significance if regex is set to true    
      whitelist: ["this word"]
      blacklist: ["hello"]
      regex: false # default is false. 
      # set to true if you want the expressions in whitelist and blacklist 
      # to be evaluated as regular expressions

    users:
      blacklist: [1547315064] # currently user ids are supported only. 
      # get user ids from @userinfobot on telegram

    files:
      whitelist: [document,nofile] 
      # valid types are 
      # audio,gif,video,video_note,sticker,contact,photo,document,nofile
    

```

Note:
- for text filtering, you may use whitelist or blacklist or both
- for users and files filtering, use either a whitelist or a blacklist
