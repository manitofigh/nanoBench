import subprocess

def hex_to_binary(hex_value):
    binary = ""
    for char in hex_value:
        decimal = int(char, 16)
        binary += format(decimal, '04b')
    return binary

# Get the first PCI device ID
output = subprocess.check_output("lspci | grep ':1e.3' | head -n 1 | cut -d' ' -f1", shell=True)
pci_id = output.decode().strip()
print("PCI Device ID:", pci_id)

# Run setpci command
output = subprocess.check_output(f"sudo setpci -s {pci_id} 0x9c.l", shell=True)
hex_value = output.decode().strip()
print("Hexadecimal value:", hex_value)

# Convert hex to binary
binary_value = hex_to_binary(hex_value)
print("Binary value:", binary_value)

# Print CHA status
print("CHA Status:", end=" ")
for i in range(32):
    status = binary_value[31-i]
    if status == "1":
        print(f"{i}:A", end=" ")
    else:
        print(f"{i}:I", end=" ")
print()

# Generate lines for activated CHAs
base_ctrl_hex = 0x0E01
base_counter_hex = 0x0E08
base_line = "msr_0x700=0x20000000.msr_0x{:04X}=0x408F34 msr_0x{:04X} CACHE_LOOKUP_CBO_{}"
CBO_counter = 0

print("\nActivated CHA lines:")
for i in range(28):
    if binary_value[31 - i] == "1":
        current_ctrl_hex = base_ctrl_hex + (i * 16)
        current_counter_hex = base_counter_hex + (i * 16)
        print(base_line.format(current_ctrl_hex, current_counter_hex, CBO_counter))
        CBO_counter += 1
