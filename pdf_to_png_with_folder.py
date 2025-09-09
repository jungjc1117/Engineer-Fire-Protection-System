import os
from pdf2image import convert_from_path
from PIL import Image

def pdf_to_png_with_folder(pdf_path, output_folder):
    """
    PDF 파일을 PNG 이미지로 변환하고, PDF 파일명을 PNG 폴더명으로 사용합니다.

    Args:
        pdf_path (str): 변환할 PDF 파일의 전체 경로.
        output_folder (str): PNG 이미지들을 저장할 최상위 폴더 경로.
    """
    try:
        # PDF 파일명에서 확장자를 제거하여 폴더명으로 사용
        pdf_filename_without_ext = os.path.splitext(os.path.basename(pdf_path))[0]
        # PNG 이미지들을 저장할 특정 폴더 생성
        specific_output_folder = os.path.join(output_folder, pdf_filename_without_ext)

        # 해당 폴더가 없으면 생성
        if not os.path.exists(specific_output_folder):
            os.makedirs(specific_output_folder)
            print(f"폴더 생성: {specific_output_folder}")

        # PDF를 이미지 리스트로 변환 (poppler 설치 필요)
        images = convert_from_path(pdf_path)

        # 각 페이지를 PNG로 저장
        for i, image in enumerate(images):
            png_filename = f"{pdf_filename_without_ext}_page_{i + 1}.png"
            png_path = os.path.join(specific_output_folder, png_filename)
            image.save(png_path, 'PNG')
            print(f"저장 완료: {png_path}")

        print(f"'{pdf_path}' 파일 변환 완료! '{specific_output_folder}'에 저장되었습니다.")

    except FileNotFoundError:
        print(f"오류: PDF 파일을 찾을 수 없습니다. 경로를 확인해주세요: {pdf_path}")
    except Exception as e:
        print(f"변환 중 오류 발생: {e}")

# --- 사용 예시 ---
if __name__ == "__main__":
    # 변환할 PDF 파일 경로 지정
    # 예: 'C:/Users/YourUser/Documents/my_document.pdf' 또는 '/home/user/documents/report.pdf'
    input_pdf_file = '2010년1회.pdf' # 실제 PDF 파일 경로로 변경해주세요.

    # PNG 이미지를 저장할 최상위 폴더 경로 지정
    # 예: 'C:/Users/YourUser/Pictures/Converted_PDFs' 또는 '/home/user/images/pdf_output'
    output_base_folder = '2010년1회-converted' # PNG 파일들이 저장될 기본 폴더명

    # 함수 호출
    pdf_to_png_with_folder(input_pdf_file, output_base_folder)