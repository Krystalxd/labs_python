import argparse


def flatten_it(iterable_object=[1, 2, 3, ["haha", [3], 7], (9)]):
    try:
        for x in iterable_object:
            if x == iterable_object:
                raise ValueError
            if hasattr(x, '__iter__') and not isinstance(x, str):  # If your element is one number
                # or a string object, then we leave it
                yield from flatten_it(x)  # Recursion for list objects
            else:
                yield x
    except RecursionError:
        raise ValueError
    except ValueError:
        print("ValueError: unavailable to flatten self-referenced lists")


def flatten_it_by_args():
    parser = argparse.ArgumentParser(description="Object flattening")  # Creating of parser to use with command line
    parser.add_argument("-iterable_object", "--iterable_object", action='append',
                        default=[1, 2, 3, ["haha", [3], 7], (9)], help="Flattening object")
    args = parser.parse_args()
    print(list(flatten_it(args.iterable_object))[:-1])


if __name__ == "__main__": 
    flatten_it_by_args()
