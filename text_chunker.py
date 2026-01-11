# Component 2: Text Chunker
# Breaks large text into smaller chunks

def chunk_text(text, chunk_size=500):
    """
    Takes a string and breaks it into chunks of specified size
    Returns a list of text chunks
    """
    text_chunked = []
    file_length = len(text)
    for i in range(0, file_length, chunk_size):
        chunk = text[i:i + chunk_size]
        text_chunked.append(chunk)
    return text_chunked

# Component 3: Batch Creator
# Groups chunks into larger batches

def create_batches(chunks, batch_size):
    """
    Takes a list of chunks and groups them into batches
    Returns a list of batches (each batch is combined text)
    """
    batches = []
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]
        combined_batch = "".join(batch)
        batches.append(combined_batch)
    return batches

# Test the chunker
if __name__ == "__main__":
    # Example usage
    sample_text = """Any culture tells you how to live your one and only life: to wit as everyone else does. 
    Probably most cultures prize, as ours rightly does, making a contribution by working hard at work that you love; 
    being in the know, and intelligent; gathering a surplus; and loving your family above all, and your dog, your boat, bird-watching."""
    
    # Test chunking
    chunks = chunk_text(sample_text, chunk_size=100)
    print("Total text length:", len(sample_text), "characters")
    print("Chunk size: 100 characters")
    print("Total chunks created:", len(chunks))
    
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1} ({len(chunk)} chars):", chunk[:50], "...")
    
    # Test batching
    print("\n--- Testing Batch Creator ---")
    batches = create_batches(chunks, batch_size=4)
    print("Total batches created:", len(batches))
    print("First batch preview:", batches[0][:100], "...")
