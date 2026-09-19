import argparse
import os
from glob import glob

from pymol import cmd

parser = argparse.ArgumentParser(description="Visualize HIV cavity clusters in PyMOL.")
parser.add_argument(
    "--root",
    choices=["results/spde/grid", "results/spde/distance", "results/spde/contact"],
    required=True,
    help="Directory containing the cavity cluster directories.",
)
parser.add_argument(
    "--state",
    nargs="+",
    help="State directory or directories whose cavities should be loaded.",
)
args = parser.parse_args()

ROOT = args.root

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
state_dirs = sorted(os.listdir(ROOT))
print(args.state)
print(args.state is not None)
# If args.state is not set

if args.state is None:
    state_dirs = [
        state for state in state_dirs if state.isdigit() and os.path.isdir(os.path.join(ROOT, state))
    ]
else:
    # Check if the provided state directories exist and are valid
    state_dirs = [
        state
        for state in args.state
        if os.path.isdir(os.path.join(ROOT, state))
    ]
print(state_dirs)

# Load cavities
for i, state in enumerate(state_dirs):
    print(f"Loading cavities for state: {state}")
    dir_path = os.path.join(ROOT, state)
    pdbs = glob(os.path.join(dir_path, "*.pdb"))

    if not pdbs:
        continue

    selection = []

    for j, pdb in enumerate(pdbs):
        obj = f"obj_{j}"
        cmd.load(pdb, obj)
        selection.append(obj)

    cmd.create(f"{state}", " or ".join(selection))

    for obj in selection:
        cmd.delete(obj)

    # cmd.load(pdbs[0], f"{state}_ref")
    # cmd.show("spheres", f"{state}_ref")
    # cmd.color(colors[i], f"{state}_ref")

    # Surface visualization
    cmd.hide("everything", f"{state}")
    cmd.show("surface", f"{state}")
    cmd.color(colors[i], f"{state}")


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