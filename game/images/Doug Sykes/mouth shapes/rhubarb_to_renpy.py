import os

def pngs_with_highest_first_word_count():
    filenames = [f for f in os.listdir() if f.endswith(".png")]

    count = {} # used to store the words and their counts
    for f in filenames:
        first_word = f.split(" ")[0]
        if not first_word in count:
            count[first_word] = 1
        else:
            count[first_word] += 1

    biggest_count = 0
    for word in count:
        if count[word] > biggest_count:
            biggest_count = count[word]
            biggest_word = word

    return [f for f in filenames if f.startswith(biggest_word)]


def confirm_unique_letters_in_mouth_shapes():
    filenames = pngs_with_highest_first_word_count()

    mouth_shapes = set([filename.split(" ")[-1].split(".png")[0] for filename in filenames])

    print(filenames)
    print(mouth_shapes)

    multiple_letter_mouth_shapes = sorted([mouth_shape for mouth_shape in mouth_shapes if len(mouth_shape) > 1])
    single_letter_mouth_shapes = sorted([mouth_shape for mouth_shape in mouth_shapes if len(mouth_shape) == 1])
    print(multiple_letter_mouth_shapes)
    found_letters = set()
    for mouth_shape in mouth_shapes:
        for letter in mouth_shape:
            if letter in found_letters:
                raise Exception("rename your .png files so that there are no repeats in your mouthshapes, like (AB, BA)" + "\nconflicting shape: " + mouth_shape)
            found_letters.add(letter)

confirm_unique_letters_in_mouth_shapes()

# if it gets past this point, then you can use the names of the files to figure out the conversion from mouth letter shape to filename
letter_to_png = {}
filenames = pngs_with_highest_first_word_count()
for letter in "XABCDEFGH":
    for filename in filenames:
        if letter in filename.split(".png")[0].split(" ")[-1]:
            letter_to_png[letter] = filename
            break
print(letter_to_png)

with open("blockbuster_mouth_shapes.txt", "r") as f:
    rhubarb_mouth_shapes = f.read().strip().split("\n")

output_folder_name = "doug_talking_animation.rpy"

directory = "Doug Sykes/mouth shapes/"

with open(output_folder_name, "w") as f:
    f.write("image doug animation:\n")

    for i, event in enumerate(rhubarb_mouth_shapes[:-1]):
        # print(event)
        event = event.split("\t")
        timestamp = float(event[0])
        next_timestamp = float(rhubarb_mouth_shapes[i + 1].split('\t')[0])
        shape = event[1].upper()
        time_difference = round(next_timestamp - timestamp, 2)
        f.write(f"{' ' * 4}\"{directory}{letter_to_png[shape]}\"\n{' ' * 4}{time_difference}\n")

    f.write(" " * 4 + "\"" + directory + letter_to_png[rhubarb_mouth_shapes[-1].split("\t")[1].upper()] + "\"")

# print(rhubarb_mouth_shapes)