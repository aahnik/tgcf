### [WARNING] ❗this document is not up-to-date with the latest changes of tgcf. Please re-visit after a few days.

<br>
<br>
<br>
<br>


This tutorial is for python developers. If you are a general user, you may make a feature request for a plugin you need.

## Prerequisites
- Intermediate level knowledge of [Python](https://python.org) programming language
- Basic knowledge of [Telethon](https://github.com/LonamiWebs/Telethon)
- Some idea about how `tgcf` works


Writing a plugin is a piece of cake. A plugin is basically a python module that can be imported by `tgcf`. You can even package it and publish it to PyPI for providing an easy `pip install` for your users.

## Naming Rules

The plugin name (also known as plugin id) should be a single word in lowercase describing the feature.

For example: if your plugin name is `hello`, then the name of the package should be `tgcf_hello`, and the name of the plugin class should be `TgcfHello`.

## Write your first plugin

First of all, create a folder named `tgcf_hello`, and inside it create `__init__.py`. For the sake of simplicity, in this example, we will be writing our logic inside `__init__.py`. For complex plugins, you can have multiple modules and even sub-packages.


```python
# __init__.py


class TgcfHello:
    id = "hello"
    # the plugin class must have this `id` attribute

    def __init__(self, data):
        # the plugin class must have a constructor and should validate data here
        self.data = data

    def modify(self, message):
        # the modify method, receives the message collected by tgcf
        # the output of this method will be forwarded

        # manipulate the message here
        return message

```

More details to be added soon!
