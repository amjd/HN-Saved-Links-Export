#!/usr/bin/env python

import csv
import json
import re
import requests
import signal
import sys

from getpass import getpass
from lxml import html

BASE_URL = "https://news.ycombinator.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:75.0) Gecko/20100101 Firefox/75.0",
}

def signal_handler(signal, frame):
    print("\nStopping...\n")
    sys.exit(130)


def save_json(saved_comments, file_name):
    result = {"total": len(saved_comments), "comments": saved_comments}
    with open(file_name, "w") as f:
        json.dump(result, f)

    print(f"\nComments saved to: {file_name}")


def save_csv(saved_comments, file_name):
    data = [
        (
            comment["author"],
            comment["author_url"],
            comment["age"],
            comment["story_title"],
            comment["story_url"],
            comment["context"],
            comment["comment"],
        )
        for comment in saved_comments
    ]
    with open(file_name, "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC, delimiter=",")
        writer.writerows(data)

    print(f"\Comments saved to: {file_name}")

def wait_for_page_load(url):
    session = requests.Session()
    while True:
        r = session.get(url, headers=headers)
        if r.status_code == 200:
            tree = html.fromstring(r.text)
            form_element = tree.cssselect("form[method='get'][action='//hn.algolia.com/']")
            if form_element:
                break
        else:
            break

def main():
    # Gracefully handle KeyboardInterrupt (Ctrl + C)
    signal.signal(signal.SIGINT, signal_handler)

    session = requests.Session()
    print("Enter your HN account details:")
    username = input("Username: ")
    password = getpass()

    try:
        print("\nLogging in...")

        r = session.post(f"{BASE_URL}/login", data={"acct": username, "pw": password})

        if session.cookies.get("user", None) is None:
            print("Error logging in. Verify the credentials and try again.")
            sys.exit(1)
        print("Logged in successfully.\n")
    except:
        print("Error logging in.\n")
        sys.exit(1)

    url = f"{BASE_URL}/upvoted?id={username}&comments=t&p="

    saved_comments = list()
    comments_processed = 0
    i = 1

    while True:
        try:
            print("Getting url: ", url + str(i))
            r = session.get(url + str(i), headers=headers)

            tree = html.fromstring(r.text)

            # Extract parts that contains the title and url for the stories
            tree_username = tree.cssselect("a.hnuser")
            tree_username_url = tree.cssselect("span.comhead a[href*='user']")
            tree_age = tree.cssselect("span.age")
            tree_onstory = tree.cssselect("span.onstory")
            tree_onstory_url = tree.cssselect("span.onstory a[href*='item']")
            tree_context_url = tree.cssselect("span.navs a[href*='context']")
            tree_commtext = tree.cssselect("span.commtext")

            # Number of username on the page
            n = len(tree_username)

            if n == 0:
                print(f"Processing page {i}. No comments found.")
                break

            print(f"Processing page {i}. Number of comments found: {n}")

            for j in range(n):

                comment_dict = {
                    "author": tree_username[j].text_content(),
                    "author_url": BASE_URL + "/" + tree_username_url[j].get("href"),
                    "age": tree_age[j].text_content(),
                    "story_title": tree_onstory[j].text_content()[8:],
                    "story_url": BASE_URL + "/" + tree_onstory_url[j].get("href"),
                    "context": BASE_URL + "/" + tree_context_url[j].get("href"),
                    "comment": tree_commtext[j].text_content(),
                }

                saved_comments.append(comment_dict)
                comments_processed += 1
            
            if n < 30:
                break
        except:
            print(f"Error getting data for page {i}")
            break

        i += 1
        wait_for_page_load(url)

    if comments_processed < 1:
        print(
            "Could not retrieve any of the comments. Check if you actually have any saved comments."
        )
        sys.exit(1)
    else:
        print(f"Processed {comments_processed} comments")

    print(
        "\nEnter the file name in the next line. Use extension '.json' for JSON, or '.csv' for CSV."
    )
    file_name = input("File name (default: comments.json): ")

    if file_name == "":
        file_name = "comments.json"

    if file_name.split(".")[-1].lower() == "json":
        save_json(saved_comments, file_name)
    elif file_name.split(".")[-1].lower() == "csv":
        save_csv(saved_comments, file_name)


if __name__ == "__main__":
    main()
