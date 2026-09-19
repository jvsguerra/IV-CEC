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
parser.add_argument(
    "--representation",
    choices=["spheres", "surface"],
    default="spheres",
    help="Representation style for the cavities (default: spheres).",
)
parser.add_argument(
    "--verbose", action="store_true", help="Enable verbose output for debugging."
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
cmd.dss("HIV")

# Select state directories to load cavities from
state_dirs = [d for d in os.listdir(ROOT) if os.path.isdir(os.path.join(ROOT, d))]
if args.state is None:
    state_dirs: list[int] = [
        int(state) for state in state_dirs if state.isdigit() and os.path.isdir(os.path.join(ROOT, state))
    ]
else:
    # Check if the provided state directories exist and are valid
    state_dirs: list[int] = [
        int(state)
        for state in args.state
        if os.path.isdir(os.path.join(ROOT, state))
    ]

# Load cavities
for state in sorted(state_dirs):
    if args.verbose:
        print(f"Loading cavities for state: {state}")
    dir_path = os.path.join(ROOT, str(state))
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

    if args.verbose:
        print(f"> Color: {colors[state]}")

    cmd.hide("everything", f"{state}")

    # Sphere visualization
    if args.representation == "spheres":
        cmd.show("spheres", f"{state}")
        cmd.color(colors[state], f"{state}")

    # Surface visualization
    if args.representation == "surface":
        cmd.show("surface", f"{state}")
        cmd.color(colors[state], f"{state}")

# Transparency and visualization settings
cmd.set("transparency", 0.0)

# Reduce VDW radius of H and HA atoms
if args.verbose:
    print("Reducing VDW radius of H and HA atoms to 0.3")
cmd.alter("name H+HA", "vdw=0.3")
cmd.rebuild()

# Nice rendering
# cmd.set("cartoon_fancy_helices", 1)
# cmd.set("surface_quality", 1)
# cmd.set("two_sided_lighting", 1)
cmd.orient("HIV")

# Save the final image
cmd.png(
    os.path.join(ROOT, f"clusters_{args.representation}.png"),
    width=6000,
    height=4500,
    dpi=600,
    ray=1,
)