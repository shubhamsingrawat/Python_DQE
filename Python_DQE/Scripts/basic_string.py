str_value ="""
 tHis iz your homeWork, copy these Text to variable.

 You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

line_list = str_value.splitlines()

#trimming the extra space
line_trim = [line.strip() for line in line_list if line != '']

#converting every thing to lower case
line_lower_case = [line.lower() for line in line_trim]
#print(line_lower_case)

#converting every line to capitalize
line_capitalize = [line.capitalize() for line in line_lower_case]
print(line_capitalize)

#replacing the "iz" with "is"
line_corrected = [line.replace('iz','is') for line in line_capitalize]
#print(line_corrected)

#current paragraph
current_paragraph = ''.join([line for line in line_corrected])
#print(current_paragraph)
"""
This is your homework, copy these text to variable.
You need to normalise it from letter cases point of view. 
also, create one more sentence with last words of each 
existing sentence and add it to the end of this paragraph.
It is misspelling here. 
fix“is” with correct “is”, but only when it is a mistake.
Last is to calculate number of whitespace characters in this tex. 
carefull, not only spaces, but all whitespaces. i got 87.
"""
one_more_sentence = ''.join([line.split(" ")[-1] for line in line_corrected])
extra_line = one_more_sentence.replace('.',' ').rstrip()
final_para = current_paragraph + extra_line+'.'

print(final_para)

# count the space
count = 0
for i in str_value:
    if i == ' ' or i == '\n':
        count += 1
print(count)

