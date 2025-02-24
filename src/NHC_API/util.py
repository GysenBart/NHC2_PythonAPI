import json

class util_functions:
    def extract_devices(json_file_path):
        """
        Extract all devices from a large JSON file.
        Each device starts with a UUID field.
        
        Args:
            json_file_path (str): Path to the JSON file
            
        Returns:
            list: List of device dictionaries
        """
        # Read the JSON file
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        
        # Extract devices from the Params -> Devices path
        devices = []
        if "Params" in data and isinstance(data["Params"], list):
            for param in data["Params"]:
                if "Devices" in param and isinstance(param["Devices"], list):
                    devices.extend(param["Devices"])
        
        # Print summary information
        print(f"Found {len(devices)} devices")
        
        # Optional: Print UUIDs of all devices
        for i, device in enumerate(devices):
            print(f"Device {i+1}: UUID={device.get('Uuid', 'Unknown')}, Name={device.get('Name', 'Unnamed')}")
        
        return devices