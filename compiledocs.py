import os

def concatenate_mdx_files(dir_names, output_dir="compiled"):
    for dir_name in dir_names:
        # Prepare the content to be written in the new file
        concatenated_content = ""
        
        # Check if directory exists
        if not os.path.isdir(dir_name):
            print(f"Directory not found: {dir_name}")
            continue

        # List all files in the directory
        for filename in os.listdir(dir_name):
            if filename.endswith('.mdx'):
                # Open and read the content of the .mdx file
                with open(os.path.join(dir_name, filename), 'r') as file:
                    concatenated_content += file.read() + "\n"

        # Create a new .mdx file with the concatenated content
        with open(os.path.join(output_dir, f"{dir_name}.mdx"), 'w') as new_file:
            new_file.write(concatenated_content)

        print(f"Concatenated file created for directory: {dir_name}")

# Example usage
dir_names = ["components", "tutorials", "getstarted", "features"]  # Replace with your directory names
concatenate_mdx_files(dir_names)
