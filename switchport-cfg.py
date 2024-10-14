# Function to define VLANs
vlan_id = input("Enter the VLAN ID: ")
vlan_name = input("Enter the VLAN name: ")
description = input("Enter Description: ")
interface_prefix = input("Enter Ethernet Interface prefix (e.g., Ethernet): ")

# Get a comma-separated list of interface numbers from the user
interface_numbers = input("Enter the interface numbers (e.g., 1,2,3,5,10): ")
interface_list = [f"{interface_prefix}{num.strip()}" for num in interface_numbers.split(',')]

def vlan(vlan_id, vlan_name):
    # Format and print the VLAN configuration
    configuration = (
        f"vlan {vlan_id}\n"
        f"  name {vlan_name}\n"
    )
    print(configuration)

# Call the VLAN function
vlan(vlan_id, vlan_name)

def vlan_configuration(interface, description, vlan_id):
    # Format and print the VLAN configuration
    configuration = (
        f"interface {interface}\n"
        f"  description {description}\n"
        f"  switchport access vlan {vlan_id}\n"
    )
    print(configuration)

# Loop through the specified interface numbers
for interface in interface_list:
    vlan_configuration(interface, description, vlan_id)
