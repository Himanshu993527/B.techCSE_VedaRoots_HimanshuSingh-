#!/usr/bin/env python3
"""
Create simple 3D plant models using Three.js geometry
This script generates basic GLB files for medicinal plants
"""

import json
import struct
import numpy as np
from pathlib import Path

def create_simple_plant_model(plant_type="tulsi"):
    """Create a simple plant model with basic geometry"""
    
    # Define vertices, normals, and indices for a simple plant
    if plant_type == "tulsi":
        # Tulsi - bushy herb with leaves
        vertices = [
            # Stem
            0.0, 0.0, 0.0,   # bottom center
            0.0, 2.0, 0.0,   # top center
            -0.1, 0.0, 0.0,  # bottom left
            0.1, 0.0, 0.0,   # bottom right
            -0.05, 2.0, 0.0, # top left
            0.05, 2.0, 0.0,  # top right
            
            # Leaves
            -0.5, 1.5, 0.0,  # left leaf base
            -1.0, 1.8, 0.0,  # left leaf tip
            0.5, 1.5, 0.0,   # right leaf base
            1.0, 1.8, 0.0,   # right leaf tip
            -0.3, 1.8, 0.0,  # upper left leaf
            0.3, 1.8, 0.0,   # upper right leaf
        ]
        
        indices = [
            # Stem triangles
            0, 2, 4,  0, 4, 3,
            3, 4, 5,  3, 5, 1,
            
            # Leaf triangles
            2, 6, 7,  3, 8, 9,
            4, 10, 5,  4, 5, 11
        ]
        
    elif plant_type == "ashwagandha":
        # Ashwagandha - shrub with berries
        vertices = [
            # Main stem
            0.0, 0.0, 0.0,
            0.0, 3.0, 0.0,
            -0.15, 0.0, 0.0,
            0.15, 0.0, 0.0,
            -0.1, 3.0, 0.0,
            0.1, 3.0, 0.0,
            
            # Branches
            -0.8, 2.0, 0.0,
            0.8, 2.0, 0.0,
            -0.6, 1.5, 0.0,
            0.6, 1.5, 0.0,
            
            # Berries (simplified as points)
            -0.9, 2.2, 0.0,
            0.9, 2.2, 0.0,
            -0.7, 1.7, 0.0,
            0.7, 1.7, 0.0,
        ]
        
        indices = [
            # Stem
            0, 2, 4,  0, 4, 3,
            3, 4, 5,  3, 5, 1,
            
            # Branches
            4, 6, 1,  5, 7, 1,
            2, 8, 4,  3, 9, 5
        ]
        
    elif plant_type == "neem":
        # Neem - tree structure
        vertices = [
            # Trunk
            0.0, 0.0, 0.0,
            0.0, 4.0, 0.0,
            -0.3, 0.0, 0.0,
            0.3, 0.0, 0.0,
            -0.2, 4.0, 0.0,
            0.2, 4.0, 0.0,
            
            # Branches
            -1.5, 3.0, 0.0,
            1.5, 3.0, 0.0,
            -1.2, 2.0, 0.0,
            1.2, 2.0, 0.0,
            
            # Leaves clusters
            -2.0, 3.2, 0.0,
            2.0, 3.2, 0.0,
        ]
        
        indices = [
            # Trunk
            0, 2, 4,  0, 4, 3,
            3, 4, 5,  3, 5, 1,
            
            # Branches
            4, 6, 1,  5, 7, 1,
            2, 8, 4,  3, 9, 5,
            6, 10, 7,  7, 11, 6
        ]
        
    else:
        # Default simple plant
        vertices = [
            0.0, 0.0, 0.0,
            0.0, 2.0, 0.0,
            -0.1, 0.0, 0.0,
            0.1, 0.0, 0.0,
            -0.05, 2.0, 0.0,
            0.05, 2.0, 0.0,
        ]
        
        indices = [
            0, 2, 4,  0, 4, 3,
            3, 4, 5,  3, 5, 1
        ]
    
    # Create normals (pointing outward)
    normals = []
    for i in range(0, len(vertices), 3):
        normals.extend([0.0, 0.0, 1.0])
    
    # Create UV coordinates
    uvs = []
    for i in range(0, len(vertices), 3):
        uvs.extend([0.5, 0.5])
    
    return {
        "vertices": vertices,
        "indices": indices,
        "normals": normals,
        "uvs": uvs
    }

