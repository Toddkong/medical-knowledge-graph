import http.server
import socketserver
import os

PORT = 8889

# 设置当前工作目录为项目根目录
os.chdir("e:/Trae Project/KG")

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"HTTP服务器已启动在 http://localhost:{PORT}")
    print(f"请访问 http://localhost:{PORT}/pages/graph_canvas.html 测试修复效果")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止")
        httpd.shutdown()