def generate_paragraph(row):
    sentences = []
    if row.get('full_name') and row.get('title') and row.get('company'):
        sentences.append(f"{row['full_name']}, currently working as {row['title']} at {row['company']}.")
    if row.get('location'):
        sentences[-1] += f" They are based in {row['location']}."
    if row.get('company_description'):
        sentences.append(f"{row['company']} specializes in {row['company_description']}.")
    if row.get('skills'):
        sentences.append(f"Their skills include: {row['skills']}.")
    if row.get('education'):
        sentences.append(f"Their educational background includes: {row['education']}.")
    if row.get('work_history'):
        sentences.append(f"They have worked in roles such as: {row['work_history']}.")
    return " ".join(sentences)

def generate_advertising_paragraph(row):
    sentences = []
    if row.get('full_name') and row.get('title') and row.get('company'):
        sentences.append(f"{row['full_name']} is the {row['title']} at {row['company']}.")
    if row.get('skills'):
        sentences.append(f"Key skills include: {row['skills']}.")
    if row.get('work_history'):
        sentences.append(f"Past work includes roles such as: {row['work_history']}.")
    return " ".join(sentences)
