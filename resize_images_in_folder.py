import os
from PIL import Image

def resize_images_in_folder(input_folder, output_folder, target_width):
    """
    폴더 내 모든 이미지들의 가로 길이를 지정된 픽셀로 변경하고,
    비율에 맞춰 세로 길이를 자동으로 조절하여 다른 폴더에 저장합니다.

    Args:
        input_folder (str): 원본 이미지가 들어있는 폴더의 경로.
        output_folder (str): 리사이즈된 이미지를 저장할 폴더의 경로.
        target_width (int): 변경하고 싶은 가로 길이 (픽셀).
    """
    if not os.path.isdir(input_folder):
        print(f"오류: 원본 폴더 '{input_folder}'를 찾을 수 없습니다.")
        return

    # 출력 폴더가 존재하지 않으면 생성합니다.
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"새로운 폴더 '{output_folder}'가 생성되었습니다.")

    # 지원하는 이미지 확장자
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(image_extensions)]

    if not image_files:
        print(f"'{input_folder}' 폴더에 이미지 파일이 없습니다.")
        return

    print(f"'{input_folder}' 폴더 내 이미지들을 {target_width}px로 리사이즈하여 '{output_folder}'에 저장합니다...")

    for image_file in image_files:
        original_path = os.path.join(input_folder, image_file)
        
        try:
            with Image.open(original_path) as img:
                original_width, original_height = img.size
                
                # 새로운 높이 계산 (비율 유지)
                new_height = int(original_height * (target_width / original_width))
                
                # 이미지 리사이즈
                resized_img = img.resize((target_width, new_height), Image.LANCZOS)
                
                # 새로운 폴더에 저장
                new_path = os.path.join(output_folder, image_file)
                resized_img.save(new_path)
                print(f"'{image_file}' 리사이즈 완료: {original_width}x{original_height} -> {target_width}x{new_height}")

        except Exception as e:
            print(f"'{image_file}' 처리 중 오류 발생: {e}")

# --- 사용 예시 ---
# 1. 원본 이미지가 있는 폴더 경로를 지정하세요.
input_folder = "images-trimmed"

# 2. 리사이즈된 이미지를 저장할 폴더 경로를 지정하세요.
# (원본 폴더 안에 'resized'라는 새 폴더를 만듭니다.)
output_folder = "images-trimmed-1"

# 3. 원하는 가로 길이를 픽셀 단위로 지정하세요.
desired_width = 1433

# 4. 함수 실행
resize_images_in_folder(input_folder, output_folder, desired_width)