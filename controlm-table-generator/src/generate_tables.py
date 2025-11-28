"""
Control-M Table Generator v1.0
Generates XML tables automatically for every ABI listed in abi_list.txt.
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from copy import deepcopy

# ==========================================================
# 1. Define paths relative to the script location
# ==========================================================
BASE_DIR = Path(__file__).resolve().parent       # folder: /src
ROOT_DIR = BASE_DIR.parent                       # parent folder (repository root)

TEMPLATE_PATH = BASE_DIR / "template_table.xml"
ABI_LIST_PATH = BASE_DIR / "abi_list.txt"

OUTPUT_DIR = ROOT_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

OUTPUT_PATH = OUTPUT_DIR / "tables_generated.xml"


# ==========================================================
# 2. Load template
# ==========================================================
if not TEMPLATE_PATH.exists():
    raise FileNotFoundError(f"Template file not found: {TEMPLATE_PATH}")

template_tree = ET.parse(TEMPLATE_PATH)
template_root = template_tree.getroot()


# ==========================================================
# 3. Load ABI list
# ==========================================================
if not ABI_LIST_PATH.exists():
    raise FileNotFoundError(f"ABI list file not found: {ABI_LIST_PATH}")

with open(ABI_LIST_PATH, "r", encoding="utf-8") as f:
    abi_list = [line.strip() for line in f if line.strip()]

if not abi_list:
    raise ValueError("ABI list is empty. Please add ABI codes to abi_list.txt.")


# ==========================================================
# 4. Create the output XML
# ==========================================================
root_out = ET.Element("TABLES")

for abi in abi_list:

    # Deep-copy the template for the current ABI
    table_copy = deepcopy(template_root)

    # Apply placeholder replacement
    for elem in table_copy.iter():
        if elem.text:
            elem.text = elem.text.replace("{{ABI}}", abi)

    # Example: set dynamic table name
    for elem in table_copy.iter("TABLE_NAME"):
        elem.text = f"{abi}_TEST"

    # Append generated table
    root_out.append(table_copy)


# ==========================================================
# 5. Save the final XML
# ==========================================================
tree_out = ET.ElementTree(root_out)
tree_out.write(OUTPUT_PATH, encoding="utf-8", xml_declaration=True)

print("\n==== Control-M Table Generator v1.0 ====")
print(f"Template loaded from : {TEMPLATE_PATH}")
print(f"ABI list loaded from : {ABI_LIST_PATH}")
print(f"Output directory     : {OUTPUT_DIR}")
print(f"Output XML created   : {OUTPUT_PATH}")
print(f"Total tables created : {len(abi_list)}")
print("✔ Generation completed successfully.\n")
