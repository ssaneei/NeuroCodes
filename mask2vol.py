def mask2vol(maskfilepath,unit):
    volume = ""
    import nibabel as nib
    mask= nib.load(maskfilepath)
    mask_data = mask.get_fdata()
    import numpy as np
    vox_size = np.array(mask.header.get_zooms()).prod()
    count_of_nonzeros = np.count_nonzero(mask_data)
    volume = count_of_nonzeros * vox_size
    try:
        if unit == 'mm3':
            return volume
        elif unit == 'cm3':
            #volume = mask.header.get_zooms()
            volume = [v/1000 for v in volume]
            return volume

    except:
        return("Unit can be either mm3 or cm3")


import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument("-q", "--quiet", action="store_true")

parser.add_argument("path", type=str, help="The mask file path")
parser.add_argument("unit", type=str, help="Unit of the voxel sizes")
args = parser.parse_args()
answer = mask2vol(args.path, args.unit)

if args.quiet:
    print(answer)
elif args.verbose:
    print(f"The file in the address{args.path} has {answer} voxel size in {args.unit}")
else:
    print(f"{args.path}:{answer}{args.unit}")
