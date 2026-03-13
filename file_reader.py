import os

def read_building_info(building_number: str) -> str | None:
    """Read building information from text file."""
    building_file = f"building_info/{building_number}.txt"
    
    if not os.path.exists(building_file):
        return None
    
    try:
        with open(building_file, "r") as file:
            return file.read()
    except Exception as e:
        print(f"Error reading building file: {e}")
        return None

def get_available_buildings() -> list[str]:
    """Get list of available building numbers."""
    building_dir = "building_info"
    
    if not os.path.exists(building_dir):
        return []
    
    buildings = []
    for filename in os.listdir(building_dir):
        if filename.endswith(".txt"):
            building_num = filename.replace(".txt", "")
            buildings.append(building_num)
    
    return sorted(buildings)
