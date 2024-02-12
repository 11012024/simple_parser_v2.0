import json

# Created: Thursday, August 18, 2022, 6:38:48 PM


class WithJsonWorker:

    def __init__(self, file_name):
        self.__file_name = file_name
        self.__info = self.__get_info_from_file()

    @property
    def exchange_info(self) -> dict:
        return self.__info

    def __get_info_from_file(self) -> dict:
        try:
            with open(self.__file_name) as json_file:
                xpaths = json.load(json_file)
            return xpaths
        except Exception as exception:
            print(exception)
            return {}

    def dump_to_the_file(self, key, **args):
        self.__info[key] = {}
        for name, value in args.items():
            self.__info[key][name] = value
        with open(self.__file_name, 'w') as json_file:
            json.dump(self.__info, json_file)
