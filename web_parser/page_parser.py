import json
import re

import requests
from bs4 import BeautifulSoup


class PageParser:
    def __init__(self, url, content_request_tag, content_request_sub_tag, content_request_css_tag, main_tag, sub_tag):
        self.__url = url
        self.__content_request_tag = content_request_tag
        self.__content_request_sub_tag = content_request_sub_tag
        self.__content_request_css_tag = content_request_css_tag
        self.main_tag = main_tag
        self.sub_tag = sub_tag
        self.__page = None
        self.__soup = None
        self.__content = None
        self.__final_content = {}
        self.__parse_page()

    def __parse_page(self):
        try:
            self.__page = requests.get(self.__url)
            self.__soup = BeautifulSoup(self.__page.content, 'html.parser')
            self.__content = self.__soup.find(self.main_tag,
                                              attrs={'id': self.__content_request_css_tag})
            self.__content_body = self.__content.find(self.sub_tag)

            self.__content_data = self.__content_body.find_all(self.__content_request_tag)

            for self.__data in self.__content_data:
                self.__col = self.__data.find_all(self.__content_request_sub_tag)
                for self.__item in self.__col:
                    try:
                        self.__code = str(self.__col[0].text)
                        self.__description = self.__col[1].text.split("Start")[0]
                        self.__all_dates = (self.__col[1].text.split("Start")[1].replace(':', '').strip().split('|'))
                        self.__start_date = self.__all_dates[0]
                        self.__get_modified_date()
                        self.__get_stop_date()
                        self.__result = {
                            "status": self.__get_status(),
                            "description": self.__description,
                            "dates": {
                                "start_date": self.__start_date,
                                "modified_date": self.__modified_date,
                                "stop_date": self.__stop_date
                            },
                        }
                        self.__final_content[self.__code] = self.__result
                    except IndexError:
                        pass
                    break
        except RuntimeWarning as r:
            print(r)

    def __get_modified_date(self):
        if len(self.__all_dates) > 1:
            self.__modified_date = self.__all_dates[1].split(" ")[-1]
        else:
            self.__modified_date = ""

    def __get_stop_date(self):
        if len(self.__all_dates) > 2:
            self.__stop_date = self.__all_dates[2].split(" ")[-1]
        else:
            self.__stop_date = ""

    def __get_status(self):
        if self.__stop_date:
            return "inactive"
        else:
            return "active"

    def get_status_codes(self):
        return self.__final_content