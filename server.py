import http.server
import socketserver

PORT = 3000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"服务器运行在 http://localhost:{PORT}")
    print(f"访问 http://localhost:{PORT}/pages/graph_canvas.html 查看项目")
    httpd.serve_forever()