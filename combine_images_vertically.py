import os
from PIL import Image

def get_image_list(folder_path):
    """
    폴더 안의 모든 이미지 파일 경로를 리스트로 반환합니다.
    (PNG, JPG, JPEG, GIF, BMP 확장자 지원)
    """
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
    return sorted([
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.lower().endswith(image_extensions)
    ])

def stitch_images_vertically(folder_path, output_path):
    """
    지정된 폴더 안의 이미지들을 세로로 이어붙여 저장합니다.
    모든 이미지는 첫 번째 이미지의 가로 크기에 맞춰 리사이즈됩니다.
    """
    image_paths = get_image_list(folder_path)

    if not image_paths:
        print(f"'{folder_path}' 폴더에 이미지가 없습니다.")
        return

    # 첫 번째 이미지 로드 및 가로 크기(width)와 세로 크기(height)를 가져옵니다.
    first_image = Image.open(image_paths[0])
    target_width, _ = first_image.size

    # 병합될 이미지들의 총 세로 길이(total_height)를 계산합니다.
    total_height = 0
    resized_images = []
    for path in image_paths:
        img = Image.open(path)
        
        # 첫 번째 이미지의 가로 길이에 맞춰 비율을 유지하며 리사이즈합니다.
        if img.width != target_width:
            img = img.resize((target_width, int(img.height * target_width / img.width)), Image.LANCZOS)
        
        resized_images.append(img)
        total_height += img.height

    # 모든 이미지를 담을 빈 이미지를 생성합니다.
    merged_image = Image.new('RGB', (target_width, total_height))

    # 이미지를 세로로 이어붙입니다.
    y_offset = 0
    for img in resized_images:
        merged_image.paste(img, (0, y_offset))
        y_offset += img.height

    # 병합된 이미지를 저장합니다.
    merged_image.save(output_path)
    print(f"이미지 병합이 완료되었습니다. 결과: '{output_path}'")

# --- 사용 예시 ---
# 이미지가 있는 폴더 경로와 최종 결과물이 저장될 경로를 지정하세요.
input_folder = "새 폴더"  # 이미지들이 있는 폴더
# output_file = os.path.join(input_folder, "2010년1회.png")
output_file = "2020년2회.png"

# 함수 실행
stitch_images_vertically(input_folder, output_file)