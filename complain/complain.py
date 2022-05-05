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
from complaint import Complaint


class ComplainClient:
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
        Init

        Parameters
        ----------
        None

        Attributes
        ----------
        base_url: str
            The base_url used for all requests
        cookie: dict
            The cookie used to automatically accept terms

        Returns
        -------
        None
        """
        self.base_url = "https://www.pakin.org/complaint"
        self.cookie = {
            "ACLG_agreed": datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")
        }

    def _format_url(self, params: dict) -> str:
        """
        Method to reformat params into a url

        Parameters
        ----------
        params: dict
            The parameters needed to be reformatted

        Returns
        -------
        str
        """
        param_len = len(params)
        if param_len == 1:
            url_link = f"?{params.keys()[0]}={params[params.keys()[0]]}"
        elif param_len >= 2:
            url_link = f"?{params.keys()[0]}={params[params.keys()[0]]}"
            value = 0
            for param in params.keys():
                if value == 0:
                    value = 1
                else:
                    url_link = url_link + f"&{param}={params[param]}"
        return url_link

    def _format_data(self, data: str, html: bool=False) -> str:
        """
        Parsing the data into a regular string from html

        Parameters
        ----------
        data: str
            The html that needs to be parsed
        html: bool = False
            If you want raw html, default False
        """
        data = data.split("</h1>")[1].split("</body>")[0]
        if not html:
            data = (
                data.replace("&rsquo;", "'")
                .replace('<i lang="la">', "")
                .replace("</i>", "")
                .replace("<q>", '"')
                .replace("</q>", '"')
                .replace("<p>", "")
                .replace("</p>", "")
            )
        return data

    def _request(self, url: str) -> requests.Response:
        """
        The request function used to request data

        This is not meant to be used by users

        Parameters
        ----------
        url: str
            The url to request

        Returns
        -------
        requests.Response
        """
        data = requests.get(url=url, cookies=self.cookie)
        return data

    def generate(self) -> Complaint:
        """
        Generate a complaint based on given options
        """
        data = self._request()

        return Complaint(
            
        )

