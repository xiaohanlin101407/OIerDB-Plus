from requests import post

with open("Query.oierdb", "r", encoding="utf8") as f:
    cont = f.read()

resp = post("http://127.0.0.1:8080/parser_api/", data={"code": cont})
print(resp.content)
