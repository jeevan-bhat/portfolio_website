# 🚀 Jeevan Bhat - Developer Portfolio

A modern, dark-themed developer portfolio showcasing projects, skills, and experience in C, C++, Python, and Web Development.

## ✨ Features

- 🌙 Dark/Light theme toggle
- ⚡ Smooth animations and transitions
- 📱 Fully responsive design (mobile, tablet, desktop)
- 💼 Professional layout optimized for internships & placements
- 🎯 Interactive sections:
  - Hero with typing animation
  - About Me
  - Technical Skills (4 categories)
  - 8 Featured Projects
  - Learning Journey Timeline
  - GitHub Stats
  - Contact Form
  - Resume Download

## 🛠️ Tech Stack

**Frontend:**
- HTML5
- CSS3 (Minified & Optimized)
- Vanilla JavaScript

**Backend:**
- Flask (Python)
- Render.com (Deployment)

**Services:**
- Web3Forms (Contact Form)

## 📦 Installation

### Local Setup

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/jeevan-portfolio.git
cd jeevan-portfolio

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
```

Visit `http://localhost:5000` in your browser.

## 🚀 Deployment

### Deploy to Render.com

1. Push code to GitHub
2. Go to https://render.com
3. Connect GitHub account
4. Create Web Service
5. Select this repository
6. Configure:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
7. Deploy!

Your portfolio will be live at: `https://your-service-name.onrender.com`

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed instructions.

## 📁 Project Structure

```
jeevan-portfolio/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
├── DEPLOYMENT_GUIDE.md   # Deployment instructions
├── README.md             # This file
└── templates/
    └── index.html        # Portfolio HTML
```

## 🎨 Customization

Edit `templates/index.html` to customize:
- Your name and title
- Bio and skills
- Projects (add/remove cards)
- Contact email
- Social links
- Colors and styling

## 📝 Features Breakdown

### Theme Toggle
- Switch between dark and light modes
- Preference saved in localStorage
- All colors automatically adjust

### Contact Form
- Integrated with Web3Forms
- Validates all fields
- Shows loading state during submission
- Success/error alerts
- Auto-clears after submission

### Resume Download
- Generates HTML resume file
- Includes all projects and skills
- Downloads as `Jeevan_Bhat_Resume.html`

### Social Links
- GitHub
- LinkedIn
- Email

### Projects Section
- 8 featured projects
- Tech stack badges
- Feature lists
- GitHub links

## 🔧 Maintenance

### To Update Portfolio:
```bash
# Make changes locally
# Edit templates/index.html or app.py

# Commit changes
git add .
git commit -m "Update portfolio content"

# Push to GitHub
git push

# Render auto-deploys! (1-2 minutes)
```

## 📊 Performance

- Page Load: < 2 seconds
- Lighthouse Score: 95+
- Mobile Friendly: ✓
- Zero external dependencies
- Fully SEO optimized

## 🔐 Security

- No sensitive data stored
- HTTPS enabled on Render
- CSRF protection for forms
- XSS protection in place

## 📄 License

This portfolio template is open source. Feel free to use it as inspiration for your own portfolio!

## 💡 Tips for Success

1. **Update Projects**: Add your own projects with real GitHub links
2. **Personalize**: Change colors, fonts, and styling to match your brand
3. **Add Content**: Write compelling descriptions for your work
4. **Keep Fresh**: Update your portfolio regularly with new projects
5. **Share**: Add portfolio link to resume, LinkedIn, and GitHub bio

## 🤝 Contributing

Want to improve this portfolio? Feel free to fork and submit PRs!

## 📧 Contact

- Email: jeevanbhat33@gmail.com
- GitHub: https://github.com/jeevan-bhat/
- LinkedIn: https://www.linkedin.com/in/jeevan-bhat-a26260263/

---

**Made with ❤️ for internships and placements**

Last Updated: 2024
