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

from typing import Optional


class Complaint:
    """
    Base template for all complaints

    Attributes
    ----------
    None
    """

    def __init__(
        self,
        title: Optional[str],
        first: str,
        middle: Optional[str],
        last: Optional[str],
        suffix: Optional[str],
        gender: Optional[str],
    ) -> None:
        """
        Base object for complaints

        Attributes
        ----------
        title: Optional[str]

        """
        pass
