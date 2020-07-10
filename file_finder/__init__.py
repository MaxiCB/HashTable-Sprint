def finder(files, queries):
    result = []
    box = {}

    for f in files:
        split = f.split("/")
        name = split[-1]

        if name not in box:
            box[name] = []

        box[name].append(f)

    for q in queries:
        if q in box:
            result.extend(box[q])

    return result


# if __name__ == "__main__":
#     files = [
#         '/bin/foo',
#         '/bin/bar',
#         '/usr/bin/baz'
#     ]
#     queries = [
#         "foo",
#         "qux",
#         "baz"
#     ]
#     print(finder(files, queries))
