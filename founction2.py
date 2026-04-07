# function to calculate disk space usage 
def calculate_disk_space(total_space, used_space):
    free_space = total_space - used_space 
    return free_space

# calling the function with arguments
total = 500 # GB
used = 300 # GB

free = calculate_disk_space(total,used)

print(f"free disk space:{free}GB")