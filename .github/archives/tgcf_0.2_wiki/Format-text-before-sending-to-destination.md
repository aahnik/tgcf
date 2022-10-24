The `format` plugin allows you to force a style before sending the messages to destination chat.

Make sure you have read 
- [How to configure tgcf](https://github.com/aahnik/tgcf/wiki/How-to-configure-tgcf-%3F)
- [Plugins](https://github.com/aahnik/tgcf/wiki/Plugins)


To use the `format` plugin, put the following in your configuration file.

```yaml
plugins:
    # ... your other plugins here
    format:
        style: bold # choose from [ bold, italics, code, strike, plain, preserve ]
    # ... other plugins
        
```