from json import dumps, load
from .models import Oier as OIer
from .models import Record
from django.contrib import admin
import tqdm
# Register your models here.

admin.site.register(OIer)


def updateOIer(oierData: dict) -> OIer:
    if (OIer.objects.filter(uid=oierData["uid"]).exists()):
        return None
    ans = []
    for i in oierData["records"]:
        rec = Record.objects.create(**i)
        rec.uid = oierData["uid"]
        rec.save()
        ans.append(rec)

    del oierData["records"]  # = dumps(oierData["records"])
    oier = OIer.objects.create(**oierData)
    for i in ans:
        oier.records.add(i)
    oier.save()
    return oier


def updateOIers(path="./piggySQL/dist/OIer.json") -> None:
    with open(path, "r", encoding="utf8") as f:
        for i in tqdm.tqdm(load(f).values()):
            updateOIer(i)


# updateOIers()
