import math
from pathlib import Path

OUT = Path("iphone_stand_output")
OUT.mkdir(exist_ok=True)


def vadd(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def vsub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def vmul(a, s):
    return (a[0] * s, a[1] * s, a[2] * s)


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def norm(a):
    length = math.sqrt(dot(a, a))
    return (a[0] / length, a[1] / length, a[2] / length)


def oriented_box(name, center, axes, half):
    ux, uy, uz = axes
    hx, hy, hz = half
    corners = []
    for sx, sy, sz in [
        (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
        (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1),
    ]:
        p = center
        p = vadd(p, vmul(ux, sx * hx))
        p = vadd(p, vmul(uy, sy * hy))
        p = vadd(p, vmul(uz, sz * hz))
        corners.append(p)
    faces = [
        (0, 3, 2, 1), (4, 5, 6, 7), (0, 1, 5, 4),
        (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7),
    ]
    return {"name": name, "vertices": corners, "faces": faces}


def axis_box(name, xmin, xmax, ymin, ymax, zmin, zmax):
    return oriented_box(
        name,
        ((xmin + xmax) / 2, (ymin + ymax) / 2, (zmin + zmax) / 2),
        ((1, 0, 0), (0, 1, 0), (0, 0, 1)),
        ((xmax - xmin) / 2, (ymax - ymin) / 2, (zmax - zmin) / 2),
    )


parts = []

# Millimeters. The stand is sized for an iPhone in horizontal StandBy mode.
parts.append(axis_box("left_base_rail", 0, 90, -85, -20, 0, 9))
parts.append(axis_box("right_base_rail", 0, 90, 20, 85, 0, 9))
parts.append(axis_box("rear_crossbar", 38, 90, -85, 85, 0, 12))
parts.append(axis_box("front_lip_left", 8, 20, -85, -18, 8, 24))
parts.append(axis_box("front_lip_right", 8, 20, 18, 85, 8, 24))
parts.append(axis_box("phone_shelf_left", 20, 46, -85, -20, 9, 15))
parts.append(axis_box("phone_shelf_right", 20, 46, 20, 85, 9, 15))

angle = math.radians(68)
u = norm((math.cos(angle), 0, math.sin(angle)))
n = norm((-math.sin(angle), 0, math.cos(angle)))
start = (36, 0, 11)
length = 58
thickness = 9
center = vadd(vadd(start, vmul(u, length / 2)), vmul(n, thickness / 2))
parts.append(oriented_box("angled_backrest", center, (u, (0, 1, 0), n), (length / 2, 85, thickness / 2)))


def triangulate(face):
    return [(face[0], face[1], face[2]), (face[0], face[2], face[3])]


def write_stl(path):
    lines = ["solid iphone_standby_dock"]
    for part in parts:
        vs = part["vertices"]
        for face in part["faces"]:
            for tri in triangulate(face):
                a, b, c = [vs[i] for i in tri]
                normal = norm(cross(vsub(b, a), vsub(c, a)))
                lines.append(f"  facet normal {normal[0]:.6f} {normal[1]:.6f} {normal[2]:.6f}")
                lines.append("    outer loop")
                for p in (a, b, c):
                    lines.append(f"      vertex {p[0]:.6f} {p[1]:.6f} {p[2]:.6f}")
                lines.append("    endloop")
                lines.append("  endfacet")
    lines.append("endsolid iphone_standby_dock")
    Path(path).write_text("\n".join(lines), encoding="utf-8")


def write_obj(path):
    lines = []
    offset = 1
    for part in parts:
        lines.append(f"o {part['name']}")
        for v in part["vertices"]:
            lines.append(f"v {v[0]:.6f} {v[1]:.6f} {v[2]:.6f}")
        for face in part["faces"]:
            ids = [i + offset for i in face]
            lines.append("f " + " ".join(str(i) for i in ids))
        offset += len(part["vertices"])
    Path(path).write_text("\n".join(lines), encoding="utf-8")


def project(p, view):
    eye, right, up = view
    return (dot(p, right), dot(p, up), dot(p, eye))


views = {
    "front": ((-1, 0, 0), (0, 1, 0), (0, 0, 1), "正面"),
    "back": ((1, 0, 0), (0, -1, 0), (0, 0, 1), "背面"),
    "side": ((0, 1, 0), (1, 0, 0), (0, 0, 1), "侧面"),
    "iso": (norm((-1.2, 1.4, 0.9)), norm((1, 0.85, 0)), (0, 0, 1), "斜视"),
}


def draw_svg(path, view_key):
    eye, right, up, title = views[view_key]
    right = norm(right)
    up = norm(up)
    projected_faces = []
    for part in parts:
        for face in part["faces"]:
            poly3 = [part["vertices"][i] for i in face]
            poly2 = [project(p, (eye, right, up)) for p in poly3]
            depth = sum(p[2] for p in poly2) / len(poly2)
            normal = norm(cross(vsub(poly3[1], poly3[0]), vsub(poly3[2], poly3[0])))
            light = max(0.35, dot(normal, norm((-0.5, -0.8, 1.6))))
            shade = int(185 + 50 * light)
            projected_faces.append((depth, [(p[0], p[1]) for p in poly2], shade))
    all_points = [pt for _, poly, _ in projected_faces for pt in poly]
    minx, maxx = min(x for x, _ in all_points), max(x for x, _ in all_points)
    miny, maxy = min(y for _, y in all_points), max(y for _, y in all_points)
    w, h = 1200, 820
    margin = 90
    scale = min((w - 2 * margin) / (maxx - minx), (h - 2 * margin) / (maxy - miny))

    def screen(pt):
        x, y = pt
        return (margin + (x - minx) * scale, h - margin - (y - miny) * scale)

    projected_faces.sort(key=lambda x: x[0], reverse=True)
    body = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        '<rect width="100%" height="100%" fill="#f7f7f4"/>',
        f'<text x="56" y="72" font-family="Arial, sans-serif" font-size="42" font-weight="700" fill="#202124">{title}视图</text>',
        '<text x="56" y="112" font-family="Arial, sans-serif" font-size="22" fill="#5f6368">iPhone 横屏待机底座 / 3D 打印单件式结构</text>',
    ]
    for _, poly, shade in projected_faces:
        pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in map(screen, poly))
        body.append(f'<polygon points="{pts}" fill="rgb({shade},{shade},{shade - 8})" stroke="#4b4d4f" stroke-width="2" stroke-linejoin="round"/>')

    # Phone silhouette for scale in visible views.
    if view_key in {"front", "side", "iso"}:
        body.append('<g opacity="0.42">')
        if view_key == "front":
            x1, y1 = screen((-76, 18))
            x2, y2 = screen((76, 84))
            body.append(f'<rect x="{x1:.1f}" y="{y2:.1f}" width="{x2 - x1:.1f}" height="{y1 - y2:.1f}" rx="18" fill="#111827" stroke="#111827"/>')
            body.append(f'<rect x="{x1 + 10:.1f}" y="{y2 + 10:.1f}" width="{x2 - x1 - 20:.1f}" height="{y1 - y2 - 20:.1f}" rx="12" fill="#d7eef4"/>')
        elif view_key == "side":
            body.append('<path d="M 375 425 L 530 145" stroke="#111827" stroke-width="26" stroke-linecap="round"/>')
        else:
            body.append('<path d="M 430 510 L 635 272" stroke="#111827" stroke-width="30" stroke-linecap="round"/>')
        body.append("</g>")

    notes = [
        "尺寸：约 170mm 宽 x 90mm 深 x 64mm 高",
        "后靠角：68°，适合横屏 StandBy 观看",
        "中间开槽：给 USB-C/Lightning 线穿出",
        "建议：0.2mm 层高，15-25% 填充，PETG/PLA 均可",
    ]
    for i, note in enumerate(notes):
        body.append(f'<text x="56" y="{690 + i * 28}" font-family="Arial, sans-serif" font-size="20" fill="#3c4043">{note}</text>')
    body.append("</svg>")
    Path(path).write_text("\n".join(body), encoding="utf-8")


