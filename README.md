# HN Saved Links Export

This is a python script to export your saved links from [Hacker News](https://news.ycombinator.com/news). What's a saved link, you ask? Any story that you upvote on HN is added to your saved links. You can access your them from `https://news.ycombinator.com/saved?id=<username>` where `<username>` is your HN username.

### Instructions
1. This script depends on `lxml` and `requests` packages, which should be installed by default on most systems. If not, install them like so:
 ```bash
 $ pip install -r requirements.txt
 ```
 You might have to use `sudo` with that command on Linux.

2. Obtain the cookie while you are logged in to HN. You can do it by loading the page with the Networks tab of your browser's developer tools open. Check [this](http://storage8.static.itmages.com/i/16/0522/h_1463922946_3928666_d21ffff115.png) image.

3. Run the script and profit!
 ```bash
 $ python export_links.py
 ```

### Todo
- Add support for saving file as CSV
- Detect the number of pages automatically
- Add option to use username and password instead of cookie


### Similar
[HN Saved Export](https://github.com/thomaskcr/hn-saved-export) by thomaskcr

### Contribute
If you think of any improvements, create an issue or send a pull request. :)
