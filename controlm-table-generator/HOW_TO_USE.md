HOW TO USE – Control-M Table Generator
======================================

This guide explains how to use the Control-M Table Generator to produce XML
tables starting from a template and a list of ABI codes.

1. Prepare the Template:
   Edit templates/template_table.xml and use placeholder {{ABI}}.

2. Edit the ABI List:
   Add one ABI per line in abi_list.txt.

3. Run the Generator:
   python src/generate_tables.py

4. Output:
   Output file will be written to output/tables_generated.xml
