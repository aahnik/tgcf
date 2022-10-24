For an intro to configuration [read this](https://github.com/aahnik/tgcf/wiki/How-to-configure-tgcf-%3F) page.

## Simple Replacement

Inside your configuration under the plugins section put this:

```yaml
plugins:
  replace:
    text:
      "god": devil
      "smart": idiot
      "original": new
```

In the above example, "god" will be replaced by "devil" and "smart" will be replaced by "idiot" and so on.

## Using Regex

If you want to use regex, you can do so, by setting `regex: true`.

Example:

```yaml
plugins:
  replace:
    text:
      "regex pattern": "new word"

    regex: true
```







