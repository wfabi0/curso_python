from http.server import BaseHTTPRequestHandler, HTTPServer
import json

alunos = [
    {"id": 1, "nome": "Maria", "idade": 16},
    {"id": 2, "nome": "João", "idade": 17},
    {"id": 3, "nome": "Pedro", "idade": 15},
    {"id": 4, "nome": "Júlia", "idade": 17},
    {"id": 5, "nome": "Letícia", "idade": 16}
]


def proximo_id():
    return max(aluno["id"] for aluno in alunos) + 1 if alunos else 1


class MinhaAPI(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/api/alunos":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(json.dumps(alunos).encode("utf-8"))

        elif self.path.startswith("/api/alunos"):
            try:
                aluno_id = int(self.path.split("/")[-1])
            except ValueError:
                self.send_response(400)
                self.end_headers()
                return

            for aluno in alunos:
                if aluno["id"] == aluno_id:
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(aluno).encode("utf-8"))

            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(
                "Aluno não encontrado!").encode("utf-8"))

        else:
            self.send_response(404)
            self.end_headers()

    # criação dos métodos

    def do_POST(self):  # criar os dados
        if self.path == "/api/alunos":
            tamanho = int(self.headers.get("Content-length", 0))

            corpo = self.rfile.read(tamanho)
            dados = json.loads(corpo)

            if "nome" not in dados or "idade" not in dados:
                self.send_response(404)
                self.headers()
                return
            novo_aluno = {
                "id": proximo_id(),
                "nome": dados["nome"],
                "idade": dados["idade"]
            }
            alunos.append(novo_aluno)

            self.send_response(201)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(novo_aluno).encode("utf-8"))

    def do_PUT(self):
        if self.path == "/api/alunos":
            try:
                aluno_id = int(self.path.split("/")[-1])
            except ValueError:
                self.send_response(400)
                self.end_headers()
                return

            tamanho = int(self.headers.get("Content-length", 0))
            corpo = self.rfile.read(tamanho)
            dados = json.loads(corpo)

            for aluno in alunos:
                if aluno["id"] == aluno_id:
                    aluno["nome"] = dados.get("nome", aluno["nome"])
                    aluno["idade"] = dados.get("idade", aluno["idade"])
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(aluno).encode("utf-8"))
                    return
            self.send_response(404)
            self.end_headers()

    def do_PATCH(self):
        if self.path == "/api/alunos":
            try:
                aluno_id = int(self.path.split("/")[-1])
            except ValueError:
                self.send_response(400)
                self.end_headers()
                return

            tamanho = int(self.headers.get("Content-length", 0))
            corpo = self.rfile.read(tamanho)
            dados = json.loads(corpo)

            for aluno in alunos:
                if aluno["id"] == aluno_id:
                    if "nome" in dados:
                        aluno["nome"] = dados["nome"]
                    if "idade" in dados:
                        aluno["idade"] = dados["idade"]
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(aluno).encode("utf-8"))
                    return
            self.send_response(404)
            self.end_headers()

    def do_DELETE(self):
        if self.path == "/api/alunos":
            try:
                aluno_id = int(self.path.split("/")[-1])
            except ValueError:
                self.send_response(400)
                self.end_headers()
                return

            for aluno in alunos:
                if aluno["id"] == aluno_id:
                    alunos.remove(aluno)
                    self.send_response(204)
                    self.end_headers()
                    return
            self.send_response(404)
            self.end_headers()


def main():
    servidor = HTTPServer(("localhost", 8005), MinhaAPI)

    print(f"Servidor rodando em http://localhost:8005")
    servidor.serve_forever()


main()
