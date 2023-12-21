from bardapi import Bard
import requests, os, json
import tools_api.helpers.response as res

class BardHelper():
    
    def initial_token(self, id, cc, ts):
        self._1PSID = id
        self._1PSIDCC = cc
        self._1PSIDTS = ts
        
    def initial_session(self) -> None:
        self.session = requests.Session()
        self.session.cookies.set('__Secure-1PSID', self._1PSID)
        self.session.cookies.set('__Secure-1PSIDCC', self._1PSIDCC)
        self.session.cookies.set('__Secure-1PSIDTS', self._1PSIDTS)
        self.session.headers = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/",
        }
        self.bard = Bard(token=self._1PSID, session=self.session)
        
    def transform_to_json(self, response: str) -> any:
        res = response.split('```')[1]
        res = res[5:]
        res = res.replace('\\n','')
        res = res.replace('\n',' ')
        res = res.replace('\\"','"')
        res = res.replace('*','')
        res = res.replace(',}','}')
        try:
            return json.loads(res)
        except:
            return res
        
    def ask_logo_brief(self) -> str:
        self.initial_session()
        try:
            prompt = """
                Anda adalah seorang pemberi ide handal dalam branding.
                Saya ingin berlatih membuat desain brand logo untuk suatu perusahaan.
                Berikan saya contoh ide brief dengan ketentuan JSON seperti ini:
                {
                "nama_perusahaan": "nama merek yang abstrak",
                "bidang_perusahaan": "ide anda",
                "warna": "tuliskan dalam bentuk hex",
                "jenis_logo": "seperti logotype, logogram, emblem, dll",
                "brief": "tuliskan sedetail mungkin",
                "donts": "elemen yang tidak diinginkan",
                "nice": "elemen yang sangat diharapkan pada desain",
                }
                *PENTING: berikan dalam format JSON saja, jangan ada tambahan teks apapun
            """
            return self.transform_to_json(self.bard.get_answer(prompt)['content'])
        except Exception as e:
            print(e)
            return res.server_error()
    
    def ask_website_brief(self) -> str:
        self.initial_session()
        try:
            prompt = """
                Anda adalah seorang pemberi ide handal dalam web desain.
                Saya ingin berlatih membuat desain web untuk suatu perusahaan.
                Berikan saya contoh ide brief dengan ketentuan JSON seperti ini:
                {
                "nama_perusahaan": "nama merek yang abstrak",
                "bidang_perusahaan": "ide anda",
                "skema_warna": "tuliskan dalam bentuk hex",
                "tema": "seperti elegan, minimalis, modern, dll",
                "kebutuhan_page": "seperti detail section dan page",
                "brief": "tuliskan sedetail mungkin",
                "donts": "elemen yang tidak diinginkan",
                "nice": "elemen yang sangat diharapkan pada desain",
                }
                *PENTING: berikan dalam format JSON saja, jangan ada tambahan teks apapun
            """
            return self.transform_to_json(self.bard.get_answer(prompt)['content'])
        except Exception as e:
            print(e)
            return res.server_error()
    
bardhelper = BardHelper()