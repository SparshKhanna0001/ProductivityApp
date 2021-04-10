def txt_file_parser(path: str,score: float) -> list:
    """WHAT IT DOES
        1. will add recent score and delete the oldest
        2. parse strings(type of data enetered) from .txt file and convert it into list .
    """
    
    file = open(path,"r")
    data = file.read()
    file.close()
    scores = data.split(",")
    scores[0] = 0
    scores.append(score)
    return scores


def txt_file_editor(scores: list,path: str) -> None:
    
    file = open(path, "w")
    new_data = scores[1]
    
    for score in scores[2:]:
        new_data= "," + score
        
    file.write(new_data)
    file.close()
    
    
def seven_day_scorer(scores: list) -> float:
    
    seven_day_score = 0
    
    for score in scores[1:]:
        seven_day_score += score
        avg_7_day_score = seven_day_score/7
        
    return avg_7_day_score

