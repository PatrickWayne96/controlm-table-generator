# Control-M Table Generator (v1.0)

A lightweight Python tool that generates Control-M table definitions based on a template and a list of ABI codes.

This script automates the creation of multiple Control-M tables by:
- Duplicating a base XML template  
- Replacing the `{{ABI}}` placeholder  
- Generating one table per ABI  
- Producing a clean, ready-to-import XML file  

No external dependencies.  
No database.  
Just Python + XML.

---

## 🚀 Features

- ✔ Generates one table per ABI (based on `abi_list.txt`)
- ✔ Automatically replaces all `{{ABI}}` placeholders
- ✔ Automatically sets the `<TABLE_NAME>` based on ABI
- ✔ Produces a single output file: `tables_generated.xml`
- ✔ Uses only built-in Python modules (`xml.etree.ElementTree`)
- ✔ Fast and extremely easy to modify

---

## 📁 Project Structure

## License
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
