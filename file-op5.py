#copy with chunk

with open('test-pic.png', 'rb') as rf:
    with open('test-pic-copy3.png', 'wb') as wf:
        chunk_size = 100
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
