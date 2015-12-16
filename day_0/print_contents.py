__author__ = 'Dav-Z'

import glob

# print(lyrics_file.read())
def clean_lyrics_file(lyrics_file, clean_file):
    clean_lines = []

    # Process file and clean it up
    for line in lyrics_file:
        line = line.casefold()
        # Extra Extra credit: get rid of punctuation
        # Another way to get rid of the chorus junk
        # line = line.rstrip("[chorus]")
        line = line.rstrip()
        for junk_character in [",", "'", "?", "!", "."]:
            line = line.replace(junk_character, "")

        found_junk_line = False
        for junk_line in ["[chorus]", "[chorus:]"]:
            if junk_line in line:
                found_junk_line = True

        # if "[chorus" not in line:
        if not found_junk_line:
            if line:
                clean_file.write(line + '\n')
                clean_lines.append(line)

    return clean_lines


all_lyrics = []
# Loop over each file, one at a time
all_files = glob.glob("JayZ/*.txt")
print("Looping over", len(all_files), "files")
for infile in all_files:

    # stuff below goes here!
    lyricsf = open(infile)
    cleanf = open(infile + '.clean', 'w')

    curr_clean_lines = clean_lyrics_file(lyricsf, cleanf)
    all_lyrics.append(curr_clean_lines)

    lyricsf.close()
    cleanf.close()

# if all_lyrics:
#    print("list is not empty!")
print("Got", len(all_lyrics), "processed lyrics")

# from all_lyrics, compute line_counts that are strings

line_counts = []
lines_seen = 0
for lyrics in all_lyrics:
    num_lines = len(lyrics)
    line_counts.append(num_lines)
    lines_seen = lines_seen + num_lines

print("here are counts:", line_counts)
print("Lines seen:", lines_seen)
print("Direct sum:", sum(line_counts))



counts_as_strings = [str(count) for count in line_counts]
print("Counts as strings:", counts_as_strings)

# TODO Create a dictionary from counts_as_strings for a stem-and-leaf plot, e.g.:
# {'7': ['71', ...], '5': ['52', ...], ...}

# countstr = '39'
# prefix = countstr[:-1]
# d = {}
# '3' in d
# if '3' not in d:
#     d['3'] = []
# d['3'].append(countstr)

stem_leaf_data = {}
for countstr in counts_as_strings:
    prefix = countstr[:-1]
    if prefix not in stem_leaf_data:
        stem_leaf_data[prefix] = []

    stem_leaf_data[prefix].append(countstr[-1])

print(stem_leaf_data)

# We convert to ints again to get order, and back to strings to get 0-padding
for k in sorted(int(val) for val in stem_leaf_data):
    if k < 10:
        to_print = '0' + str(k)
    else:
        to_print = str(k)
    print(to_print, "|", ' '.join(stem_leaf_data[str(k)]))

# Bonus challenge: also compute word count, character count
# Number of occurrences of "a" and "the"



print("We're done!")

