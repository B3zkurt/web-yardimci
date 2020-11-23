import webbrowser

print("-----------------------------------")
print("     Bozkurt Yardımcı Toolu        ")
print("                                   ")
print("-----------------------------------")
print()

print("1.Youtube'u Aç")
print("2.Google'u Aç")
print("3.Gmail'i Aç")
print("4.İnstagram'ı Aç")
print("5.Twitter'ı Aç")
print("6.Github'ı Aç")
print("7.Facebook'u Aç")
print("8.Twitch'ı Aç")
print("9.Dlive'ı Aç")
print("10.Eba'ı Aç")
print("11.Youtube Kanalıma Git")
print("12.İnstagram Sayfamı Takip Et")

asistan = input("Ne Yapmamı İstersin : ")

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

if asistan =="1":
    webbrowser.get(chrome_path).open("youtube.com")

if asistan =="2":
    webbrowser.get(chrome_path).open("google.com")

if asistan =="3":
    webbrowser.get(chrome_path).open("https://www.google.com/gmail/")

if asistan =="4":
    webbrowser.get(chrome_path).open("instagram.com")

if asistan =="5":
    webbrowser.get(chrome_path).open("twitter.com")

if asistan =="6":
    webbrowser.get(chrome_path).open("github.com")

if asistan =="7":
    webbrowser.get(chrome_path).open("facebook.com")

if asistan =="8":
    webbrowser.get(chrome_path).open("https://www.twitch.tv/")

if asistan =="9":
    webbrowser.get(chrome_path).open("https://dlive.tv/")

if asistan =="10":
    webbrowser.get(chrome_path).open("https://giris.eba.gov.tr/EBA_GIRIS/giris.jsp")

if asistan =="11":
    webbrowser.get(chrome_path).open("https://www.youtube.com/channel/UChlvMD3VIvKw_Wf4ST6OnZQ?view_as=subscriber")

if asistan =="12":
    webbrowser.get(chrome_path).open("instagram.com/b3zkurt/")
