## Cicada3301


### Описание проекта
Проект состоит из нескольких частей:
  1. bash-скрипты. Используются для парсинга всех звуков системы. Скрипт позволяет использовать нейросеть в любых приложениях, издающих звук (Zoom, Discord, MS Teams, Skype и так далее)
  2. python-скрипты. Используются для препроцессинга, логгирования сказанного в текст
  3. jupyter-notebook с туториалом [tutorial.ipynb](https://github.com/danyanyam/notahack/blob/master/tutorial.ipynb)
  4. [log.txt](https://github.com/danyanyam/notahack/blob/master/log.txt) - файл формата выходного файла

**[Видео](https://youtu.be/0AvAGU5cs4E) с примером использования:**
[![Видео с использованием](https://i.imgur.com/MsJFLnB.png)](https://youtu.be/0AvAGU5cs4E)
### Установка

Для запуска модели на собственной машине, или удаленном сервере требуется сделать следующую последовательность действий:

**Важно**: распознавание нейросети базируется на open-source проекте [vosk](https://github.com/alphacep/vosk-api), поэтому единственная поддерживаемая ОС на данный момент - **UBUNTU 18.04/LINUX**.

1. Скачиваем этот репозиторий к себе на сервер/локальный компьютер

- `!git clone https://github.com/danyanyam/notahack.git`

- `cd notahack`

2. Скачиваем веса проекта

  - `!wget http://alphacephei.com/kaldi/models/vosk-model-ru-0.10.zip` - спич2текст

  - `!wget http://alphacephei.com/kaldi/models/vosk-model-spk-0.3.zip` - спич2монологи

3. Разархивируем скаченные веса

  - `!unzip vosk-model-spk-0.3.zip`

  - `!unzip vosk-model-ru-0.10.zip`

### Использование

1. В терминале ввести `sudo chmod +x record.sh`

2. Запускаем запись `./record.sh`

3. После окончания беседы используется комбинация CTRL-C

4. Далее идет автоматическая предобработка записи и конвертация в необходимый для нейронной сети формат

5. Нейронная сеть автоматически считывает входную запись и создает файл `log.txt`, содержащий распознанный текст

6. Файл `ffmpeg_output.wav` содержит запись беседы

