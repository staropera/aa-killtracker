from datetime import datetime
from hashlib import md5
import json

from allianceauth.eveonline.models import EveAllianceInfo, EveCorporationInfo
from eveuniverse.models import EveEntity, EveUniverseEntityModel

from ...helpers.killmails import KillmailTemp
from ...models import EveKillmail
from .load_eveuniverse import load_eveuniverse
from . import _currentdir


def _load_json_from_file(filename: str):
    with open(f"{_currentdir}/{filename}.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


def _load_killmails_data():
    data = dict()
    for obj in _load_json_from_file("killmails"):
        killmail_id = obj["killID"]
        obj["killmail"]["killmail_id"] = killmail_id
        obj["killmail"]["killmail_time"] = datetime.utcnow().strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        )
        my_hash = md5(str(killmail_id).encode("utf8")).hexdigest()
        obj["zkb"]["hash"] = my_hash
        obj["zkb"][
            "href"
        ] = f"https://esi.evetech.net/v1/killmails/{killmail_id}/{my_hash}/"
        data[killmail_id] = obj

    return data


killmails_data = _load_killmails_data()
eveentities_data = _load_json_from_file("eveentities")
evealliances_data = _load_json_from_file("evealliances")
evecorporations_data = _load_json_from_file("evecorporations")


def load_eveentities():
    for item in eveentities_data:
        EveEntity.objects.update_or_create(
            id=item["id"], defaults={"name": item["name"], "category": item["category"]}
        )

    for MyModel in EveUniverseEntityModel.all_models():
        if MyModel.eve_entity_category():
            for obj in MyModel.objects.all():
                EveEntity.objects.update_or_create(
                    id=obj.id,
                    defaults={
                        "name": obj.name,
                        "category": MyModel.eve_entity_category(),
                    },
                )


def load_evealliances():
    EveAllianceInfo.objects.all().delete()
    for item in evealliances_data:
        alliance = EveAllianceInfo.objects.create(**item)
        EveEntity.objects.create(
            id=alliance.alliance_id,
            name=alliance.alliance_name,
            category=EveEntity.CATEGORY_ALLIANCE,
        )


def load_evecorporations():
    EveCorporationInfo.objects.all().delete()
    for item in evecorporations_data:
        corporation = EveCorporationInfo.objects.create(**item)
        EveEntity.objects.create(
            id=corporation.corporation_id,
            name=corporation.corporation_name,
            category=EveEntity.CATEGORY_CORPORATION,
        )


def load_killmails(killmail_ids: set = None):
    if killmail_ids:
        killmail_ids = set(killmail_ids)
    EveKillmail.objects.all().delete()
    for killmail_id, item in killmails_data.items():
        if not killmail_ids or killmail_id in killmail_ids:
            EveKillmail.objects._create_from_dict(item)


def load_temp_killmail(killmail_id: int):
    for item_id, item in killmails_data.items():
        if killmail_id == item_id:
            return KillmailTemp._create_from_dict(item)

    raise ValueError(f"EveKillmail with id {killmail_id} not found.")


def load_all():
    EveEntity.objects.all().delete()
    load_eveuniverse()
    load_eveentities()
    load_evealliances()
    load_killmails()
