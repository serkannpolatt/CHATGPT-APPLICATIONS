## English
## Therapist Chat Bot - with Gradio and OpenAI

This project focuses on libraries of a simple therapist chatbot using OpenAI GPT-3.5 Turbo for user interface and speech using Gradio outputs. Users can be carried by bot using microphone.

### Purpose

This project aims to gain experience in artificial intelligence and voice user interests and to create an understandable, responsive chatbot. Also learned how to develop in a real-time chatbook using the OpenAI GPT-3.5 Turbo API.

### Project Components

**1. therapist.py**

This script generates Gradio outputs and determines the transcriptions. transcription function, the use of the following use:

- Takes the user's audio file as input and follows these steps:
- Changes to the '.wav' extension of the name of the audio file.
- Transmits audio features using OpenAI's Whisper ASR (openai.Audio.transcribe).
- Adds the transcript as a user message with the messages it contains.
- sends list of messages to OpenAI's GPT-3.5 Turbo chat model (openai.ChatCompletion.create).
- Adds the model's response as system message messages.
- reads the system message aloud using the subprocess module (restriction, for macOS).
- Creates chat compilations by combining user and therapist messages.

**2.config.py**

This file contains your OpenAI API key. Please describe your real API key instead of 'YOUR_OPENAI_API_KEY' Authenticate with OpenAI API.

### Additional Notes

- A stable internet connection is required to use the OpenAI GPT-3.5 Turbo API.
- To read the system message aloud, Windows users use a different command depending on the system's ability to read the text aloud.

You can warn for special use or different projects by examining and changing the codes.

If you encounter any problems or issues, you can refer to the Gradio and OpenAI documentation.


## Türkçe
## Terapist Sohbet Botu - Gradio ve OpenAI ile

Bu proje, Gradio arayüzünü kullanarak kullanıcı arayüzü ve konuşma için OpenAI GPT-3.5 Turbo'yu kullanarak basit bir terapist sohbet botunun oluşturulması üzerine odaklanmaktadır. Kullanıcılar mikrofon kullanarak bot ile etkileşime geçebilirler.

### Amaç

Bu proje, yapay zeka ve sesli kullanıcı arayüzleri konusunda deneyim kazanma ve anlamlandırılabilir, duyarlı bir sohbet botu oluşturma amacı gütmektedir. Ayrıca, OpenAI GPT-3.5 Turbo API'sini kullanarak gerçek zamanlı bir sohbet uygulamasının nasıl geliştirileceği öğrenilmiştir.

### Proje Bileşenleri

**1. therapist.py**

Bu betik, Gradio arayüzünü oluşturur ve transcribe işlevini tanımlar. transcribe işlevi, aşağıdaki adımları gerçekleştirir:

- Kullanıcının ses dosyasını girdi olarak alır ve şu adımları takip eder:
	- Ses dosyasının adını '.wav' uzantısıyla değiştirir.
	- OpenAI'nin Whisper ASR'sini kullanarak ses içeriğini transkribe eder (openai.Audio.transcribe).
	- Transkripti, messages listesine kullanıcı mesajı olarak ekler.
	- messages listesini OpenAI'nin GPT-3.5 Turbo sohbet modeline gönderir (openai.ChatCompletion.create).
	- Modelin yanıtını, sistem mesajı olarak messages listesine ekler.
	- subprocess modülünü kullanarak sistem mesajını sesli olarak okur (say komutu, macOS için).
	- Kullanıcı ve terapist mesajlarını birleştirerek sohbet metnini oluşturur.

**2.config.py**

Bu dosya, OpenAI API anahtarınızı içerir. Lütfen 'YOUR_OPENAI_API_KEY' yerine gerçek API anahtarınızı yazarak OpenAI API'siyle kimlik doğrulama yapın.

### Ek Notlar

- OpenAI GPT-3.5 Turbo API'sini kullanmak için stabil bir internet bağlantısı gereklidir.
- Sistem mesajını sesli okumak için Windows kullanıcıları, sistemin metni sesli olarak okuma yeteneğine bağlı olarak farklı bir komut kullanabilir.

Kodları inceleyerek ve değiştirerek özel kullanım veya farklı projeler için uyarlayabilirsiniz.

Herhangi bir sorun veya sorunla karşılaşırsanız, Gradio ve OpenAI belgelerine başvurabilirsiniz.