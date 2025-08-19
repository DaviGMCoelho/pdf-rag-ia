class Validation():
    def exists(self, content):
        chunks_returned = []
        for chunk in content:
            text = chunk[0].page_content
            chunks_returned.append(text)
        join = '\n\n----\n\n'.join(chunks_returned)
        return join
