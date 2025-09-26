import os
from PIL import Image

# 결과 파일명을 '06_1 시퀀스.png'로 통일
OUTPUT_FILENAME = "09 배선·계통도·가닥수 산출(자동화재탐지·수압개폐).png" 

def stitch_images_vertically(folder_path, output_filename=OUTPUT_FILENAME):
    """
    폴더 내 모든 이미지 파일을 읽어와 가장 작은 가로 길이에 맞춰 비례 축소하고,
    그 이미지들을 세로로 이어 붙여 하나의 이미지 파일로 저장합니다.

    Args:
        folder_path (str): 이미지가 들어있는 폴더의 경로.
        output_filename (str): 최종 결과 이미지 파일의 이름 (확장자 포함).
    """
    
    # 1. 지원되는 이미지 확장자 정의
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
    
    # 2. 폴더 내 이미지 파일 경로 목록 가져오기
    image_paths = []
    # os.listdir 대신 os.walk를 사용하여 서브폴더도 포함하거나, glob을 사용하여 간단화할 수 있지만,
    # 기본 요청에 따라 '현재' 폴더만 검사합니다.
    for f in os.listdir(folder_path):
        if f.lower().endswith(valid_extensions):
            image_paths.append(os.path.join(folder_path, f))

    if not image_paths:
        print(f"오류: '{folder_path}' 폴더에서 유효한 이미지 파일을 찾을 수 없습니다.")
        return

    print(f"총 {len(image_paths)}개의 이미지 파일을 찾았습니다.")

    # 3. 모든 이미지 열기 및 가장 작은 가로 길이 찾기
    images = []
    min_width = float('inf') # 무한대로 초기화
    
    for path in image_paths:
        try:
            # RGB 모드로 변환하여 통일성 확보 (알파 채널/투명도 문제 방지)
            img = Image.open(path).convert("RGB") 
            images.append(img)
            if img.width < min_width:
                min_width = img.width
        except Exception as e:
            # 파일이 이미지 형식이 아니거나 손상된 경우 건너뛰기
            print(f"경고: {path} 파일을 여는 중 오류 발생. 스킵합니다. ({e})")
            continue
            
    if not images:
        print("오류: 처리할 수 있는 이미지가 없습니다.")
        return

    print(f"가장 작은 가로 길이 (기준 폭): {min_width} 픽셀")

    # 4. 이미지들을 기준 가로 길이에 맞춰 비례 축소
    resized_images = []
    total_height = 0
    
    for img in images:
        if img.width > min_width:
            # 비례 축소 비율 계산
            ratio = min_width / img.width
            new_height = int(img.height * ratio)
            
            # 이미지 비례 축소 (LANCZOS 필터 사용하여 고품질 다운샘플링)
            resized_img = img.resize((min_width, new_height), Image.Resampling.LANCZOS)
        else:
            # 기준 길이보다 작거나 같으면 그대로 사용
            resized_img = img
            
        resized_images.append(resized_img)
        total_height += resized_img.height

    # 5. 모든 이미지를 세로로 이어 붙일 최종 캔버스 생성
    # 캔버스 크기: (가장 작은 가로 길이, 축소된 이미지들의 총 세로 길이)
    final_image = Image.new('RGB', (min_width, total_height))

    # 6. 캔버스에 이미지 순서대로 붙여넣기
    y_offset = 0
    for img in resized_images:
        final_image.paste(img, (0, y_offset))
        y_offset += img.height # 다음 이미지를 붙일 위치 업데이트
        
    # 7. 결과 이미지 저장
    output_path = os.path.join(folder_path, output_filename)
    # JPEG 품질을 95로 설정하여 고품질 유지
    final_image.save(output_path, quality=95) 
    print(f"\n✅ 성공적으로 이미지를 이어 붙여 저장했습니다: {output_path}")

# --- 사용 예시 ---
if __name__ == '__main__':
    # **중요:** 여기에 이미지들이 들어있는 폴더 경로를 지정하세요.
    folder_to_process = "09 배선·계통도·가닥수 산출(자동화재탐지·수압개폐)" 
    
    # 예시 폴더가 없으면 생성 (테스트용)
    if not os.path.exists(folder_to_process):
        os.makedirs(folder_to_process)
        print(f"'{folder_to_process}' 폴더를 생성했습니다. 여기에 이미지 파일을 넣어주세요.")
    
    # 함수 실행
    # 결과 파일명은 OUTPUT_FILENAME 변수에 의해 "final_stitched_result.jpg"로 저장됩니다.
    stitch_images_vertically(folder_to_process, OUTPUT_FILENAME)