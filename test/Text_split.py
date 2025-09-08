from Sentiment_text import score_paragraph
import multitasking

@multitasking.task
def score(chunk_data,index):
    out = score_paragraph(chunk_data)
    print("processing ===>",index)
    return  out

if __name__ == "__main__":
    f = open("randomparas.txt.py")
    huge_text = f.read()

    chunks = huge_text.split("\n")
    for i,chunk in enumerate(chunks):
        # print(f"Para{i} , Score is {score_paragraph(chunk)}")
        score(chunk,i)
    # f.close()
    multitasking.wait_for_tasks()