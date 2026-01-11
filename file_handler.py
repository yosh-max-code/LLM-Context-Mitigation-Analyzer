# Component 1: Text File Handler

def file_read(filename):
    with open(filename, "r") as file:
        file_content = file.read()
        return file_content

def file_write(filename, content):
    with open(filename, "w") as file:
        file.write(content)

# Test the file handler
if __name__ == "__main__":
    # Example usage
    # text = file_read("test_data.txt")
    # print("Total text length:", len(text), "characters")
    pass
