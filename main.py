from chemspipy import ChemSpider

cs = ChemSpider('9b584d03-8f0b-409a-a9f9-af4fb3ced33b')

# search_string = ["Hydrogen", "Helium"]

# element_list = ["Hydrogen","Helium","Lithium","Beryllium","Boron","Carbon","Nitrogen","Oxygen","Fluorine","Neon","Sodium","Magnesium","Aluminium","Silicon","Phosphorus",
# 	"Sulfur","Chlorine","Argon","Potassium","Calcium","Scandium","Titanium","Vanadium","Chromium",
# 	"Manganese","Iron","Cobalt","Nickel","Copper","Zinc","Gallium","Germanium","Arsenic",
# 	"Selenium","Bromine","Krypton","Rubidium","Strontium","Yttrium","Zirconium","Niobium","Molybdenum","Technetium",
# 	"Ruthenium","Rhodium","Palladium","Silver","Cadmium","Indium","Tin","Antimony","Tellurium","Iodine",
# 	"Xenon","Caesium","Barium","Lanthanum","Cerium","Praseodymium","Neodymium","Promethium","Samarium","Europium",
# 	"Gadolinium","Terbium","Dysprosium","Holmium","Erbium","Thulium","Ytterbium","Lutetium","Hafnium","Tantalum",
# 	"Tungsten","Rhenium","Osmium","Iridium","Platinum","Gold","Mercury","Thallium","Lead","Bismuth","Polonium","Astatine","Radon","Francium","Radium","Actinium","Thorium","Protactinium",
# 	"Uranium","Neptunium","Plutonium","Americium","Curium","Berkelium","Californium","Einsteinium","Fermium","Mendelevium","Nobelium",
# 	"Lawrencium","Rutherfordium","Dubnium","Seaborgium","Bohrium","Hassium","Meitnerium","Darmstadtium","Roentgenium","Copernicium","Ununtrium","Flerovium",
# 	"Ununpentium","Livermorium","Ununseptium","Ununoctium",
# 	"CO2","carbon dioxide","CO","carbon monoxide","NaCl","sodium chloride","CuO","copper oxide","AgBr","silver bromide","KI","potassium iodide","HCl","hydrogen chloride", "hydrochloric acid","NH4Cl","ammonium chloride","KOH",
# 	"potassium hydroxide","NaOH","sodium hydroxide","Ca(OH)2",
# 	"calcium hydroxide","CaS","calcium sulphide","NaNO3","sodium nitrate","HNO3","hydrogen nitrate (nitric acid)","NaHCO3","sodium bicarbonate","ZnSO4","zinc sulphate","MgCO3","magnesium carbonate","CaSO4",
# 	"calcium sulphate","CuCO3","copper carbonate","AlPO4",
# 	"aluminium phosphate","FeSO4","iron sulphate","FeCO3","iron carbonate","NH4NO3","ammonium nitrate","NH4HCO3","ammonium bicarbonate","H2SO4","hydrogen sulphate","sulphuric acid","Na2SO4","sodium sulphate",
# 	"(NH4)2CO3","ammonium carbonate", "salt", "water", "common salt",

# 	]

element_list = [
"Barrelene","Basketane","Cubane","Dodecahedrane","Fenestrane","Housane","Ladderane","Olympiadane","Olympicene","Penguinone","Prismane","Quadratic acid	","Sulflower","Tetrahedrane","Buckminsterfullerene","Bullvalene","Dickite","Josiphos","Alcindoromycine","Bohemamine","Collinemycin	","Ranasmurfin","Mimimycin","Musettamycin","Marcellomycin	","Pikachurin","Rudolphomycin","Arsole","Bastardane","Crapinon","DuPhos","BARF","Uranocene","Draculin","Moronic acid","Psicose","Rhamnose","Sydnone","Montelukast","Gossypol"
]



def save_mol_file(csid, mol_data):
	file_name = str(csid) + ".mol"
	file = open(file_name, 'w')
	file.write(mol_data)
	file.close()

# def save_x3d_file(csid, mol_data):
# 	file_name = str(csid) + ".x3d"
# 	file = open(file_name, 'w')

for element in element_list:
	for com in cs.search(element):
		# save_x3d_file(com.csid, com.mol_3d)
		save_mol_file(com.csid, com.mol_3d)
