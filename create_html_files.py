import os

def create_html_files(file_names):
  """
  주어진 이름들로 HTML 파일을 생성합니다.

  Args:
    file_names: 생성할 HTML 파일 이름들의 리스트.
  """
  for name in file_names:
    file_path = f"{name}.html" # 파일 이름에 .html 확장자 추가
    try:
      with open(file_path, 'w', encoding='utf-8') as f:
        # 필요하다면 HTML 기본 구조를 파일에 쓸 수 있습니다.
        f.write("<!DOCTYPE html>\n")
        f.write("<html lang=\"ko\">\n")
        f.write("<head>\n")
        f.write(f"  <meta charset=\"UTF-8\">\n")
        f.write(f"  <title>{name}</title>
  <style>
    /* 테이블 셀에 flex를 적용하여 이미지와 체크박스를 정렬합니다. */
    td {
      display: flex;
      align-items: center;
    }
    img {
      margin-right: 10px;
    }
    #srcList {
      width: 100%;
      height: 200px;
      margin-top: 20px;
      box-sizing: border-box;
    }
    .button-container {
      margin-top: 10px;
      display: flex;
      gap: 10px;
    }
    .button-container button {
      padding: 8px 16px;
      cursor: pointer;
    }
  </style>\n")
        f.write("</head>\n")
        f.write("<body>\n")
        f.write(f"  <h1>{name}</h1>

  <table border="1">
<thead>
      <tr>
        <th>문제</th>
        <th>체크</th>
 
     </tr>
    </thead>
    <tbody>
      <tr>
        <td>\n")
        f.write("</body>\n")
        f.write("</html>")
      print(f"'{file_path}' 파일을 성공적으로 만들었습니다.")
    except FileExistsError:
      print(f"'{file_path}' 파일이 이미 존재합니다.")
    except OSError as e:
      print(f"'{file_path}' 파일을 만드는 중 오류가 발생했습니다: {e}")

# --- 사용 예시 ---
if __name__ == "__main__":
  my_html_files = [
    "2010년1회", "2010년2회", "2010년4회",
    "2011년1회", "2011년2회", "2011년4회",
    "2012년1회", "2012년2회", "2012년4회",
    "2013년1회", "2013년2회", "2013년4회",
    "2014년1회", "2014년2회", "2014년4회",
    "2015년1회", "2015년2회", "2015년4회",
    "2016년1회", "2016년2회", "2016년4회",
    "2017년1회", "2017년2회", "2017년4회",
    "2018년1회", "2018년2회", "2018년4회",
    "2019년1회", "2019년2회", "2019년4회",
    "2020년1회", "2020년2회", "2020년3회", "2020년4회", "2020년5회",
    "2021년1회", "2021년2회", "2021년4회",
    "2022년1회", "2022년2회", "2022년4회",
    "2023년1회", "2023년2회", "2023년4회",
    "2024년1회", "2024년2회", "2024년3회",
  ] # 원하는 파일 이름을 여기에 추가하세요!
  create_html_files(my_html_files)