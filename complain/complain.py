"""
MIT License

Copyright (c) 2022 Ben

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
"""

import datetime
import requests
from complaint import Complain


class Complain:
    """
    Base class for requesting complaints

    Attributes
    ----------
    None

    Methods
    -------
    generate: str
        Returns a new complaint
    """

    def __init__(self) -> None:
        """
        Base options


        """
        pass

    def _request(self) -> None:
        """
        Base request
        """
        cookie = {
            "ACLG_agreed": datetime.datetime.strftime("%a, %d %b %Y %H:%M:%S GMT")
        }
        data = requests.get(
            url="",
            cookies=cookie
        )

    def generate(self) -> Complain:
        """
        Generate a complaint based on given options
        """