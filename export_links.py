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


def signal_handler(signal, frame):
    print("\nStopping...\n")
    sys.exit(130)


def save_json(saved_links, file_name):
    result = {"total": len(saved_links), "links": saved_links}
    with open(file_name, "w") as f:
        json.dump(result, f)

    print(f"\nLinks saved to: {file_name}")


def save_csv(saved_links, file_name):
    data = [
        (
            link["number"],
            link["title"],
            link["url"],
            link["points"],
            link["comments"],
            link["comments_url"],
            link["author"],
            link["age"],
        )
        for link in saved_links
    ]
    with open(file_name, "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC, delimiter=",")
        writer.writerows(data)

    print(f"\nLinks saved to: {file_name}")


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

    url = f"{BASE_URL}/upvoted?id={username}&p="
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:75.0) Gecko/20100101 Firefox/75.0",
    }

    saved_links = list()
    links_processed = 0
    i = 1

    while True:
        try:
            print("Getting url: ", url + str(i))
            r = session.get(url + str(i), headers=headers)

            tree = html.fromstring(r.text)

            # Part that contains the title and url for the stories
            tree_title = tree.cssselect(".title")

            # Part that contains metadata such as author, no. of comments, etc.
            tree_subtext = tree.cssselect(".subtext")

            # Part that contains score
            tree_score = tree.cssselect(".subtext span.score")

            # Number of links on the page
            n = len(tree_score)

            if n == 0:
                print(f"Processing page {i}. No links found.")
                break

            print(f"Processing page {i}. Number of links found: {n}")

            for j in range(n):
                tree_subtext_each = tree_subtext[j].cssselect("a")
                tree_title_each = tree_title[2 * j + 1].cssselect("a")

                link_dict = {
                    "number": int(tree_title[2 * j].text_content()[:-1]),
                    "title": tree_title_each[0].text_content(),
                    "url": tree_title_each[0].values()[0],
                    "points": int(tree_score[j].text_content().split()[0]),
                    "author": tree_subtext_each[0].text_content(),
                    "age": tree_subtext_each[1].text_content(),
                }

                # Use correct URL for stories without links (e.g., Ask HN, Show HN, etc.)
                if link_dict["url"].startswith("item?"):
                    link_dict["url"] = f"{BASE_URL}/{link_dict['url']}"

                # This is to take care of situations where flag link may not be
                # present in the subtext. So number of links could be either 3
                # or 4.
                num_subtext = len(tree_subtext_each)
                link_dict["comments_url"] = (
                    BASE_URL + "/" + tree_subtext_each[num_subtext - 1].values()[0]
                )

                if (
                    tree_subtext_each[num_subtext - 1].text_content().strip()
                    == "discuss"
                ):
                    link_dict["comments"] = 0
                else:
                    link_dict["comments"] = int(
                        tree_subtext_each[num_subtext - 1].text_content().split()[0]
                    )

                saved_links.append(link_dict)
                links_processed += 1

            if n < 30:
                break
        except:
            print(f"Error getting data for page {i}")
            break

        i += 1

    if links_processed < 1:
        print(
            "Could not retrieve any of the links. Check if you actually have any saved links."
        )
        sys.exit(1)
    else:
        print(f"Processed {links_processed} links")

    print(
        "\nEnter the file name in the next line. Use extension '.json' for JSON, or '.csv' for CSV."
    )
    file_name = input("File name (default: links.json): ")

    if file_name == "":
        file_name = "links.json"

    if file_name.split(".")[-1].lower() == "json":
        save_json(saved_links, file_name)
    elif file_name.split(".")[-1].lower() == "csv":
        save_csv(saved_links, file_name)


if __name__ == "__main__":
    main()
