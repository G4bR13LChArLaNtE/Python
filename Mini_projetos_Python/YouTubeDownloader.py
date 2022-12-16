from pytube import YouTube

def DownloadAlta(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
      youtubeObject.download()
  except:
    print("Há algum erro no download do seu Vídeo do You Tube!")
  print("Download completo! Parabéns!!!")

def DownloadBaixa(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_lowest_resolution()
  try:
      youtubeObject.download()
  except:
    print("Há algum erro no download do seu Vídeo do You Tube!")
  print("Download completo! Parabéns!!!")



opc= input("Digite a opção de Download: A/B (A -> Alta resolução e B -> Baixa resolução) ")
link = input("Coloque o link do YouTube aqui!! URL: ")
if opc == "A":
    DownloadAlta(link)
else:
    DownloadBaixa(link)