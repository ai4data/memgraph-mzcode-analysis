#!/usr/bin/env python3
"""
Fix the specific cell in the notebook that has JSON_EXTRACT issues.
"""

import json

def fix_specific_cell():
    """Fix the materialized views cell specifically."""
    
    with open("03_analytics_ready_features.ipynb", 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Find and fix the problematic cell
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            source_text = ''.join(cell['source'])
            if 'List all available materialized views' in source_text and 'JSON_EXTRACT' in source_text:
                print("Found problematic cell, fixing...")
                
                # Replace the entire cell content
                new_source = [
                    "# List all available materialized views\n",
                    "views_df, _ = execute_query(\n",
                    "    \"\"\"MATCH (v:Node {node_type: 'materialized_view'})\n",
                    "       RETURN v.name as view_name,\n",
                    "              v.id as view_id,\n",
                    "              v.properties as properties\n",
                    "       ORDER BY v.name\"\"\",\n",
                    "    \"Available materialized views\"\n",
                    ")\n",
                    "\n",
                    "if not views_df.empty:\n",
                    "    print(f\"\\n📋 Found {len(views_df)} Materialized Views:\")\n",
                    "    for _, view in views_df.iterrows():\n",
                    "        # Parse properties JSON to extract specific fields\n",
                    "        try:\n",
                    "            props = json.loads(view['properties']) if isinstance(view['properties'], str) else view['properties']\n",
                    "            record_count = props.get('record_count', 'Unknown')\n",
                    "            version = props.get('version', 'Unknown')\n",
                    "            print(f\"  • {view['view_name']}: {record_count} records (v{version})\")\n",
                    "        except:\n",
                    "            print(f\"  • {view['view_name']}: Properties parsing failed\")\n",
                    "    \n",
                    "    display(views_df)\n",
                    "else:\n",
                    "    print(\"❌ No materialized views found.\")\n",
                    "    print(\"The graph may not be analytics-ready or may need to be regenerated.\")"
                ]
                
                cell['source'] = new_source
                print("Fixed the materialized views cell")
                break
    
    # Fix the helper function too
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            source_text = ''.join(cell['source'])
            if 'def get_materialized_view_data' in source_text and 'JSON_EXTRACT' in source_text:
                print("Found helper function cell, fixing...")
                
                new_source = [
                    "# Helper function to access materialized view data\n",
                    "def get_materialized_view_data(view_name, description=None):\n",
                    "    \"\"\"Get data from a materialized view.\"\"\"\n",
                    "    query = f\"\"\"MATCH (v:Node {{id: 'view:{view_name}'}})\n",
                    "                RETURN v.properties as view_properties\"\"\"\n",
                    "    \n",
                    "    df, exec_time = execute_query(query, description or f\"Accessing {view_name} materialized view\", time_it=True)\n",
                    "    \n",
                    "    if not df.empty and df.iloc[0]['view_properties']:\n",
                    "        try:\n",
                    "            props = json.loads(df.iloc[0]['view_properties']) if isinstance(df.iloc[0]['view_properties'], str) else df.iloc[0]['view_properties']\n",
                    "            view_data = props.get('data')\n",
                    "            record_count = props.get('record_count')\n",
                    "            print(f\"📊 Records in view: {record_count}\")\n",
                    "            return view_data, exec_time\n",
                    "        except Exception as e:\n",
                    "            print(f\"❌ Error parsing view data: {e}\")\n",
                    "            return None, exec_time\n",
                    "    else:\n",
                    "        print(\"❌ View not found or empty\")\n",
                    "        return None, exec_time"
                ]
                
                cell['source'] = new_source
                print("Fixed the helper function cell")
                break
    
    # Fix the assessment class too
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            source_text = ''.join(cell['source'])
            if 'class SSISMigrationAssessment' in source_text and 'JSON_EXTRACT' in source_text:
                print("Found assessment class cell, fixing...")
                
                # Find the get_view_data method and fix it
                for i, line in enumerate(cell['source']):
                    if 'JSON_EXTRACT' in line:
                        cell['source'][i] = line.replace(
                            'RETURN JSON_EXTRACT(v.properties, \'$.data\') as data',
                            'RETURN v.properties as properties'
                        )
                
                # Also need to fix the parsing logic
                for i, line in enumerate(cell['source']):
                    if 'return json.loads(result[0])' in line:
                        cell['source'][i] = '            props = json.loads(result[0]) if isinstance(result[0], str) else result[0]\\n'
                        cell['source'].insert(i+1, '            return props.get(\"data\", [])\\n')
                        break
                
                print("Fixed the assessment class cell")
                break
    
    # Write the fixed notebook
    with open("03_analytics_ready_features.ipynb", 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    
    print("Notebook has been fixed!")

if __name__ == "__main__":
    fix_specific_cell()