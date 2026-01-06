"""Function to scrap the website for link and it's text."""

from typing import Iterator

import requests
from bs4 import BeautifulSoup, Tag


def is_valid_link(tag: Tag) -> bool:
    """Verify whether the link doesn't start with wiki.

    Args:
        tag: a tag with attributes.

    Returns:
        True if the link exists and doesn't start with wiki.
    """
    href = tag.get("href")
    return (
        isinstance(href, str) and not href.startswith("/wiki/") and bool(tag.get_text(strip=True))
    )


def extract_link(url: str) -> dict[str, str]:
    """Scrap the link and text from the given URL.

    Args:
        url: URL to be scrapped.

    Returns:
        Text mapped to the link as dictionary.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        valid_links: Iterator[Tag] = filter(
            is_valid_link,
            soup.find_all("a"),
        )

        content: dict[str, str] = dict(
            map(
                lambda tag: (
                    tag.get_text(strip=True),
                    str(tag["href"]),
                ),
                valid_links,
            )
        )
    except requests.exceptions.HTTPError as e:
        raise RuntimeError("Error occurred at client/server") from e
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Network error while fetching {url}") from e
    except KeyError as e:
        raise RuntimeError("Anchor tag missing href attribute") from e
    else:
        return content


def main():
    """Start the script."""
    count = 0
    while count < 5:
        try:
            url = input("Enter the URL to scrap the link : ").replace('"', "")
            if not url:
                raise ValueError("Cannot scrap the empty URL!!!")
            link_map: dict[str, str] = extract_link(url)
            for k in link_map:
                print(f"Text : {k} & Link : {link_map.get(k)}")
            return
        except ValueError as e:
            print(f"Application error : {e}")
        except RuntimeError as e:
            print(f"Error while scrapping the site : {e}")
        count += 1


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program inputted shutting down the application.")
