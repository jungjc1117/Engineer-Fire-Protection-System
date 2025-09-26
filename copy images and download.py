import shutil
import os
from bs4 import BeautifulSoup

def copy_and_rename_images_from_file(html_file_path, destination_folder):
    """
    HTML 파일 경로를 받아, 파일 내의 이미지 태그를 찾아 이미지를 복사하고 이름을 변경합니다.
    경로 구분자(₩ 또는 /)를 모두 올바르게 처리하고, 경로 끝의 공백을 제거합니다.
    """
    if not os.path.exists(html_file_path):
        print(f"오류: HTML 파일을 찾을 수 없습니다: '{html_file_path}'")
        return

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        soup = BeautifulSoup(html_content, 'html.parser')
        img_tags = soup.find_all('img')

        html_directory = os.path.dirname(os.path.abspath(html_file_path))

        for i, img in enumerate(img_tags, 1):
            src = img.get('src')
            if src:
                # 경로 문자열 양 끝의 공백과 줄 바꿈 문자를 제거
                src = src.strip()
                
                # 경로에 포함된 모든 역슬래시를 정방향 슬래시로 통일
                src = src.replace('\\', '/')
                
                # './'로 시작하는 상대 경로를 올바르게 처리
                if src.startswith(('./', '.\\')):
                    src = src[2:]

                # 절대 경로 생성
                source_path = os.path.normpath(os.path.join(html_directory, src))

                # 기존 파일명 추출 (예: '2018년1회_04.png')
                original_file_name = os.path.basename(src)
                
                # 새 파일 이름 생성 (예: '01 2018년1회_04.png')
                new_file_name = f"{i:02d} {original_file_name}"
                
                # 최종 목적지 경로
                destination_path = os.path.join(destination_folder, new_file_name)

                try:
                    shutil.copy(source_path, destination_path)
                    print(f"성공: '{source_path}' -> '{destination_path}'")
                except FileNotFoundError:
                    print(f"오류: 파일을 찾을 수 없습니다: '{source_path}'")
                except Exception as e:
                    print(f"오류: 파일 복사 중 문제가 발생했습니다: {e}")

    except Exception as e:
        print(f"예기치 않은 오류가 발생했습니다: {e}")

# ---
### 사용 예시

# HTML 파일 경로와 이미지를 저장할 폴더를 지정합니다.
html_file = '13 피난구유도등·전류계산·가스누설경보기.html'
output_folder = "13 피난구유도등·전류계산·가스누설경보기"

# 함수 실행
copy_and_rename_images_from_file(html_file, output_folder)