write_stl(OUT / "iphone_standby_dock.stl")
write_obj(OUT / "iphone_standby_dock.obj")
Path(OUT / "iphone_standby_dock.scad").write_text(
    """// iPhone horizontal StandBy dock, units in mm.
// Open in OpenSCAD, then export STL after changing parameters if needed.

width = 170;
depth = 90;
base_h = 9;
slot_w = 36;
back_angle = 68;

module rail(y0, y1) {
  translate([0, y0, 0]) cube([depth, y1 - y0, base_h]);
}

module split_pair(x0, x1, z0, z1) {
  translate([x0, -width/2, z0]) cube([x1-x0, (width-slot_w)/2, z1-z0]);
  translate([x0, slot_w/2, z0]) cube([x1-x0, (width-slot_w)/2, z1-z0]);
}

union() {
  rail(-width/2, -20);
  rail(20, width/2);
  translate([38, -width/2, 0]) cube([depth-38, width, 12]);
  split_pair(8, 20, 8, 24);      // front retaining lip with cable gap
  split_pair(20, 46, 9, 15);     // low shelf under the phone edge

  // Angled back support.
  translate([36, 0, 11])
    rotate([0, 90-back_angle, 0])
      translate([0, -width/2, 0])
        cube([58, width, 9]);
}
""",
    encoding="utf-8",
)
for key in views:
    draw_svg(OUT / f"iphone_standby_dock_{key}.svg", key)

print(OUT.resolve())
