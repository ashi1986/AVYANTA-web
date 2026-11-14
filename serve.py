#!/usr/bin/env python3
"""Local server for the mirrored avyanta.ai site.

Serves D:\website with a single-page-app fallback and opens a browser.
Run with: python serve.py [port]
"""
import http.server
import os
import socketserver
import sys
import threading
import webbrowser

ROOT = os.path.dirname(os.path.abspath(__file__))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def do_GET(self):
        path = self.translate_path(self.path)
        # Directory or existing file -> normal behaviour (/about -> /about/)
        if os.path.isdir(path):
            index = os.path.join(path, "index.html")
            if os.path.isfile(index):
                if not self.path.endswith("/"):
                    self.send_response(301)
                    self.send_header("Location", self.path + "/")
                    self.end_headers()
                    return
                return super().do_GET()
        elif os.path.isfile(path):
            return super().do_GET()
        # Unknown route -> SPA shell
        if "." not in os.path.basename(self.path.split("?")[0]):
            self.path = "/index.html"
        return super().do_GET()

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        pass  # keep the console quiet


class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True


def main():
    port = PORT
    for _ in range(20):
        try:
            httpd = Server(("127.0.0.1", port), Handler)
            break
        except OSError:
            port += 1
    else:
        sys.exit("could not bind a port")

    url = "http://127.0.0.1:%d/" % port
    print("\n  avyanta.ai clone")
    print("  Serving %s" % ROOT)
    print("  Open:    %s" % url)
    print("  Stop:    Ctrl+C\n")
    if not os.environ.get("NO_BROWSER"):
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        httpd.server_close()


if __name__ == "__main__":
    main()
