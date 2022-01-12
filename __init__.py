"""Opens a new tab on the browser with the selected AWS service."""

from albert import Item, UrlAction, Query
import os
from urllib.parse import urlencode
from typing import Dict, List

__authors__ = "<Dave Gallant> davegallant@gmail.com"
__dependencies__ = []
__icon_path__ = os.path.dirname(__file__) + "/logo.svg"
__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Aws Caller"
__title__ = "awscaller"
__triggers__ = "aws"
__version__ = "0.3.0"


SERVICE_ALIASES = {
    "cw": "cloudwatch",
    "eb": "elasticbeanstalk",
}


def get_service_name(query: str, service_aliases: Dict) -> str:
    """The service name must always be the first word in the query string."""
    if not query:
        return ""
    service = query.split()[0]
    if service in service_aliases:
        return service_aliases[service]
    return service


def get_encoded_params(query: Query) -> str:
    """Any extra params in the query are parsed (e.g. region:us-west-2)."""
    query_items = query.split()
    params = {}
    encoded_params = ""

    for item in query_items:
        if ":" not in item:
            continue
        key, value = item.split(":")
        if not (key and value):
            continue
        params[key] = value

    if params:
        encoded_params = "?" + urlencode(params)

    return encoded_params


def handle_query(query: Query) -> List[Item]:
    """Handle the query and return a list of results."""
    if not query.isTriggered:
        return []

    service_name = get_service_name(query.string.strip(), SERVICE_ALIASES)
    encoded_params = get_encoded_params(query.string.strip())
    aws_console_url = (
        "https://console.aws.amazon.com/" + service_name + "/home" + encoded_params
    )
    return [
        Item(
            id=__prettyname__,
            icon=__icon_path__,
            completion=query.rawString,
            text="AWS",
            subtext="Opens an AWS service console page for the given name",
            actions=[UrlAction(text="Open", url=aws_console_url)],
        )
    ]


def handleQuery(query: Query) -> List[Item]:
    """Pass to the renamed function."""
    return handle_query(query)
