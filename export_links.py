import json
import requests
from lxml import html

BASE_URL = "https://news.ycombinator.com/"


def save_json(saved_links, file_name):
    result = {
        "total": len(saved_links),
        "links": saved_links
    }
    with open(file_name, 'w') as f:
        json.dump(result, f)

    print "Links saved to: {}".format(file_name)


def save_csv(saved_links, file_name):
    pass


def main():
    username = raw_input("HN username: ")
    cookie = raw_input("HN cookie: ")
    num_of_pages = int(raw_input("Number of pages: "))

    url = "{}saved?id={}&p=".format(BASE_URL, username)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0",
        "Cookie": cookie
    }

    saved_links = list()
    links_processed = 0

    for i in range(1, num_of_pages + 1):
        try:
            r = requests.get(url + str(i), headers=headers)

            tree = html.fromstring(r.text)

            # Part that contains the title and url for the stories
            tree_title = tree.cssselect(".title a")

            # Part that contains metadata such as author, no. of comments, etc.
            tree_subtext = tree.cssselect(".subtext")

            # Part that contains score
            tree_score = tree.cssselect(".subtext span.score")

            # Number of links on the page
            n = len(tree_score)

            print "Page {}. Number of links: {}".format(i, n)

            for j in range(n):
                tree_subtext_each = tree_subtext[j].cssselect("a")

                link_dict = {
                    "title": tree_title[j * 2].text_content(),
                    "url": tree_title[j * 2].values()[0],
                    "points": int(tree_score[j].text_content().split()[0]),
                    "author": tree_subtext_each[0].text_content(),
                    "age": tree_subtext_each[1].text_content(),
                }

                # This is to take care of situations where flag link may not be
                # present in the subtext. So number of links could be either 3
                # or 4.
                num_subtext = len(tree_subtext_each)
                link_dict["comments_url"] = BASE_URL + \
                    tree_subtext_each[num_subtext - 1].values()[0]

                if tree_subtext_each[num_subtext - 1].text_content().strip() == "discuss":
                    link_dict["comments"] = 0
                else:
                    link_dict["comments"] = int(
                        tree_subtext_each[num_subtext - 1].text_content().split()[0])

                saved_links.append(link_dict)
                links_processed += 1

        except:
            print "Error getting data for page {}".format(i)

    print "Processed {} links".format(links_processed)

    print "Enter the file name in the next line. Use extension '.json' for JSON, or '.csv' for CSV."
    file_name = raw_input("File name (default: links.json): ")

    if file_name == "":
        file_name = "links.json"

    if file_name.split(".")[-1].lower() == "json":
        save_json(saved_links, file_name)
    elif file_name.split(".")[-1].lower() == "csv":
        save_csv(saved_links, file_name)

if __name__ == '__main__':
    main()
