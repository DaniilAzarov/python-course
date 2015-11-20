with open('/home/daniil/python-course/lectures/enzyme_small.txt', 'r') as f:
    text = f.read()

descriptions = text.split("///\n")



for descriptions in descriptions:
    lines = descriptions.split("\n")
    header = lines[0]
    trash = header.split(" ")
    clean = [line for line in trash if line]

    enzimes_id = clean[2]
    for i, line in enumerate(lines):
        if line.startswith("GENES"):
            for j, line_end in enumerate(lines[i + 1:]):
                if not line_end.startswith(" "):
                    break
            print(i, j)




