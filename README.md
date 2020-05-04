## Cicada3301

### Описание проекта.
Модель состоит из нескольких частей:
  1. bash-скрипт. Используется для парсинга всех звуков системы. Скрипт позволяет использовать нейросеть в любых приложениях, издающих звук (Zoom, Discord, MS Teams, Skype и так далее).
  2. python-скрипт. Используется для препроцессинга, логгирования сказанного в текст. Функционал скрипта позволяет делать следующие вещи:
  3. jupyter-notebook с туториалами.
  
### Установка.

Для запуска модели на собственной машине, или удаленном сервере требуется сделать следующую последовательность действий:

**Важно**: распознавание нейросети базируется на open-source проекте [vosk](https://github.com/alphacep/vosk-api), поэтому единственная поддерживаемая ОС на данный момент - ***Линукс***.

1. Скачиваем этот репозиторий к себе на  машину

`!git clone https://github.com/danyanyam/notahack.git`

2. Скачиваем веса проекта

  - `!wget http://alphacephei.com/kaldi/models/vosk-model-ru-0.10.zip` - спич2текст

  - `!wget http://alphacephei.com/kaldi/models/vosk-model-spk-0.3.zip` - спич2монологи

3. Разархивируем скаченные веса:

  - `!unzip vosk-model-spk-0.3.zip`

  - `!unzip vosk-model-ru-0.10.zip`




### Использование.
### Credentials.
