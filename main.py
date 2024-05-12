from docx import Document

def read_docx_lines(docx_file):
  doc = Document(docx_file)
  count_of_question = 1
  answer_array = ['a','b','c','d','e']
  right_answer = -1
  count_variant = 0
  error_answer = 0
  for para in doc.paragraphs:
    for line in para.text.splitlines():
      if "<question>"  in line:
        count_variant = 0
        if right_answer !=-1:
          pick_answer = -1
          while(pick_answer == -1):
            pick_answer = input("Введите ваш ответ: ")
            if pick_answer == 'a' or pick_answer == 1:
              pick_answer = 1
            elif pick_answer == 'b' or pick_answer == 2:
              pick_answer = 2
            elif pick_answer == 'c' or pick_answer == 3:
              pick_answer = 3
            elif pick_answer == 'd' or pick_answer == 4:
              pick_answer = 4
            else:
              print('DONT UNDESTAND')
              pick_answer = -1
          if pick_answer != right_answer:
            error_answer +=1
            print('Wrong answer You have ' + str(3-error_answer) + ' heart correct answer = ' + answer_array[right_answer-1])
            if error_answer == 3:
              print('YOU LOSE!! YOU LOSS 3 HEART.')
              return
          else:
            print('RIGHT!')
        print(str(count_of_question) + line.replace("<question>",''))
        count_of_question+=1
      else:
        if "<variant>" in line:
          print(answer_array[count_variant] + line.replace("<variant>",''))
          count_variant+=1
        if "<variantright>" in line:
          print(answer_array[count_variant] + line.replace("<variantright>", ''))
          count_variant += 1
          right_answer = count_variant

if __name__ == "__main__":
  file_path = "Психология.docx"
  read_docx_lines(file_path)