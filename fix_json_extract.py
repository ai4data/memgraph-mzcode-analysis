#!/usr/bin/env python3
"""
Fix JSON_EXTRACT function calls in Jupyter notebooks for Memgraph compatibility.
Memgraph doesn't have JSON_EXTRACT, so we need to parse JSON properties in Python instead.
"""

import json
import re

def fix_notebook(filename):
    """Fix JSON_EXTRACT calls in a Jupyter notebook."""
    
    with open(filename, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Pattern to match JSON_EXTRACT calls
    json_extract_pattern = r'JSON_EXTRACT\(([^,]+),\s*[\'"]([^\'"]+)[\'"]\)'
    
    changes_made = 0
    
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            for i, line in enumerate(cell['source']):
                # Replace JSON_EXTRACT with property access
                if 'JSON_EXTRACT' in line:
                    # For materialized views, we'll just return the full properties
                    # and parse them in Python instead
                    if 'materialized_view' in line:
                        # Replace the entire query to return just properties
                        new_line = re.sub(
                            r'JSON_EXTRACT\(v\.properties,\s*[\'"][^\'"]+[\'"\])\s*as\s+\w+',
                            'v.properties as properties',
                            line
                        )
                        # Remove multiple property extractions, keep just one
                        new_line = re.sub(
                            r',\s*JSON_EXTRACT\(v\.properties,\s*[\'"][^\'"]+[\'"\])\s*as\s+\w+',
                            '',
                            new_line
                        )
                    else:
                        # For other cases, replace with property access
                        new_line = re.sub(json_extract_pattern, r'\1', line)
                    
                    if new_line != line:
                        cell['source'][i] = new_line
                        changes_made += 1
                        print(f"Fixed line: {line.strip()}")
                        print(f"     -> {new_line.strip()}")
    
    if changes_made > 0:
        # Write the fixed notebook
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1, ensure_ascii=False)
        print(f"\nFixed {changes_made} JSON_EXTRACT calls in {filename}")
    else:
        print(f"No JSON_EXTRACT calls found in {filename}")

if __name__ == "__main__":
    # Fix the problematic notebook
    fix_notebook("03_analytics_ready_features.ipynb")