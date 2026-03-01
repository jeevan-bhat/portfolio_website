# 🚀 DEPLOYMENT GUIDE: Jeevan Bhat Portfolio on Render.com

## Step-by-Step Instructions

### 1. Prepare Files
Your portfolio files are ready:
- `app.py` - Flask server
- `requirements.txt` - Python dependencies
- `templates/index.html` - Your portfolio HTML
- `.gitignore` - Git ignore file

### 2. Create GitHub Repository

**Option A: Using Git Command Line**
```bash
# Navigate to your project folder
cd your-project-folder

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial portfolio commit"

# Create repo on GitHub: https://github.com/new
# Name it: jeevan-portfolio

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/jeevan-portfolio.git
git branch -M main
git push -u origin main
```

**Option B: Using GitHub Desktop**
1. Go to https://github.com/new
2. Create repository named `jeevan-portfolio`
3. Open GitHub Desktop
4. File → Clone Repository → Select your repo
5. Copy files into the cloned folder
6. Commit and Push

### 3. Deploy to Render.com

**Step 1: Create Render Account**
- Go to https://render.com
- Sign up with GitHub (recommended)
- Authorize GitHub connection

**Step 2: Create New Web Service**
1. Click "New +" button
2. Select "Web Service"
3. Connect to your GitHub repository
4. Search for "jeevan-portfolio" and connect

**Step 3: Configure Deployment**
- **Name**: `jeevan-portfolio` (or any name)
- **Environment**: Python 3
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`
- **Plan**: Free (or Paid if needed)

**Step 4: Deploy**
1. Click "Create Web Service"
2. Wait for build to complete (2-5 minutes)
3. Get your live URL: `https://jeevan-portfolio-xxxxx.onrender.com`

### 4. Verify Deployment
- Visit your URL
- Check all features work:
  - Theme toggle (dark/light)
  - Download Resume
  - Social links
  - Contact form

### 5. Custom Domain (Optional)
1. Go to Render Dashboard
2. Select your service
3. Settings → Custom Domains
4. Add your domain (if you have one)
5. Update DNS settings at your domain provider

## Troubleshooting

**Issue: Build fails**
- Check `requirements.txt` is in root folder
- Ensure `app.py` is in root folder
- Check Python version compatibility

**Issue: 404 Error**
- Verify `templates/index.html` exists
- Check `app.py` imports are correct

**Issue: Contact form not working**
- Web3Forms API key is embedded in HTML
- Ensure internet connection is working
- Check browser console for errors (F12)

**Issue: Static files not loading**
- All CSS is inline in HTML
- No external dependencies needed
- Should work immediately

## File Structure
```
jeevan-portfolio/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── .gitignore
└── README.md
```

## Environment Variables (if needed)
Currently none required! Portfolio is self-contained.

## Updates & Maintenance

**To update your portfolio:**
1. Edit files locally
2. Commit changes: `git add . && git commit -m "Update portfolio"`
3. Push to GitHub: `git push`
4. Render auto-deploys from main branch (usually within 1-2 minutes)

## Support
- Render Docs: https://render.com/docs
- Flask Docs: https://flask.palletsprojects.com
- GitHub Docs: https://docs.github.com

---

## Quick Checklist

- [ ] Files prepared and ready
- [ ] GitHub repository created
- [ ] GitHub connected to Render
- [ ] Web Service configured
- [ ] Deployment successful
- [ ] Live URL working
- [ ] All features tested
- [ ] Custom domain added (optional)

Your portfolio is now live! 🎉
