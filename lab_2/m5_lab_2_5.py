def to_json(info={"check": 142, "check2": [125, "waiting for a good mark"], "check3": None,
                  "check4": {"a": 666}, "check5": True, "check6": "hahaxd"}):
    if info is None:
        return "null"

    if type(info) == str:
        return '"{}"'.format(info)  # adding "" to string object

    if type(info) == int or type(info) == float:
        return "{}".format(info)

    if type(info) == list or type(info) == tuple:
        result = ''
        for i in info:
            result += to_json(i) + ", "
        return "[" + result[:-3] + result[(-1):] + "]"

    if type(info) == bool:
        return "{}".format(info)

    if type(info) == dict:
        result = ""
        for key, file in info.items():
            if type(key) not in (str, int):
                raise ValueError
            result += '  "{}": {}, \n'.format(key, to_json(file))
        return "{" + "\n" + result[:-3] + "\n""}"


def to_json_by_file(file = "to_json.txt", info = {"check": 142, "check2": [125, "waiting for a good mark"],
                                                  "check3": None, "check4": {"a": 666},
                                                  "check5": True, "check6": "hahaxd"}):
    with open(file, "w") as f:
        f.write(to_json(info))
    return "Information successfully written in the file"


if __name__ == "__main__":
    print(to_json_by_file())
