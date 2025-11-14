'''
this function reads the input document and chunks it
and sends it to embeddings to save it to vectordb along with some metadata

'''

def fetch_and_chunk_document():
    with open('Documents/wellness_plan.md','r', encoding='utf-8') as file:
        content = file.read()
        chunker(content)
        
def chunker(file_text, chunk_size = 150, overlap = 50):
    total_chunks = []
    content = file_text.split('\n')
    trimmed_lines = [line.strip() for line in content if line.strip()]
    processed_lines = '\n'.join(trimmed_lines)
    current_chunk = []
    curr_chunk_length = 0
    for line in trimmed_lines:
        #print(curr_chunk_length)
        current_chunk.append(line)
        curr_chunk_length+=len(line)
        if curr_chunk_length >= chunk_size and not any('|' in l for l in current_chunk):
            #break adding to the chunk list
            #print(f"curr chunk is: ${'\n'.join(current_chunk)}")
            total_chunks.append('\n'.join(current_chunk))
            current_chunk = current_chunk[-overlap:]
            curr_chunk_length = sum(len(l) for l in current_chunk)
            pass
        if curr_chunk_length:
            total_chunks.append('\n'.join(current_chunk))
    print(total_chunks)
    print(len(total_chunks))
        

fetch_and_chunk_document()
