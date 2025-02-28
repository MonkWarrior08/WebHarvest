import os
import glob

def combine(folder="base", output="combine/combine.txt"):
    txt_file = glob.glob(os.path.join(folder, "*.txt"))

    with open(output, 'w', encoding="utf-8") as outfile:
        for txt in txt_file:
            with open(txt, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
                outfile.write("\n")
if __name__ == "__main__":
    combine()