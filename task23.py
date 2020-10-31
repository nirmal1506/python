import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("filename", nargs="?", default="file", help="Enter filename")
parser.add_argument("--folder", nargs="?", default="current", help="Enter folder")
args = parser.parse_args()

def count_words(s):
    word_list = s.split()
    print("no. of words:- ", len(word_list))


def count_chars(st, space):
    count = 0
    if space == 0:
        count = len(st) - st.count("\n")
        print("Characters including space:- ", count)
    else:
        count = len(st) - st.count(" ") - st.count("\n")
        print("Characters without space", count)


if __name__ == '__main__':
    if args.folder == "current":
        f = open(args.filename+".txt", 'w+')
    else:
        dirs = os.listdir("c:/")
        print(dirs)
        if args.folder in dirs:
            os.chdir("c:/"+args.folder)
            f = open(args.filename+".txt", 'w+')
        else:
            os.mkdir("c:/"+args.folder)
            os.chdir("c:/" + args.folder)
            f = open(args.filename+".txt", 'w+')
    lines = int(input("Enter number of lines:- "))
    for i in range(lines):
        data = input("Enter data:- ")
        f.write(data + '\n')
    f.seek(0)
    x = f.read()
    print("lines = ", lines)
    count_words(x)
    count_chars(x, 0)
    count_chars(x, 1)
    f.close()