import os
from sentiment_analysis import score_paragraph

if __name__ == "__main__":
    # Path to text file in the same folder
    file_path = os.path.join(os.path.dirname(__file__), "TGB_Democracy_in_America.txt")

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        huge_text = f.read()

    # Split paragraphs by double newlines
    chunks = huge_text.split("\n\n")

    for i, chunk in enumerate(chunks):
        if chunk.strip():
            score = score_paragraph(chunk)
            print(f"Para {i+1}: Score = {score}")
