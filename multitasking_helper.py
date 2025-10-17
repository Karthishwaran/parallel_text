import multitasking
from sentiment_analysis import score_paragraph
@multitasking.task
def score(chunk_data,index):
    out=score_paragraph(chunk_data)
    print("processing===>",index)
    return out
if _name=='main_':
    with open("TPG_Democracy_in_America.txt","r",encoding="utf-8") as f:
        huge_text = f.read()
        chunks = huge_text.split("\n")
        for i,chunk in enumerate(chunks):
            score(chunk,i)
    multitasking.wait_for_tasks()

