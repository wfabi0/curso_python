from http.server import BaseHTTPRequestHandler, HTTPServer
import json

alunos = [
    {"id": 1, "nome": "Maria", "idade": 16},
    {"id": 2, "nome": "João", "idade": 17}
]

PORT = 80


class MinhaAPI(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/alunos":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            resposta = json.dumps(alunos)
            self.wfile.write(resposta.encode("utf-8"))
        elif self.path.startswith("/api/alunos"):
            try:
                aluno_id = int(self.path.split("/")[-1])
            except ValueError:
                self.send_response(400)
                self.end_headers()
                return

            aluno_encontrado = None
            for aluno in alunos:
                if aluno["id"] == aluno_id:
                    aluno_encontrado = aluno
                    break
            if aluno_encontrado:
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()

                resposta = json.dumps(aluno_encontrado)
                self.wfile.write(resposta.encode("utf-8"))
            else:
                self.send_response(404)
                self.send_header("Content-Type", "application/json")
                self.end_headers()

                erro = ("Erro: Aluno não encontrado!")
                self.wfile.write(json.dumps(erro).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()


def main():
    servidor = HTTPServer(("localhost", PORT), MinhaAPI)

    print(f"Servidor rodando em http://localhost:{PORT}")
    servidor.serve_forever()


main()
