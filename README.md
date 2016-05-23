# HN Saved Links Export

This is a python script to export your saved links from [Hacker News](https://news.ycombinator.com/news). What's a saved link, you ask? Any story that you upvote on HN is added to your saved links. You can access them from `https://news.ycombinator.com/saved?id=<username>` where `<username>` is your HN username.

### Instructions
1. This script depends on `lxml` and `requests` packages, which should be installed by default on most systems. If not, install them like so:
 ```bash
 $ pip install -r requirements.txt
 ```
 You might have to use `sudo` with that command on Linux.

2. Run the script and enter your HN login credentials.
 ```bash
 $ python export_links.py
 Enter your HN account details:
 Username: amjd
 Password: [password will be hidden]
 ```

3. After all the links are processed, you will be asked to enter an output file name. Use any name with the  extension `.json` or `.csv`, or leave blank to go with the default `links.json`. The output file will be saved in the appropriate format.

4. Profit!

P.S.: Your username and password are **100% safe** and are sent over HTTPS. You can study the source code of this small script to verify that.

### Todo
- Add CLI options


### Similar
[HN Saved Export](https://github.com/thomaskcr/hn-saved-export) by thomaskcr

### Contribute
If you think of any improvements, create an issue or send a pull request. :)
