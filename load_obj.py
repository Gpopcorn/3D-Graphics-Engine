def load_obj(file):
    try:
        content = open(file, 'r').read()
    except TypeError:
        print("An error has occured.")
        exit()
    content_lines = content.split('\n')
    verticies = []
    faces = []

    for line in content_lines:
        if line.startswith('f '):
            line = line.split(' ')
            line.pop(0)
            line_list = []
            for index, face in enumerate(line):
                if face == '':
                    line.remove(face)
                else:
                    face = face.replace('//', '/')
                    line[index] = list(map(int, face.split('/')))[0] - 1
                    line_list.append(line[index])

            faces.append(line_list)

        elif line.startswith('v '):
            line = line.replace('  ', ' ')
            line = line.split(' ')
            line.pop(0)
            line = list(map(float, line))
            for index, item in enumerate(line):
                line[index] = [item]
            verticies.append(line)

    return (verticies, faces)