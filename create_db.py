from ext import app, db
from models import Reg, Card, AddCard
from datetime import date
from werkzeug.security import generate_password_hash

kutxeebi = [
    {"name": "Samegrelo", "link": "/samegrelo", "img": "samegrelo.jpg"},
    {"name": "Svaneti", "link": "/svaneti", "img": "svaneti.jpg"},
    {"name": "Afkhazeti", "link": "/afkhazeti", "img": "afkhazeti.jpg"},
    {"name": "Guria", "link": "/guria", "img": "guria.jpg"},
    {"name": "Imereti", "link": "/imereti", "img": "imereti.jpg"},
    {"name": "Kakheti", "link": "/kakheti", "img": "kakheti.jpg"},
    {"name": "Shida Kartli", "link": "/shida_qartli", "img": "shida_qartli.jpg"},
    {"name": "Kvemo Kartli", "link": "/qvemo_qartli", "img": "kvemom_qartli.jpg"},
    {"name": "Racha-Lechkhumi", "link": "/racha", "img": "racha_lechxumi.jpg"},
    {"name": "Adjara", "link": "/adjara", "img": "adjara.jpg"},
    {"name": "Mtskheta-Tianeti", "link": "/mtskheta_tianeti", "img": "mtxeta.jpg"},
    {"name": "Samtskhe-Javakheti", "link": "/samtskhe_javakheti", "img": "samcxe.jpg"}
]
regions = [
    {"name": "Dadianebis sasaxle", "part": "Samegrelo", "img": "dadianebissasaxle.jpg"},
    {"name": "kolxetis erovnuli parki", "part": "Samegrelo", "img": "kolxetiserovnuliparki1.jpg"},
    {"name": "martvilis kanioni", "part": "Samegrelo", "img": "martviliskanioni.jpg"},
    {"name": "paliastomis tba", "part": "Samegrelo", "img": "paliastomistba.jpg"},
    {"name": "vercxlis tba", "part": "Samegrelo", "img": "vercxlistba.jpg"},
   #{"name": "botanikuri bagi", "part": "Samegrelo", "img": "botanikuribagi.jpg"},
    {"name": "mestia", "part": "Svaneti", "img": "mestia.jpg"},
    {"name": "hawvali", "part": "Svaneti", "img": "hawvali.jpg"},
    {"name": "oqrowylis tbebi", "part": "Svaneti", "img": "oqrowylistbeibi1.jpg"},
    {"name": "ratianebis saxl-muzeumi", "part": "Svaneti", "img": "ratiani.jpg"},
    {"name": "siyvarulis koshki", "part": "Svaneti", "img": "siyvaruliskoshki.jpg"},
    #{"name": "svanetis etnografiuli muzeumi", "part": "Svaneti", "img": "svanetisetnografiulimuzeumi.jpg"},
    {"name": "Bediis monasteri", "part": "Afkhazeti", "img": "Bedia2.jpg"},
    {"name": "Besletis xidi", "part": "Afkhazeti", "img": "Beslet_.jpg"},
    {"name": "webeldis cixe", "part": "Afkhazeti", "img": "webeldi.jpg"},
    {"name": "abaatas eklesia", "part": "Afkhazeti", "img": "abaata.jpg"},
    {"name": "babushersa koski", "part": "Afkhazeti", "img": "babushersakoski.jpg"},
    #{"name": "bzipis eklesia", "part": "Afkhazeti", "img": "bzipiseklesia.jpg"},
    {"name": "erketis eklesia", "part": "Guria", "img": "erketiseklesia.jpg"},
    {"name": "wvermagalasparki ", "part": "Guria", "img": "wvermagalasparki.jpg"},
    {"name": "jixetis dedata monasteri ", "part": "Guria", "img": "jixetisdedatamonasteri.jpg"},
    {"name": "shekvetilis dendrologiuri parki.jpg ", "part": "Guria", "img": "shekvetilisdendrologiuriparki.jpg"},
    {"name": "gomismta ", "part": "Guria", "img": "gomismta.jpg"},
    #{"name": "gogietis chanchqeri ", "part": "Guria", "img": "gogi.jpg"},
    {"name": "kacxis veti  ", "part": "Imereti", "img": "kacxisveti.jpg"},
    {"name": "mowameta tazari ", "part": "Imereti", "img": "mowametatazari.jpg"},
    {"name": "sataflia ", "part": "Imereti", "img": "sataflia.jpg"},
    {"name": "cxrajvari ", "part": "Imereti", "img": "cxrajvari.jpg"},
    {"name": "bagratis tazari ", "part": "Imereti", "img": "bagrati.jpg"},
    #{"name": "gelatis tazari ", "part": "Imereti", "img": "gelati.jpg"},
    {"name": "arwivis xeoba ", "part": "Kakheti", "img": "arwivisxeoba.jpg"},
    {"name": "martotis tba ", "part": "Kakheti", "img": "martotistba.jpg"},
    {"name": "davitgareji ", "part": "Kakheti", "img": "davitgareji.jpg"},
    {"name": "garejis udabno ", "part": "Kakheti", "img": "gareji.jpg"},
    {"name": "jixetis dedata monasteri ", "part": "Kakheti", "img": "jixetisdedatamonasteri.jpg"},
    #{"name": "axatelis xvtaebi seklesia ", "part": "Kakheti", "img": "axatelisxvtaebiseklesia.jpg"},
    {"name": "goriscixe ", "part": "Shida Kartli", "img": "goriscixe.jpg"},
    {"name": " qvataxevis monasteri", "part": "Shida Kartli", "img": "qvataxevismonasteri.jpg"},
    {"name": "rkonis monasteri ", "part": "Shida Kartli", "img": "rkonismonasteri.jpg"},
    {"name": " tamaris savarzlebi", "part": "Shida Kartli", "img": "tamarissavarzlebi.jpg"},
    {"name": " brutsabzeli smta", "part": "Shida Kartli", "img": "brutsabzelismta.jpg"},
    {"name": "tamaris xidi ", "part": "Shida Kartli", "img": "tamarisxidi.jpg"},
    {"name": " didgoris monumenti", "part": "Kvemo Kartli", "img": "didgorismonumenti.jpg"},
    {"name": "kldekaris cixe ", "part": "Kvemo Kartli", "img": "kldekariscixe.jpg"},
    {"name": " martyofis monasteri", "part": "Kvemo Kartli", "img": "martyofimonasteri.jpg"},
    {"name": "algetis erovnuli parki", "part": "Kvemo Kartli", "img": "algetiserovnuliparki.jpg"},
    {"name": " dashbashis kanioni", "part": "Kvemo Kartli", "img": "dashbashiskanioni.jpg"},
    {"name": "dmanisi sioni nakalakari ", "part": "Kvemo Kartli", "img": "tamarisxidi.jpg"},
    {"name": "barakonis eklesia ", "part": "Racha-Lechkhumi", "img": "barakoniseklesia.jpg"},
    {"name": "nikorwminda ", "part": "Racha-Lechkhumi", "img": "nikorwminda.jpg"},
    {"name": "shaoris wyalsacavi ", "part": "Racha-Lechkhumi", "img": "shaoriswyalsacavi.jpg"},
    {"name": "shovi ", "part": "Racha-Lechkhumi", "img": "shovi.jpg"},
    {"name": "uziro tba ", "part": "Racha-Lechkhumi", "img": "uzirotba.jpg"},
    {"name": "minda cixe ", "part": "Racha-Lechkhumi", "img": "mindacixe.jpg"},
    {"name": "goderzis alpuri bagi", "part": "Adjara", "img": "godezisalpuribagi.jpg"},
    {"name": "merisis chanchqeri", "part": "Adjara", "img": "merisischanchqeri.jpg"},
    {"name": "anbanis koshki", "part": "Adjara", "img": "anbanis-koshk.jpg"},
    {"name": "mwvane tba", "part": "Adjara", "img": "mwvanetba.jpg"},
    {"name": "tba tbiyeli", "part": "Adjara", "img": "tbatbiyeli.jpg"},
    {"name": "ali da ninos kandakeba", "part": "Adjara", "img": "ali-da-ninos-kandakeba-ali-nino-statue-1.jpg"},
    {"name": "shatili", "part": "Mtskheta-Tianeti", "img": "shatili.jpg"},
    {"name": "gveletis chanchkeri", "part": "Mtskheta-Tianeti", "img": "gveletischanchkeri.jpg"},
    {"name": "myinvewveri", "part": "Mtskheta-Tianeti", "img": "myinvewveri.jpg"},
    {"name": "snoscixe", "part": "Mtskheta-Tianeti", "img": "snoscixe.jpg"},
    {"name": "ananuri", "part": "Mtskheta-Tianeti", "img": "ananuri.jpg"},
    {"name": "sioni", "part": "Mtskheta-Tianeti", "img": "sioni.jpg"},
    {"name": "mwvane monasteri", "part": "Samtskhe-Javakheti", "img": "mwvanemonasteri.jpg"},
    {"name": "rabaatis cixe", "part": "Samtskhe-Javakheti", "img": "rabaatiscixe.jpg"},
    {"name": "tabawyuris tba", "part": "Samtskhe-Javakheti", "img": "tabawyuristba.jpg"},
    {"name": "varzia", "part": "Samtskhe-Javakheti", "img": "varzia.jpg"},
    {"name": "zarzmis cixe", "part": "Samtskhe-Javakheti", "img": "zarzmiscixe.jpg"},
    {"name": "tmogvis cixe", "part": "Samtskhe-Javakheti", "img": "tmogviscixe.jpg"},


]

users = [
    {"name": "lasha", "password": "2010", "birthday": date(2010, 4, 29), "gender": "კაცი", "country": "საქართველო", "role": "admin"},
    {"name": "tsotne", "password": "2010", "birthday": date(2010, 4, 29), "gender": "კაცი", "country": "საქართველო","role": "moderator"},
    {"name": "ioane", "password": "2010", "birthday": date(2010, 4, 29), "gender": "კაცი", "country": "საქართველო","role": "guest"}
]

with app.app_context():
    db.drop_all()
    db.create_all()
    for user in users:
        new_user = Reg(
            name=user["name"],
            password=user["password"],
            birthday=user["birthday"],
            gender=user["gender"],
            country=user["country"],
            role=user["role"])
        db.session.add(new_user)
    db.session.commit()
    for kutxe in kutxeebi:
        new_kutxe = Card(
            name=kutxe["name"],
            link=kutxe["link"],
            img=kutxe["img"])
        db.session.add(new_kutxe)
    db.session.commit()
    for regions in regions:
        new_region= AddCard(
            name=regions["name"],
            part=regions["part"],
            img=regions["img"])
        db.session.add(new_region)
    db.session.commit()


