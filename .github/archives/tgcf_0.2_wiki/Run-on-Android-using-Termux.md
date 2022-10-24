Hopefully, you have already read the README for a basic introduction to `tgcf`.

The Termux app in Android offers you a full-blown Linux terminal.

[![image](https://user-images.githubusercontent.com/66209958/115503616-559acd00-a294-11eb-8909-a27ff9a6efd6.png)](https://play.google.com/store/apps/details?id=com.termux&hl=en&gl=US)

Install [Termux](https://play.google.com/store/apps/details?id=com.termux&hl=en&gl=US) from Google Play Store.

> **Note:** Termux does not work well with Android 5 or 6. Don't worry! Most probably you have a much newer version of Android.

## Install `tgcf` on termux

Just open your termux and run this:

```shell
curl -Lks bit.ly/tgcf-termux | bash
```

<details>
<summary> What happens when you run the above line? </summary>
<br>

- The above line (the installation command) actually fetches the installer script and runs it using bash. 
- Read the installer script by visiting the link [bit.ly/tgcf-termux](http://bit.ly/tgcf-termux). You may execute the lines one by one, manually.

</details>



## Testing

To test if `tgcf` was properly installed, 

```shell
tgcf --version
```

It should output version no. and that should match with the version of the [latest release](https://github.com/aahnik/tgcf/releases). 

## Configure and run

Learn about 
   - [environment variables](https://github.com/aahnik/tgcf/wiki/Environment-Variables), 
   - [CLI usage](https://github.com/aahnik/tgcf/wiki/CLI-Usage) and 
   - how to [configure tgcf](https://github.com/aahnik/tgcf/wiki/How-to-configure-tgcf-%3F), 
   and then start using `tgcf`.

When you install `tgcf` using the above method, the text editor `micro` is also installed. You can use `micro` to edit text files.



