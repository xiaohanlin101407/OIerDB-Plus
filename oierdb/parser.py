import json
from piggySQL.models import Oier, Record
from typing import List, Union
from .QuickDjango import QJR


class Query:
    def __init__(self, string: Union[str, List[str]]):
        if isinstance(string, str):
            self.string = string.splitlines()
        self.preprocess()
        self.parse()

    def preprocess(self):
        tmp = []
        self.is_value = [False for _ in self.string]
        self.is_value.append(False)
        for i, j in enumerate(self.string):
            tmp.append(j.strip())
            if (j[0] == " "):
                self.is_value[i] = True
        self.initial = ""
        self.name = ""
        self.gender = ""
        self.enroll_middle = ""
        self.CCF_level = ""
        self.records = []
        self.string = tmp

    def parse_records(self, idx: int) -> int:
        while self.is_value[idx]:
            self.records.append(json.loads(self.string[idx]))
            idx += 1
        return idx

    def parse_initial(self, idx: int) -> int:
        if not self.is_value[idx]:
            raise ValueError("Blank initial query.")

        if idx + 1 < len(self.string) and self.is_value[idx + 1]:
            raise ValueError("No multi-initial possible.")
        if self.initial:
            raise ValueError("Initial has been provided before.")
        self.initial = self.string[idx].lower()
        return idx + 1

    def parse_name(self, idx: int) -> int:
        if not self.is_value[idx]:
            raise ValueError("Blank name query.")
        if idx + 1 < len(self.string) and self.is_value[idx + 1]:
            raise ValueError("No multi-name possible.")
        if self.name:
            raise ValueError("Name has been provided before.")
        self.name = self.string[idx]
        return idx + 1

    def parse_gender(self, idx: int) -> int:
        if not self.is_value[idx]:
            raise ValueError("Blank gender query.")
        if idx + 1 < len(self.string) and self.is_value[idx + 1]:
            raise ValueError("No multi-gender possible.")
        if self.name:
            raise ValueError("Gender has been provided before.")
        try:
            self.gender = int(self.string[idx])
        except BaseException:
            raise ValueError("Gender is not intenger.")
        if self.gender not in [-1, 0, 1]:
            raise ValueError(f"Gender param cannot accept {self.gender}.")
        return idx + 1

    def parse_enroll_middle(self, idx: int) -> int:
        if not self.is_value[idx]:
            raise ValueError("Blank enroll_middle query.")
        if idx + 1 < len(self.string) and self.is_value[idx + 1]:
            raise ValueError("No multi-enroll_middle possible.")
        if self.name:
            raise ValueError("Enroll_middle has been provided before.")
        try:
            self.enroll_middle = int(self.string[idx])
        except BaseException:
            raise ValueError("Enroll_middle is not intenger.")
        return idx + 1

    def parse_CCF_level(self, idx: int) -> int:
        if not self.is_value[idx]:
            raise ValueError("Blank CCF_level query.")
        if idx + 1 < len(self.string) and self.is_value[idx + 1]:
            raise ValueError("No multi-CCF_level possible.")
        if self.CCF_level:
            raise ValueError("CCF_level has been provided before.")
        try:
            self.CCF_level = int(self.string[idx])
        except BaseException:
            raise ValueError("CCF_level is not intenger.")
        return idx + 1

    def parse(self):
        length: int = len(self.string)
        idx: int = 0
        while idx < length:
            while not self.string[idx]:
                idx += 1
            assert self.string[idx]

            if self.string[idx] == "records:":
                idx = self.parse_records(idx + 1)
            elif self.string[idx] == "initial:":
                idx = self.parse_initial(idx + 1)
            elif self.string[idx] == "name:":
                idx = self.parse_name(idx + 1)
            elif self.string[idx] == "gender:":
                idx = self.parse_gender(idx + 1)
            elif self.string[idx] == "enroll_middle:":
                idx = self.parse_enroll_middle(idx + 1)
            elif self.string[idx] == "CCF_level:":
                idx = self.parse_CCF_level(idx + 1)
            else:
                raise ValueError(
                    f"Unexpected Query Condition: {self.string[idx]}.")

    def JsonQuery(self):
        baseQuery = {}
        if self.initial:
            baseQuery["initial"] = self.initial
        if self.name:
            baseQuery["name"] = self.name
        if self.CCF_level:
            baseQuery["CCF_level"] = self.CCF_level
        if self.enroll_middle:
            baseQuery["enroll_middle"] = self.enroll_middle
        if self.gender:
            baseQuery["gender"] = self.gender
        return {"records": self.records, "baseQuery": baseQuery}

    def query_records(self, records):
        if len(records) == 0:
            raise ValueError("No records found while query_records is called.")
        print(records)
        oiers = {i.uid for i in Record.objects.filter(**records[0])}
        for i in records[1:]:
            tmp = {j.uid for j in Record.objects.filter(**i)}
            oiers = oiers.intersection(tmp)
        return {Oier.objects.get(pk=i) for i in oiers if i != 0}

    def Query(self):
        q = self.JsonQuery()
        rcs = q["records"]
        if rcs:
            res = set(Oier.objects.filter(**q["baseQuery"]))
            return res.intersection(self.query_records(records=rcs))
        else:
            return Oier.objects.filter(**q["baseQuery"])

    def JsonResponse(self):
        resp = self.Query()
        if len(resp) > 50:
            raise ValueError("Response to large to transfer")
        return [[
            oier.uid,
            oier.initial,
            oier.name,
        ] for oier in resp]


class MultiQuery:
    def __init__(self, string: str):
        string = string.splitlines()
        self.queries = []
        tmp = []
        for i in string:
            if i != "MultiQuery:":
                tmp.append(i)
            else:
                self.queries.append(Query(tmp))
                tmp = []

    def JsonResponse(self):
        return [i.JsonResponse() for i in self.queries]


def parser_api(request):
    code = request.POST.get("code", None)
    if code is None or code == "":
        return QJR(400, "Empty request is not permitted.")
    else:
        try:
            q = Query(code)
            return QJR(200, q.JsonResponse())
        except ValueError as err:
            return QJR(400, str(err))
