def load_data_section(lines):
    '''iterate over lines, storing lines as ints until we reach /eof'''
    num_list = []
    for line in lines:
        if '/eof' not in line:
            clean_line = line.strip()
            num_list.append(float(clean_line))
        else:
            break

    return num_list


def stu_to_dict(fname):
    with open(fname) as shoesf:
        sections = {}

        for line in shoesf:
            if 'LOAD DATA' in line:
                _, key = line.rsplit(' ', 1)
                key, _ = key.split(';')

                sections[key] = load_data_section(shoesf)

    return sections


def print_sections(sections):
    '''Print a dictionary of lists as a CSV'''
    colnames = sections.keys()
    print(','.join(colnames))

    # We could do this...
    # section_list = [sections[k] for k in colnames]

    # Which is the same as this:
    section_list = []
    for k in colnames:
        section_list.append(sections[k])

    for data in zip(*section_list):
        # Again, could do:
        # print(','.join(str(d) for d in data))

        # Which is the same as:
        str_vals = []
        for d in data:
            str_vals.append(str(d))

        print(','.join(str_vals))


if __name__ == '__main__':
    shoe_sections = stu_to_dict('data/shoes.stu')
    print_sections(shoe_sections)
