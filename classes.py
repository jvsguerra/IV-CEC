import os
from glob import glob

from pymol import cmd

ROOT = "results/spde/distance"

colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "cyan",
    "blue",
    "violet",
    "magenta",
    "salmon",
    "lime",
    "marine",
    "tv_blue",
    "tv_green",
    "olive",
    "wheat",
    "pink",
]

# Load HIV structure and set visualization
cmd.load("data/HIV.pdb", "HIV", state=1)
cmd.hide("everything", "HIV")
cmd.show("cartoon", "HIV")
cmd.color("green", "HIV")

# Load cavities
for i, name in enumerate(sorted(os.listdir(ROOT))):
    dir_path = os.path.join(ROOT, name)

    if not os.path.isdir(dir_path):
        continue

    pdbs = glob(os.path.join(dir_path, "*.pdb"))

    if not pdbs:
        continue

    selection = []

    for j, pdb in enumerate(pdbs):
        obj = f"obj_{j}"
        cmd.load(pdb, obj)
        selection.append(obj)

    cmd.create(f"{name}", " or ".join(selection))

    for obj in selection:
        cmd.delete(obj)

    # cmd.load(pdbs[0], f"{name}_ref")
    # cmd.show("spheres", f"{name}_ref")
    # cmd.color(colors[i], f"{name}_ref")

    # Surface visualization
    cmd.hide("everything", f"{name}")
    cmd.show("surface", f"{name}")
    cmd.color(colors[i], f"{name}")


# Transparency and visualization settings
cmd.set("transparency", 0.0)

# Reduce VDW radius of H and HA atoms
cmd.alter("name H+HA", "vdw=0.3")
cmd.rebuild()

# Nice rendering
# cmd.set("cartoon_fancy_helices", 1)
# cmd.set("surface_quality", 1)
# cmd.set("two_sided_lighting", 1)
cmd.orient("HIV")

# Save the final image
cmd.png(
    os.path.join(ROOT, "clusters.png"),
    width=6000,
    height=4500,
    dpi=600,
    ray=1,
)