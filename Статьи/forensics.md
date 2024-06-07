## Утилиты для стеганографии
*****************************************************************
## Первичный анализ:

Простые утилиты, очень часто работают с ошибками, но очень выручают :) 

|Утилита|Описание|Пример|
|-----|-------------|-------|
|file|Определет тип файла|file _filename_|
|exiftool|Посмотреть основные метаданные |exiftool _filename_ |
|binwalk|Показывает встроенные контейнеры| binwalk _filename_ |
|strings | Показывает все текстовые строки | strings _filename_ |
|foremost | Извлекает встроенные контейнеры | foremost _filename_ |
|pngcheck | Проверяет файлы формата PNG | pngcheck _filename_ |
|ffmpeg | Проверяет целостность аудио файлов | ffmpeg -i _filename_ _output_ |

## Утилиты для поиска стеганографии

Набор утилит, который помогает искать закладки. Используем поочередно и внимательно изучаем результат.

| Утилита | Поддерживаемые типы файлов | Описание | Пример | 
|------|----------------------|-------|-------|
|zsteg | PNG,BMP | Раскладывает файл по каналам | zsteg _filename_|
|stegdetect| JPG |  | stegdetect _filename_ |
|stegbreak | JPG |  | stegbreak -t o -f wordlist.txt _filename_|
|stegsolve | All image format |  | java -jar stegsolve |

*Detail is mentioned below*
**First install the jar package of stegsolve and then use it as follows: [java -jar stegsolve] in Terminal.**

## Стеганографические утилиты

Эти утилиты могут как прятать, так и находить сообщения, но только СВОИ. 

| Утилиты | Поддерживаемые типы файлов| Спрятать | Извлечь |
|------|---------------------|--------|------------|
|Jsteg | JPG |  jsteg hide _hide.jpg_ secret.txt _filename_ | jsteg reveal _hide.jpg_ output.txt
|OpenStego| PNG | openstego embed -mf secret.txt -cf _hide.png_ -p password -sf stego.png | openstego extract -sf openstego.png -p ab12 -xf output.txt|
|Outguess| JPG | outguess -k password -d secret.txt cover.jpg stego.jpg | outguess -r -k password stego.jpg output.txt |
|Steghide| JPG,BMP,WAV | steghide embed -f -ef secret.txt -cf cover.jpg -p password -sf stego.jpg | steghide extract -sf stego.jpg -p password -xf output.txt | 
|LSBSteg| PNG,BMP | LSBSteg encode -i cover.png -o stego.png -f secret.txt | LSBSteg decode -i stego.png -o output.txt |
|mp3stego|Audio files| mp3stego-encode -E secret.txt -P password cover.wav stego.mp3 | mp3stego-decode -X -P password stego.mp3 out.txt | 
|AudioStego| Audio files| hideme cover.mp3 secret.txt && mv ./output.mp3 stego.mp3 | hideme stego.mp3 -f && cat output.txt|
|stegano|PNG| stegano-lsb hide --input cover.jpg -f secret.txt -e UTF-8 --output stego.png or stegano-red hide --input cover.png -m "secret msg" --output stego.png or stegano-lsb-set hide --input cover.png -f secret.txt -e UTF-8 -g $GENERATOR --output stego.png for various generators (stegano-lsb-set list-generators)| stegano-lsb reveal -i stego.png -e UTF-8 -o output.txt or stegano-red reveal -i stego.png or stegano-lsb-set reveal -i stego.png -e UTF-8 -g $GENERATOR -o output.txt|


## Утилиты для работы с аудио файлами

| Tool | Description | Usage|
|------|-------------|------|
|Audacity| Наверное, лучшая утилита для работы со звуком | audacity -filename| 
|Sonic Visualiser| Еще одна подобная утилита| sonic-visualiser -filename|
|Deepsound| Прячет под паролем информацию в звуке| Только для Windows |

## Утилита для анализа дампов памяти

Volatility - это программа № 1 в области анализа памяти!!!
Устанавливается она очень просто: **sudo apt-get install volatility**
Чуть попозже здесь или в отдельной статье будет небольшое руководство по решению задач с ее помощью.

## Утилиты для анализа сетевой активности:

|Утилита| Описание | Использование|
|----|-------------|------|
|Wireshark| Wireshark Лучший анализатор пакетов (GUI), есть библиотека для питона tshark | wireshark filename.pcap|
|Tcpdump| консольная версия для анализа пакетов | tcpdump -options |
|Network Miner| NetworkMiner это Network Forensic Analysis Tool (NFAT) для Windows. | GUI application|

## Утилиты для анализа образов дисков:

| Утилита | Описание | Использование |
|------|-------------|-------|
|Fdisk| Утилита для работы с разделами. **ВАЖНО**: очень аккуратно с ней | fdsik -lu filename|
|TestDisk| Утилита для восстановления данных | testdisk filename|
|Autopsy| Утилита № 1 для работы с дисками в форензике | GUI Application|
|OSForensics| Аналогично :)  | GUI Application | 







  