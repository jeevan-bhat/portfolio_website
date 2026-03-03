from flask import Flask, render_template, jsonify, request, send_file
import os
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/health')
def health():
    return jsonify({'status': 'healthy'}), 200

@app.route('/download-resume')
def download_resume():
    """Generate and download resume as HTML file"""
    resume_content = '''<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: 'Courier New', monospace; margin: 40px; line-height: 1.6; color: #333; }
        .header { text-align: center; margin-bottom: 30px; border-bottom: 3px solid #0066cc; padding-bottom: 20px; }
        .header h1 { margin: 0; color: #0066cc; font-size: 32px; }
        .header p { margin: 5px 0; color: #666; }
        .section { margin-bottom: 25px; }
        .section-title { font-size: 16px; font-weight: bold; color: #0066cc; margin-bottom: 10px; border-bottom: 2px solid #0066cc; padding-bottom: 5px; }
        .entry { margin-bottom: 15px; }
        .entry-title { font-weight: bold; color: #1a1a1a; }
        .entry-subtitle { color: #00a86b; font-style: italic; margin: 3px 0; }
        ul { margin: 10px 0; padding-left: 20px; }
        li { margin: 5px 0; }
    </style>
</head>
<body>
    <div class="header">
        <h1>JEEVAN BHAT</h1>
        <p>System Programmer | C Developer | DSA Engineer | Python Backend Developer</p>
        <p>📧 jeevanbhat33@gmail.com | 🔗 github.com/jeevan-bhat | 💼 linkedin.com/in/jeevan-bhat-a26260263</p>
    </div>

    <div class="section">
        <div class="section-title">PROFESSIONAL SUMMARY</div>
        <p>Passionate developer with strong foundation in C programming, Data Structures & Algorithms, and system-level problem solving. Experienced in backend development using Python & Flask, AI applications, and full-stack web development.</p>
    </div>

    <div class="section">
        <div class="section-title">TECHNICAL SKILLS</div>
        <div class="entry">
            <div class="entry-title">Languages:</div>
            <p>C, C++, Python, Bash/Shell Scripting</p>
        </div>
        <div class="entry">
            <div class="entry-title">Web Development:</div>
            <p>HTML5, CSS3, JavaScript, Flask, REST APIs</p>
        </div>
        <div class="entry">
            <div class="entry-title">Tools:</div>
            <p>Git, Linux, VS Code, Postman</p>
        </div>
    </div>

    <div class="section">
        <div class="section-title">FEATURED PROJECTS</div>
        <div class="entry">
            <div class="entry-title">Bank Management System | C++</div>
            <ul>
                <li>Console-based banking system</li>
                <li>File handling and data persistence</li>
                <li>Modular architecture</li>
            </ul>
        </div>
        <div class="entry">
            <div class="entry-title">DSA Implementation | C</div>
            <ul>
                <li>Data structures: Stack, Queue, Trees, Graphs</li>
                <li>Sorting & Searching algorithms</li>
                <li>Optimized complexity</li>
            </ul>
        </div>
        <div class="entry">
            <div class="entry-title">Text-to-Speech System | Python</div>
            <ul>
                <li>Speech synthesis and recognition</li>
                <li>NLP integration</li>
                <li>Interactive application</li>
            </ul>
        </div>
    </div>

    <footer style="margin-top: 40px; border-top: 2px solid #0066cc; padding-top: 20px; text-align: center; color: #999; font-size: 12px;">
        <p>Portfolio: github.com/jeevan-bhat</p>
    </footer>
</body>
</html>'''
    
    resume_bytes = io.BytesIO(resume_content.encode('utf-8'))
    return send_file(
        resume_bytes,
        mimetype='text/html',
        as_attachment=True,
        download_name='Jeevan_Bhat_Resume.html'
    )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
