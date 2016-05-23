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

### Sample output
JSON:
```json
{
  "total": 2661,
  "links": [
    {
      "author": "coloneltcb",
      "url": "https://m.signalvnoise.com/getting-from-%EF%B8%8F-%EF%B8%8F-to-%EF%B8%8F-%EF%B8%8F-%EF%B8%8F-%EF%B8%8F-%EF%B8%8F-c65cc3bb7cb1#.rgrwe5cnw",
      "age": "2 days ago",
      "title": "How to ask for reviews without feeling icky about it",
      "comments_url": "https://news.ycombinator.com/item?id=11740967",
      "number": 1,
      "comments": 28,
      "points": 79
    },
    {
      "author": "adventured",
      "url": "http://www.bloomberg.com/news/articles/2016-05-22/modi-s-mini-shuttle-set-to-blast-into-elon-musk-s-race-for-space",
      "age": "7 hours ago",
      "title": "India is set to launch a scale model of a reusable spacecraft on Monday",
      "comments_url": "https://news.ycombinator.com/item?id=11751776",
      "number": 2,
      "comments": 43,
      "points": 117
    },


    "..."
    
    
    {
      "author": "lydiahan",
      "url": "http://www.linkedin.com/today/post/article/20131029100222-95015-my-first-job-fired-and-rehired-on-day-1?trk=tod-home-art-list-small_1",
      "age": "931 days ago",
      "title": "My First Job: Fired and Rehired on Day 1",
      "comments_url": "https://news.ycombinator.com/item?id=6667202",
      "number": 2661,
      "comments": 113,
      "points": 199
    }
  ]
}
```

### Todo
- Add CLI options


### Similar
[HN Saved Export](https://github.com/thomaskcr/hn-saved-export) by thomaskcr

### Contribute
If you think of any improvements, create an issue or send a pull request. :)
