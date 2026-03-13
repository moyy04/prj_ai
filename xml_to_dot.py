import xml.etree.ElementTree as ET
import sys

def xml_to_dot(input_file, output_file):
    tree = ET.parse(input_file)
    root = tree.getroot()

    # On récupère les lignes <data> dans valmatrix id="transitions"
    valmatrix = root.find(".//valmatrix[@id='transitions']")
    rows = [row.text.strip() for row in valmatrix.findall("data")]

    with open(output_file, 'w') as f:
        f.write("digraph G {\n")
        for i, row in enumerate(rows):
            values = row.split()
            for j, val in enumerate(values):
                if val == "1":
                    f.write(f'  "{i}" -> "{j}";\n')
        f.write("}\n")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python xml_to_dot.py input.xml output.dot")
    else:
        xml_to_dot(sys.argv[1], sys.argv[2])
