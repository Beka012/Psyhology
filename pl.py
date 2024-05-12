from docx import Document

def read_docx_lines(docx_file,question_number=1):
  doc = Document(docx_file)
  answer_array = ['a', 'b', 'c', 'd']
  count_variant = 0
  right_answer = -1
  error_answer = 0
  counts_varinat_skipped = 0
  for para in doc.paragraphs:
    for line in para.text.splitlines():
      if question_number !=1:
        if "variant" in line:
          counts_varinat_skipped+=1
          if(counts_varinat_skipped==4):
            counts_varinat_skipped =0
            question_number-=1
          continue
      if "variant" not in line:
          count_variant=0
          if right_answer != -1:
            pick_answer = -1
            while (pick_answer == -1):
              pick_answer = input("Введите ваш ответ: ")
              if pick_answer == 'a' or pick_answer == 1:
                pick_answer = 1
                right_answer = -1
              elif pick_answer == 'b' or pick_answer == 2:
                pick_answer = 2
                right_answer = -1
              elif pick_answer == 'c' or pick_answer == 3:
                pick_answer = 3
                right_answer = -1
              elif pick_answer == 'd' or pick_answer == 4:
                pick_answer = 4
                right_answer = -1
              else:
                print('DONT UNDESTAND')
                pick_answer = -1
            if pick_answer != right_answer:
              error_answer += 1
              print('Wrong answer You have ' + str(3 - error_answer) + ' heart correct answer = ' + answer_array[
                right_answer - 1])
              if error_answer == 3:
                print('YOU LOSE!! YOU LOSS 3 HEART.')
                return
            else:
              print('RIGHT!')
          print(line)
      if "<variant>" in line:
        print(answer_array[count_variant]+line.replace("<variant>", '.'))
        count_variant+=1
      if "<variantright>" i
      n line:
        print(answer_array[count_variant]+line.replace("<variantright>", '.'))
        count_variant+=1
        right_answer = count_variant

if __name__ == "__main__":
  file_path = "Sql база  LEGENDARY.docx"
  read_docx_lines(file_path)