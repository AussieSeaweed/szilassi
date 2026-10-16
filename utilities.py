from ast import literal_eval
from collections import defaultdict


def parse(raw_manifolds):
    for raw_manifold in raw_manifolds.split('\n\n'):
        index = raw_manifold.index('=')

        yield raw_manifold[:index], literal_eval(raw_manifold[index + 1:])


def dual(faces):
    dual_edges = defaultdict(set)
    dual_vertices = defaultdict(set)

    for f, face in enumerate(faces):
        f += 1
        i = 0

        while i < len(face):
            u = face[i]
            v = face[(i + 1) % len(face)]
            i += 1

            if u > v:
                u, v = v, u

            dual_edges[u, v].add(f)

        for v in face:
            dual_vertices[v].add(f)

    neighboring_faces = defaultdict(set)

    for f, g in dual_edges.values():
        neighboring_faces[f].add(g)
        neighboring_faces[g].add(f)

    dual_faces = []

    for vertices in dual_vertices.values():
        dual_face = []

        while vertices:
            if dual_face:
                v = min(vertices & neighboring_faces[dual_face[-1]])
            else:
                v = min(vertices)

            dual_face.append(v)
            vertices.remove(v)

        dual_faces.append(dual_face)

    dual_faces.sort()

    return dual_faces
