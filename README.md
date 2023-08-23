# HN Saved Links & Comments Export
This is a python script to export your saved links from [Hacker News](https://news.ycombinator.com/news). What's a saved link, you ask? Any story that you upvote on HN is added to your saved links. You can access them at `https://news.ycombinator.com/upvoted?id=<your username>` while logged in.
I've added also a python script to export the comment that have been upvoted.

### Instructions
Python 3 is required to run this. If you don't have it installed, install it using the package manager for your OS before following these instructions.

1. Setup a virtual env (recommended, but optional) and install the dependencies:
    ```bash
    # Set up and activate a Python 3 virtual env
    $ python3 -m venv venv
    $ source venv/bin/activate

    # Install dependencies
    $ pip install -r requirements.txt
    ```
    You might have to use `sudo` with the last command on Linux.

2. Run the script export_links.py and enter your HN login credentials.
    ```bash
    $ python3 export_links.py
    Enter your HN account details:
    Username: amjd
    Password: [password will be hidden]
    ```

3. After all the links are processed, you will be asked to enter an output file name. Use any name with the  extension `.json` or `.csv`, or leave blank to go with the default `links.json`. The output file will be saved in the appropriate format.

4. Run the script export_comments.py and enter your HN login credentials.
    ```bash
    $ python3 export_comments.py
    Enter your HN account details:
    Username: amjd
    Password: [password will be hidden]
    ```

3. After all the comments are processed, you will be asked to enter an output file name. Use any name with the  extension `.json` or `.csv`, or leave blank to go with the default `comments.json`. The output file will be saved in the appropriate format.

5. Profit!

P.S.: Your username and password are **100% safe** and are sent over HTTPS. You can study the source code of this small script to verify that.

### Sample output: links.json
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

### Sample output: comments.json
JSON:
```json
{
  "total": 163,
  "links": [
    {
        "author": "FireInsight",
        "author_url": "https://news.ycombinator.com/user?id=FireInsight",
        "age": "1 day ago",
        "story_title": "Show HN: Writedown - Open Source Markdown Diary",
        "story_url": "https://news.ycombinator.com/item?id=36461866",
        "context": "https://news.ycombinator.com/context?id=36466326",
        "comment": "I use logseq for my diaries. https://logseq.com/It's very powerful, but really doesn't feel that way. Each day I open it, it creates a new YYYY-MM-DD.md and shows it to me. All content is MD lists (or \"blocks\") and can be individually tagged with #hashtags. When there's a certain topic I wrote about, say writing down a dream I had, I tag the top-level block with #dream. Then I can write under it as I please. All such blocks will be visible on the #dream page, with the correct dates visible.It's very easy to wrap my head around. I just write, outliner style, whatever I'm thinking of and want to write down. Never need to create a new page, always just directly to writing. Earlier dates can be found by just scrolling down.I don't know why anyone with the technical knowhow to use a notetaking tool that's just a folder with markdown files would use a journaling app on some server somewhere. Syncing is very easily handled, too, with something like Syncthing or Dropbox."
    },
    {
        "author": "JusticeJuice",
        "author_url": "https://news.ycombinator.com/user?id=JusticeJuice",
        "age": "2 days ago",
        "story_title": "Arwes: Futuristic Sci-Fi UI Web Framework",
        "story_url": "https://news.ycombinator.com/item?id=36446637",
        "context": "https://news.ycombinator.com/context?id=36449381",
        "comment": "https://www.hudsandguis.com/ - more FUI work, one of my favourite sites."
    },

  "..."
    {
        "author": "danenania",
        "author_url": "https://news.ycombinator.com/user?id=danenania",
        "age": "on May 18, 2022",
        "story_title": "I spent two years launching tiny projects",
        "story_url": "https://news.ycombinator.com/item?id=31421364",
        "context": "https://news.ycombinator.com/context?id=31424699",
        "comment": "Check out the #buildinpublic hashtag on Twitter. You\u2019ll find many good examples.Also Indiehackers."
    }
  ]
}
```
### Original
[HN Saved Export](https://github.com/amjd/HN-Saved-Links-Export) by amjd

### Similar
[HN Saved Export](https://github.com/thomaskcr/hn-saved-export) by thomaskcr

### Contribute
If you think of any improvements, create an issue or send a pull request. :)
