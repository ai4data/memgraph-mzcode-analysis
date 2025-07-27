#!/usr/bin/env python3
"""
Debug script to examine the metadata structure in detail
"""

import mgclient
import json

# Connect to Memgraph
mg = mgclient.connect(host='localhost', port=7687, username='', password='')

def debug_metadata():
    cursor = mg.cursor()
    
    # Get the full metadata
    cursor.execute("MATCH (m:Node {node_type: 'graph_metadata'}) RETURN m.properties as props")
    result = cursor.fetchone()
    
    if result:
        props = result[0]
        print("🔍 Full Metadata Properties:")
        print("=" * 50)
        
        # Parse the JSON if it's a string
        if isinstance(props, str):
            try:
                props = json.loads(props)
            except:
                print("Could not parse as JSON")
                print(props)
                return
        
        # Pretty print the full structure
        print(json.dumps(props, indent=2))
        
        print("\n" + "=" * 50)
        print("🎯 Key Observations:")
        
        # Check specific fields
        if 'node_type_counts' in props:
            print(f"Node type counts structure: {type(props['node_type_counts'])}")
            print(f"Node type counts content: {props['node_type_counts']}")
        
        if 'total_nodes' in props:
            print(f"Total nodes: {props['total_nodes']}")
            
        if 'analysis_timestamp' in props:
            print(f"Analysis timestamp: {props['analysis_timestamp']}")
    else:
        print("❌ No metadata found")

def check_actual_counts():
    cursor = mg.cursor()
    
    print("\n🔍 Actual Node Counts:")
    print("=" * 30)
    
    # Get actual counts
    cursor.execute("""
        MATCH (n) 
        WHERE n.node_type IN ['pipeline', 'operation', 'table', 'connection', 'parameter', 'variable']
        RETURN n.node_type as node_type, count(n) as count 
        ORDER BY count DESC
    """)
    
    results = cursor.fetchall()
    for row in results:
        print(f"{row[0]}: {row[1]}")

if __name__ == "__main__":
    debug_metadata()
    check_actual_counts()