from calendar import c
import json
from re import L
from fpdf import FPDF

# read json
with open('PERSONALDETAILS.json', 'r') as json_data:
    data = json.load(json_data)

#create pdf
pdf = FPDF('P', 'mm', 'Letter')
pdf.add_page()

#insert image
pdf.image("id.jpg", 11, 17, 38.1,)

# adding data from personaldetails.json

    #insert name, address, contact number, email address, and github acc 
pdf.set_font("times", "", 26)
pdf.cell(0, 15, ln = 1)
pdf.cell(180, 7, data['name'], ln = 1, align = 'C')

pdf.set_font("times", "B", 12)
pdf.cell(104, 7, "Address: ", align = 'C')
pdf.set_font("times", "", 12)
pdf.cell(37, 7, data['address'], ln = 1, align = 'C')

pdf.set_font("times", "B", 12)
pdf.cell(120, 1, "Contact Number: ", align = 'C')
pdf.set_font("times", "", 12)
pdf.cell(-62, 1, data['contact_num'], ln = 1, align = 'C')

pdf.set_font("times", "B", 12)
pdf.cell(116, 6, "Email Address: ", align = 'C')
pdf.set_font("times", "", 12)
pdf.cell(-33, 6, data['email'], ln = 1, align = 'C')
pdf.set_font("times", "B", 12)

pdf.cell(118, 2, "Github Account: ", align = 'C')
pdf.set_font("times", "", 12)
pdf.cell(-63, 2, data['github'], ln = 1, align = 'C')

    #insert career aim
pdf.cell(-17, -17, ln = 1)
pdf.set_text_color(r = 0, g = 140, b = 140)
pdf.set_font("times", "BU", 12)
pdf.cell(0, 55, "CAREER AIM:", ln = 1, align = 'L')

pdf.set_text_color(r = 0, g = 0, b = 0)
pdf.set_font("times", "", 12)
pdf.cell(15, 0)
pdf.cell(0, -41, data['career_aim'][0], ln = 1, align = 'L')
pdf.cell(11, 0)
pdf.cell(0, 48, data['career_aim'][1], ln = 1, align = 'L')
pdf.cell(11, 0)
pdf.cell(0, -40, data['career_aim'][2], ln = 1, align = 'L')

    #insert personal data such as birth of date, age, marital status, gender, religion and citizenship
pdf.set_text_color(r = 0, g = 140, b = 140)
pdf.set_font("times", "BU", 12)
pdf.cell(0, 55, "PERSONAL DATA:", ln = 1, align = 'L')

pdf.set_text_color(r = 0, g = 0, b = 0)
pdf.cell(15, 0)
pdf.set_font("times", "B", 12)
pdf.cell(35, -39, "Date of Birth", align = 'L')
pdf.set_font("times", "", 12)
pdf.cell(0, -39, data['birthdate'], ln = 1, align = 'L')

pdf.set_font("times", "B", 12)
pdf.cell(15, 0)
pdf.cell(35, 48, "Age", align = 'L')
pdf.set_font("times", "", 12)
pdf.cell(0, 48, data['age'], ln = 1, align = 'L')

pdf.set_font("times", "B", 12)
pdf.cell(15, 0)
pdf.cell(35, -38, "Marital Status", align = 'L')
pdf.set_font("times", "", 12)
pdf.cell(0, -38, data['marital_status'], ln = 1, align = 'L')

pdf.set_font("times", "B", 12)
pdf.cell(15, 0)
pdf.cell(35, 46, "Gender", align = 'L')
pdf.set_font("times", "", 12)
pdf.cell(0, 46, data['gender'], ln = 1, align = 'L')

pdf.set_font("times", "B", 12)
pdf.cell(15, 0)
pdf.cell(35, -37, "Religion", align = 'L')
pdf.set_font("times", "", 12)
pdf.cell(0, -37, data['religion'], ln = 1, align = 'L')

pdf.set_font("times", "B", 12)
pdf.cell(15, 0)
pdf.cell(35, 46, "Citizenship", align = 'L')
pdf.set_font("times", "", 12)
pdf.cell(0, 46, data['citizenship'], ln = 1, align = 'L')

    #insert educational background
pdf.set_text_color(r = 0, g = 140, b = 140)
pdf.set_font("times", "BU", 12)
pdf.cell(0, -30, "EDUCATIONAL BACKGROUND:", ln = 1, align = 'L')

pdf.set_text_color(r = 0, g = 0, b = 0)
pdf.set_font("times", "B", 12)
pdf.cell(35, 45.5, data["senior_high"], ln = 1, align = 'L')
pdf.set_font("times", "I", 12)
pdf.cell(35, -37.5, data['senior_high_desc'][0], ln = 1, align = 'L')
pdf.cell(35, 45.5, data['senior_high_desc'][1], ln = 1, align = 'L')

pdf.set_font("times", "B", 12)
pdf.cell(35, -34.5, data["college"], ln = 1, align = 'L')
pdf.set_font("times", "I", 12)
pdf.cell(35, 42.5, data['college_desc'][0], ln = 1, align = 'L')
pdf.cell(35, -33.5, data['college_desc'][1], ln = 1, align = 'L')

    #insert soft skills
pdf.set_text_color(r = 0, g = 140, b = 140)
pdf.set_font("times", "BU", 12)
pdf.cell(0, 50, "SOFT SKILLS:", ln = 1, align = 'L')

pdf.set_text_color(r = 0, g = 0, b = 0)
pdf.set_font("times", "", 12)
pdf.cell(35, -34.5, data["soft_skills"][0], ln = 1, align = 'L')
pdf.cell(35, 42.5, data["soft_skills"][1], ln = 1, align = 'L')
pdf.cell(35, -34.5, data["soft_skills"][2], ln = 1, align = 'L')
pdf.cell(35, 42.5, data["soft_skills"][3], ln = 1, align = 'L')
pdf.cell(35, -34.5, data["soft_skills"][4], ln = 1, align = 'L')
pdf.cell(35, 42.5, data["soft_skills"][5], ln = 1, align = 'L')

    #insert hard skills
pdf.set_text_color(r = 0, g = 140, b = 140)
pdf.set_font("times", "BU", 12)
pdf.cell(0, -28, "HARD SKILLS:", ln = 1, align = 'L')

pdf.set_text_color(r = 0, g = 0, b = 0)
pdf.set_font("times", "", 12)
pdf.cell(35, 42.5, data["hard_skills"][0], ln = 1, align = 'L')
pdf.cell(35, -34.5, data["hard_skills"][1], ln = 1, align = 'L')
pdf.cell(35, 42.5, data["hard_skills"][2], ln = 1, align = 'L')
pdf.cell(35, -34.5, data["hard_skills"][3], ln = 1, align = 'L')

    #insert achievements and awards
pdf.set_text_color(r = 0, g = 140, b = 140)
pdf.set_font("times", "BU", 12)
pdf.cell(0, 50, "ACHIEVEMENTS/AWARDS:", ln = 1, align = 'L')
pdf.set_text_color(r = 0, g = 0, b = 0)
pdf.set_font("times", "", 12)
pdf.cell(35, -34.5, data["achievements_awards"][0], ln = 1, align = 'L')
pdf.cell(35, 42.5, data["achievements_awards"][1], ln = 1, align = 'L')


# pdf maker
pdf.output('FLORIDO_GIAN-GREGORIO.pdf')