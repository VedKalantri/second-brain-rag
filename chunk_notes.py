from langchain_text_splitters import RecursiveCharacterTextSplitter


def get_chunks(file_path="notes.txt"):
    """
    Reads the notes file and returns a list of text chunks.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=30,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )

    return text_splitter.split_text(text)


if __name__ == "__main__":

    chunks = get_chunks()

    for i, chunk in enumerate(chunks, start=1):
        print(f"\n----- Chunk {i} -----")
        print(chunk)