def create_glb_file(mesh_data, filepath):
    """Create a simple GLB file from mesh data"""
    
    # This is a simplified GLB creator
    # In production, you'd use proper GLTF libraries
    
    # Create a simple binary representation
    vertices = mesh_data["vertices"]
    indices = mesh_data["indices"]
    
    # Convert to numpy arrays
    vertices_array = np.array(vertices, dtype=np.float32)
    indices_array = np.array(indices, dtype=np.uint16)
    
    # Create binary data
    binary_data = bytearray()
    
    # GLB header (simplified)
    binary_data.extend(b'glTF')
    binary_data.extend(struct.pack('<I', 2))  # version
    binary_data.extend(struct.pack('<I', 0))  # total size (will be updated)
    
    # JSON chunk (minimal)
    json_chunk = json.dumps({
        "asset": {"version": "2.0"},
        "scenes": [{"nodes": [0]}],
        "nodes": [{"mesh": 0}],
        "meshes": [{"primitives": [{
            "attributes": {"POSITION": 1},
            "indices": 0
        }]}],
        "buffers": [{"byteLength": len(vertices_array) * 4 + len(indices_array) * 2}],
        "bufferViews": [
            {"buffer": 0, "byteOffset": 0, "byteLength": len(indices_array) * 2, "target": 34963},
            {"buffer": 0, "byteOffset": len(indices_array) * 2, "byteLength": len(vertices_array) * 4, "target": 34962}
        ],
        "accessors": [
            {"bufferView": 0, "componentType": 5123, "count": len(indices_array), "type": "SCALAR"},
            {"bufferView": 1, "componentType": 5126, "count": len(vertices_array) // 3, "type": "VEC3", "min": [0, 0, 0], "max": [1, 1, 1]}
        ]
    })
    
    # Pad JSON to 4-byte alignment
    json_padding = (4 - (len(json_chunk) % 4)) % 4
    json_chunk += ' ' * json_padding
    
    # JSON chunk header
    binary_data.extend(struct.pack('<I', len(json_chunk)))
    binary_data.extend(b'JSON')
    binary_data.extend(json_chunk.encode('utf-8'))
    
    # Binary chunk
    binary_data.extend(struct.pack('<I', len(indices_array) * 2 + len(vertices_array) * 4))
    binary_data.extend(b'BIN\0')
    
    # Add index data
    binary_data.extend(indices_array.tobytes())
    
    # Add vertex data
    binary_data.extend(vertices_array.tobytes())
    
    # Update total size
    total_size = len(binary_data)
    binary_data[8:12] = struct.pack('<I', total_size)
    
    # Write to file
    with open(filepath, 'wb') as f:
        f.write(binary_data)

def create_all_models():
    """Create all required 3D plant models"""
    
    models_dir = Path("static/models")
    models_dir.mkdir(exist_ok=True)
    
    plants = {
        "tulsi": "tulsi",
        "ashwagandha": "ashwagandha", 
        "neem": "neem",
        "turmeric": "turmeric",
        "aloe_vera": "aloe_vera",
        "giloy": "giloy",
        "shatavari": "shatavari",
        "brahmi": "brahmi",
        "karela": "karela",
        "arjuna": "arjuna"
    }
    
    for plant_name, model_name in plants.items():
        print(f"Creating model for {plant_name}...")
        
        # Create mesh data
        mesh_data = create_simple_plant_model(plant_name)
        
        # Save as GLB
        filepath = models_dir / f"{model_name}.glb"
        create_glb_file(mesh_data, filepath)
        
        print(f"  Saved: {filepath}")

if __name__ == "__main__":
    create_all_models()
    print("All 3D models created successfully!")
