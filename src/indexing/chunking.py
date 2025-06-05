from langchain.text_splitter import RecursiveCharacterTextSplitter
def split_text_into_chunks(text: str,chunk_size:int,chunk_overlap:int):
    """Splits the input text into smaller chunks.

    Args:
        text (str): The input text to be split.
        chunk_size (int): The size of each chunk.
        chunk_overlap (int): The number of overlapping characters between chunks.

    Returns:
        list: A list of Documnet objects chunks.
    """
    try:
        splitter=RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        return splitter.create_documents([text])
    except Exception as e:
        return f"An error occurred while splitting text: {e}"