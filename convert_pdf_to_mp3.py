from gtts import gTTS
import pdfplumber
from pathlib import Path


def pdf_mp3(file_path='test.pdf', language='en'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf': # проверка на расширение pdf и проверка файл is True or False

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf: # открываем файл на чтение в двойчном режиме(rb)
            pages = [page.extract_text() for page in pdf.pages] # проходимся по страницам 
        
        text = ''.join(pages)
        text = text.replace('\n', '')

        my_audio = gTTS(text=text, lang=language, slow=False) # создаем аудио-файл, slow - скорость воспроизведения файла
        file_name = Path(file_path).stem # получаем имя файло с помощью свойства stem
        my_audio.save(f'{file_name}.mp3')

        return f'{file_name}.mp3 saved successfully, thanks for waiting.'
    
    else:
        return "File not exist!"


def main():
    file_path = input("Enter a filr path, example (/Users/apple/Desktop/practice with/file_pdf/sample.pdf): ")
    language = input("Choose language, 'en' or 'ru': " )
    print(pdf_mp3(file_path=file_path, language=language))


if __name__ == "__main__": # используется, чтобы проверить, выполняется ли файл как автаномная программа
    main()

