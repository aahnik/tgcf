Make sure you have read 
- [How to configure tgcf](https://github.com/aahnik/tgcf/wiki/How-to-configure-tgcf-%3F)
- [Plugins](https://github.com/aahnik/tgcf/wiki/Plugins)

The OCR plugin allows you to do Optical Character Recognition for images. 

If an image is posted in source chat, the image with text (ocr) caption will be sent to the destination chats.

To activate the OCR plugin, just put the line `ocr:` under the plugins section of your configuration file.

```yaml
plugins:
    # ... your other plugins here
    ocr:
    # ... other plugins
        
```

If you are running on your own computer,you must have [tesseract-ocr](https://github.com/tesseract-ocr/tesseract) installed in your system for this. 

If you are deploying to cloud platform, or running tgcf using the Docker method as per the instructions in the wiki, then there is nothing to worry. 