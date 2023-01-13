def ave_size(all_data: str) -> str:
    """
      Use ONLY with defined structured data
    :param all_data: file info with height & weight in inches & pounds
    :return: average height and weight HTML type
    """
    el = all_data.replace("\n", ",").split(",")[3:]
    total = len(el) / 3
    
    all_heights = [float(el[i]) for i in range(1, len(el), 3) if el[i]]
    avg_height = round(inch_to_cm(sum(all_heights) / total))
    
    all_weights = [float(el[i]) for i in range(2, len(el), 3) if el[i]]
    avg_weight = round(pound_to_kg(sum(all_weights) / total))
    
    return f"Avg Height - {str(avg_height)} cm <br >" \
           f"Avg Weight - {str(avg_weight)} kg"


def inch_to_cm(inch: int | float) -> float:
    return inch * 2.54


def pound_to_kg(pound: int | float) -> float:
    return pound * 0.453592


def ave_size_universal(all_data: str) -> str:
    """
      Universal way to read lines and calculate data. More stable
    than ave_size if not all data available (missed weight or height)
    :param all_data: file info with height & weight in inches & pounds
    :return: average height and weight HTML type
    """
    lines = all_data.split("\n")
    total_students, total_height, total_weight = 0, 0, 0
    
    for line in lines:
        attributes = line.split(",")
        
        # We must be sure that all data is correct before count it
        try:
            height = float(attributes[1])
            weight = float(attributes[2])
        except (TypeError, IndexError, ValueError):
            # If not - just skip it
            continue
        
        total_students += 1
        total_height += height
        total_weight += weight
    
    avg_height = round(inch_to_cm(total_height) / total_students)
    avg_weight = round(pound_to_kg(total_weight) / total_students)
    
    return f"Avg Height - {str(avg_height)} cm <br >" \
           f"Avg Weight - {str(avg_weight)} kg"
