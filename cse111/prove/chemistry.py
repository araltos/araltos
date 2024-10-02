from formula import parse_formula

NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1
ATOMIC_NUMBER_INDEX = 2 

SYMBOL_INDEX = 0
QUANTITY_INDEX = 1

def make_periodic_table():
    """Create and return a compound dictionary containing data for all 94 naturally occurring elements"""
    periodic_table_dict = {
        # symbol: [name, atomic_mass]
        "Ac": ["Actinium", 227, 1],
        "Ag": ["Silver", 107.8682,2],
        "Al": ["Aluminum", 26.9815386,3],
        "Ar": ["Argon", 39.948,4],
        "As": ["Arsenic", 74.9216,5],
        "At": [ "Astatine", 210,6],
        "Au": [ "Gold", 196.966569,7],
        "B":  ["Boron", 10.811,8],
       "Ba": [ "Barium", 137.327,9],
        "Be": [ "Beryllium", 9.012182,10],
        "Bi": [ "Bismuth", 208.9804,11],
        "Br" :[ "Bromine", 79.904,12],
        "C"  :["Carbon", 12.0107,13],
        "Ca" :[ "Calcium", 40.078,14],
        "Cd" :[ "Cadmium", 112.411,15],
        "Ce" :[ "Cerium", 140.116,16],
        "Cl" :[ "Chlorine", 35.453,17],
        "Co" :[ "Cobalt", 58.933195,18],
        "Cr" :[ "Chromium", 51.9961,19],
        "Cs" :[ "Cesium", 132.9054519,20],
        "Cu" :[ "Copper", 63.546,21],
        "Dy" :[ "Dysprosium", 162.5,22],
        "Er" :[ "Erbium", 167.259,23],
        "Eu" :[ "Europium", 151.964,24],
        "F"  :["Fluorine", 18.9984032,25],
        "Fe" :[ "Iron", 55.845,26],
        "Fr" :[ "Francium", 223,27],
        "Ga" :[ "Gallium", 69.723,28],
        "Gd" :[ "Gadolinium", 157.25,29],
        "Ge" :[ "Germanium", 72.64,30],
        "H"  :["Hydrogen", 1.00794,31],
        "He" :[ "Helium", 4.002602,32],
        "Hf" :[ "Hafnium", 178.49,33],
        "Hg" :[ "Mercury", 200.59,34],
        "Ho" :[ "Holmium", 164.93032,35],
        "I"  :["Iodine", 126.90447,36],
        "In" :[ "Indium", 114.818,37],
        "Ir" :[ "Iridium", 192.217,38],
        "K"  :["Potassium", 39.0983,39],
        "Kr" :[ "Krypton", 83.798,40],
        "La" :[ "Lanthanum", 138.90547,41],
        "Li" :[ "Lithium", 6.941,42],
        "Lu" :[ "Lutetium", 174.9668,43],
        "Mg" :[ "Magnesium", 24.305,44],
        "Mn" :[ "Manganese", 54.938045,45],
        "Mo" :[ "Molybdenum", 95.96,46],
        "N"  :["Nitrogen", 14.0067,47],
        "Na" :[ "Sodium", 22.98976928,48],
        "Nb" :[ "Niobium", 92.90638,49],
        "Nd" :[ "Neodymium", 144.242,50],
        "Ne" :[ "Neon", 20.1797,51],
        "Ni" :[ "Nickel", 58.6934,52],
        "Np" :[ "Neptunium", 237,53],
        "O"  :["Oxygen", 15.9994,54],
        "Os" :[ "Osmium", 190.23,55],
        "P"  :["Phosphorus", 30.973762,56],
        "Pa" :[ "Protactinium", 231.03588,57],
        "Pb" :[ "Lead", 207.2,58],
        "Pd" :[ "Palladium", 106.42,59],
        "Pm" :[ "Promethium", 145,60],
        "Po" :[ "Polonium", 209,61],
        "Pr" :[ "Praseodymium", 140.90765,62],
        "Pt" :[ "Platinum", 195.084,63],
        "Pu" :[ "Plutonium", 244,64],
        "Ra" :[ "Radium", 226,65],
        "Rb" :[ "Rubidium", 85.4678,66],
        "Re" :[ "Rhenium", 186.207,67],
        "Rh" :[ "Rhodium", 102.9055,68],
        "Rn" :[ "Radon", 222,69],
        "Ru" :[ "Ruthenium", 101.07,70],
        "S"  :["Sulfur", 32.065,71],
        "Sb" :[ "Antimony", 121.76,72],
        "Sc" :[ "Scandium", 44.955912,73],
        "Se" :[ "Selenium", 78.96,74],
        "Si" :[ "Silicon", 28.0855,75],
        "Sm" :[ "Samarium", 150.36,76],
        "Sn" :[ "Tin", 118.71,77],
        "Sr" :[ "Strontium", 87.62,78],
        "Ta" :[ "Tantalum", 180.94788,79],
        "Tb" :[ "Terbium", 158.92535,80],
        "Tc" :[ "Technetium", 98,81],
        "Te" :[ "Tellurium", 127.6,82],
        "Th" :[ "Thorium", 232.03806,83],
        "Ti" :[ "Titanium", 47.867,84],
        "Tl" :[ "Thallium", 204.3833,85],
        "Tm" :[ "Thulium", 168.93421,86],
        "U"  :["Uranium", 238.02891,87],
        "V"  :["Vanadium", 50.9415,88],
        "W"  :["Tungsten", 183.84,89],
        "Xe" :[ "Xenon", 131.293,90],
        "Y"  :["Yttrium", 88.90585,91],
        "Yb" :[ "Ytterbium", 173.054,92],
        "Zn" :[ "Zinc", 65.38,93],
        "Zr" :[ "Zirconium", 91.224,94]
    }
    return periodic_table_dict

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the elements listed in symbol_quantity_list."""
    total_molar_mass = 0
    for symbol, quantity in symbol_quantity_list:
        atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]
        total_molar_mass += atomic_mass * quantity
    return total_molar_mass

def sum_protons(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total number of protons in all the elements listed in symbol_quantity_list."""
    total_protons = 0
    for symbol, quantity in symbol_quantity_list:
        atomic_number = periodic_table_dict[symbol][ATOMIC_NUMBER_INDEX]
        total_protons += atomic_number * quantity
    return total_protons

def main():
    periodic_table = make_periodic_table()

    formula = input("Enter the molecular formula of the sample: ")
    mass = float(input("Enter the mass in grams of the sample: "))

    symbol_quantity_list = parse_formula(formula, periodic_table)

    molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table)

    number_of_moles = mass / molar_mass

    total_protons = sum_protons(symbol_quantity_list, periodic_table)

    
    print(f"{molar_mass:.5f} grams/mole")
    print(f"{number_of_moles:.5f} moles")
    print(f"Total Protons: {total_protons}")

if __name__ == "__main__":
    main()

