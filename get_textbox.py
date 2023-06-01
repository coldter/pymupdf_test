import fitz

doc = fitz.open("input.pdf")

page = doc[0]

"""
expecting this to return --> Our business continuity plan
but gets -->Our plan
Our business continuity plan
customers, employees, and reg
"""
rect = fitz.Rect(43.333333015441895, 139, 131.3333330154419, 146)

extracted_text = page.get_textbox(rect)
print("extracted_text -->", extracted_text)

# mark the page with the rectangle
page.draw_rect(rect, color=(1, 0, 0), overlay=False, width=1.5, fill_opacity=1)
new_doc = fitz.open()
new_doc.insert_pdf(doc, from_page=0, to_page=0)
new_doc.ez_save("output.pdf")
