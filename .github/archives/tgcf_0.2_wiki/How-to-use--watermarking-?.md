Make sure you have read 
- [How to configure tgcf](https://github.com/aahnik/tgcf/wiki/How-to-configure-tgcf-%3F)
- [Plugins](https://github.com/aahnik/tgcf/wiki/Plugins)

The `mark` plugin allows you to apply a watermark on images/videos/gifs.

If an image/video/gif is posted in the source chat, the watermarked version will be sent to the destination chat.

Just put this in your configuration file.

```yaml
plugins:
   # ... your other plugins here
    mark:
        image: /path/to/image.png # the image to apply as watermark
        # this can be a local path, or an URL starting with https://
```

If you are running on your own computer,you must have [ffmpeg](https://ffmpeg.org/) installed in your system for this. 

If you are deploying to cloud platform, or running tgcf using the Docker method as per the instructions in the wiki, then there is nothing to worry. 