import numpy as np

EPS = 1e-2

def obb_corners(pos, rot, half):
    hx, hy = half
    local = np.array([
        [-hx, -hy],
        [ hx, -hy],
        [ hx,  hy],
        [-hx,  hy],
    ], dtype=float)
    return pos + local @ rot.T

def project_radius(rot, half, axis):

    return (
        half[0] * abs(np.dot(axis, rot[:, 0])) +
        half[1] * abs(np.dot(axis, rot[:, 1]))
    )

def support_point(pos, rot, half, direction):
    x_axis = rot[:, 0]
    y_axis = rot[:, 1]

    p = pos.copy()
    p += x_axis * (half[0] if np.dot(direction, x_axis) >= 0 else -half[0])
    p += y_axis * (half[1] if np.dot(direction, y_axis) >= 0 else -half[1])
    return p

def obb_collision(posA, rotA, halfA, posB, rotB, halfB):
    axes = [
        rotA[:, 0], rotA[:, 1],
        rotB[:, 0], rotB[:, 1]
    ]

    delta = posB - posA
    min_overlap = np.inf
    best_axis = None
    best_from_A = True

    for i, axis in enumerate(axes):
        axis = axis / np.linalg.norm(axis)

        ra = project_radius(rotA, halfA, axis)
        rb = project_radius(rotB, halfB, axis)
        dist = abs(np.dot(delta, axis))
        overlap = ra + rb - dist

        if overlap < 0:
            return False, 0, np.zeros(3), np.zeros(3)

        if overlap < min_overlap:
            min_overlap = overlap
            best_axis = axis
            best_from_A = (i < 2)

    if best_axis is None:
        return False, 0, np.zeros(3), np.zeros(3)
    
    normal = best_axis.copy()
    if np.dot(delta, normal) < 0:
        normal = -normal

    if best_from_A:
        ref_pos, ref_rot, ref_half = posA, rotA, halfA
        inc_pos, inc_rot, inc_half = posB, rotB, halfB
        ref_face_normal = normal
    else:
        ref_pos, ref_rot, ref_half = posB, rotB, halfB
        inc_pos, inc_rot, inc_half = posA, rotA, halfA
        ref_face_normal = -normal

    ax = ref_rot[:, 0]
    ay = ref_rot[:, 1]

    if abs(np.dot(ref_face_normal, ax)) > abs(np.dot(ref_face_normal, ay)):
        face_axis = ax
        face_half = ref_half[0]
        tangent_axis = ay
        tangent_half = ref_half[1]
        sign = 1.0 if np.dot(ref_face_normal, ax) > 0 else -1.0
    else:
        face_axis = ay
        face_half = ref_half[1]
        tangent_axis = ax
        tangent_half = ref_half[0]
        sign = 1.0 if np.dot(ref_face_normal, ay) > 0 else -1.0

    face_center = ref_pos + face_axis * (sign * face_half)

    c = np.dot(face_center, ref_face_normal)

    incident_pts = obb_corners(inc_pos, inc_rot, inc_half)
    hits = []

    def add_hit(p):
        s = np.dot(p - face_center, tangent_axis)
        if s < -tangent_half - 1e-7 or s > tangent_half + 1e-7:
            return
        for q in hits:
            if np.linalg.norm(p - q) < 1e-6:
                return
        hits.append(p)

    for i in range(4):
        a = incident_pts[i]
        b = incident_pts[(i + 1) % 4]

        da = np.dot(a, ref_face_normal) - c
        db = np.dot(b, ref_face_normal) - c

        if abs(da) < 1e-7:
            add_hit(a)
        if abs(db) < 1e-7:
            add_hit(b)

        if da * db < 0:
            t = da / (da - db)
            p = a + t * (b - a)
            add_hit(p)

    if len(hits) == 0:
        pa = support_point(posA, rotA, halfA, normal)
        pb = support_point(posB, rotB, halfB, -normal)
        contact_point = 0.5 * (pa + pb)
    else:
        contact_point = np.mean(hits, axis=0)

    return True, float(min_overlap), normal, contact_point