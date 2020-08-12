#Cristopher jose Rodolfo Barrios Solis
#SR4
class Obj(object):
    def __init__(self, filename):
        with open(filename) as f:
            self.lines = f.read().splitlines()

        self.vertices = []
        self.faces = []
        self.text_coords = []
        self.normals = []
        self.read()

    def read(self):
        for line in self.lines:
            if line:
                prefix, value = line.split(' ', 1)
                
                if prefix == 'v':
                    self.vertices.append(list(map(float, value.split(' '))))
                elif prefix == "vn":
                    self.normals.append(list(map(float, value.split(" "))))
                elif prefix == "vt":
                    self.text_coords.append(list(map(float, value.split(" "))))
                elif prefix == 'f':
                    self.faces.append ([ list(map(int , face.split('/'))) for face in value.split(' ') ])
                        