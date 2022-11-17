printf "GIFs for HIV-1 protease"

# HIV structure MD
printf "> Molecular dynamics\n"
convert -delay 10 -loop 0 HIV/DM/*.png HIV/DM.gif

# Cavities MD
printf "> Molecular dynamics with cavities"
convert -delay 10 -loop 0 HIV/cavity/*.png HIV/cavity.gif

# HIV Volume/Depth MD
printf "> Shape/Volume/Depth characterization\n"
convert -delay 10 -loop 0 HIV/volume/*.png HIV/volume.gif

# HIV Surface/Hydropathy MD
printf "> Surface/Hydropathy characeterizaiton\n"
convert -delay 10 -loop 0 HIV/surface/*.png HIV/surface.gif

# HIV Interface residues MD
printf "> Constitutional characeterizaiton\n"
convert -delay 10 -loop 0 HIV/residues/*.png HIV/residues.gif
