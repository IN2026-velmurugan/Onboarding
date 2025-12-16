"""Module contains the function to scrap the website for link and it's text."""

from typing import Dict

import requests
from bs4 import BeautifulSoup


def extract_link(url: str) -> Dict[str, str]:
    """Scraps the link and text from the given URL.

    Args:
        url: URL to be scrapped.

    Returns:
        Text mapped to the link as dictionary.
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    a_tag_comp = [tag for tag in soup.find_all("a")]
    filtered = [
        tag
        for tag in a_tag_comp
        if tag.get("href")
        and isinstance(tag.get("href"), str)
        and not tag.get("href").startswith("/wiki/")  # type: ignore
    ]

    filtered_string = [tag.string for tag in filtered]
    filtered_link = [tag["href"] for tag in filtered]
    link_map: Dict[str, str] = {
        str(filtered_string[i]): str(filtered_link[i])
        for i in range(len(filtered_link))
        if filtered_string[i]
    }

    return link_map


if __name__ == "__main__":
    url = input("Enter the URL to scrap the link : ").replace('"', "")
    link_map: Dict[str, str] = extract_link(url)
    for k in link_map:
        print(f"Text : {k} & Link : {link_map.get(k)}")
