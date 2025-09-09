from PIL import Image
import os

def print_max_image_height(folder_path):
    """
    지정된 폴더 내 모든 이미지 파일의 높이 중 가장 큰 값을 출력하는 함수

    Args:
        folder_path (str): 이미지가 저장된 폴더의 경로
    """
    
    # 지원하는 이미지 파일 확장자 목록
    supported_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
    image_heights = [] # 모든 이미지의 높이를 저장할 리스트

    # 폴더가 존재하는지 확인
    if not os.path.isdir(folder_path):
        print(f"오류: '{folder_path}' 폴더를 찾을 수 없습니다.")
        return

    # 폴더 내 파일 목록을 순회
    for filename in os.listdir(folder_path):
        # 파일 확장자가 이미지인지 확인 (대소문자 무시)
        if filename.lower().endswith(supported_extensions):
            file_path = os.path.join(folder_path, filename)
            
            try:
                # Pillow를 사용해 이미지 열기
                with Image.open(file_path) as img:
                    width, height = img.size
                    image_heights.append(height) # 이미지 높이를 리스트에 추가
                    
            except Exception as e:
                print(f"오류: {filename} 파일을 여는 중 오류가 발생했습니다. ({e})")

    # 이미지 높이 리스트가 비어있지 않으면 최대 높이 계산
    if image_heights:
        max_height = max(image_heights)
        print(f"폴더 내 이미지들의 최대 세로 길이: {max_height}px")
    else:
        print(f"'{folder_path}' 폴더에서 유효한 이미지 파일을 찾을 수 없습니다.")

# 사용 예시: '새폴더-1'이라는 폴더에 이미지가 있다고 가정
image_folder = 'images-trimmed-1'  # 이 경로를 실제 이미지 폴더 경로로 변경하세요
print_max_image_height(image_folder)