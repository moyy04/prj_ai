import sys
import re

def dot_to_xml(input_file, output_file):
    edges = []
    nodes = set()
    pattern = re.compile(r'"([^"]+)"\s*->\s*"([^"]+)"')

    with open(input_file, 'r') as f:
        for line in f:
            m = pattern.search(line)
            if m:
                from_node, to_node = m.group(1), m.group(2)
                edges.append((from_node, to_node))
                nodes.add(from_node)
                nodes.add(to_node)

    nodes = sorted(nodes)
    index = {node: i for i, node in enumerate(nodes)}
    size = len(nodes)

    matrix = [[0]*size for _ in range(size)]
    for f, t in edges:
        matrix[index[f]][index[t]] = 1

    with open(output_file, 'w') as f:
        f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
        f.write('<instance format="Talos">\n')
        f.write('  <values>\n')
        f.write('    <valmatrix id="transitions">\n')
        for row in matrix:
            f.write('      <data>' + ' '.join(map(str, row)) + '</data>\n')
        f.write('    </valmatrix>\n')
        f.write('  </values>\n')
        f.write('</instance>\n')

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python dot_to_xml.py input.dot output.xml")
    else:
        dot_to_xml(sys.argv[1], sys.argv[2])
