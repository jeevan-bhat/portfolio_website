# 📤 Push to GitHub & Render

Your files are ready! Here's how to push them to your repos:

## 1️⃣ Push to GitHub (jeevan-bhat/portfolio_website)

```bash
# Navigate to your local project folder
cd your-local-portfolio-folder

# Initialize git (if not already done)
git init

# Add GitHub remote
git remote add origin https://github.com/jeevan-bhat/portfolio_website.git

# Add all files
git add .

# Commit
git commit -m "Initial portfolio commit - Dark theme, resume download, contact form"

# Push to GitHub
git branch -M main
git push -u origin main
```

## 2️⃣ Connect to Render (portfolio_website-jeevan_bhat)

Render auto-connects to your GitHub repo! Just:

1. Go to your Render Dashboard
2. Select "portfolio_website-jeevan_bhat"
3. Go to Settings → GitHub
4. Reconnect if needed
5. Click "Manual Deploy" in the Deploy tab

**OR** If not connected yet:

1. Go to https://render.com/dashboard
2. Click "New +" → "Web Service"
3. Select "Connect Repository"
4. Search for "portfolio_website"
5. Click "Connect"
6. Fill in:
   - **Name**: portfolio_website-jeevan_bhat
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
7. Click "Create Web Service"

## ✅ File Structure for Push

```
portfolio_website/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── DEPLOYMENT_GUIDE.md
├── QUICK_START.md
└── templates/
    └── index.html
```

## 🔄 Deployment Happens Automatically

Once pushed to GitHub:
1. Render detects changes
2. Builds your project
3. Deploys automatically (2-3 minutes)
4. Your URL updates: https://portfolio-website-jeevan-bhat.onrender.com

## 📝 Git Commands Summary

```bash
# Check status
git status

# Push changes
git push

# Pull latest
git pull

# View commit history
git log
```

## 🎉 You're Done!

Both repos will be synced and live on Render!
