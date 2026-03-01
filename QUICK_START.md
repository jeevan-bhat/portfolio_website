# 📋 QUICK START: Deploy to Render.com

## 5-Minute Deployment

### Step 1: Create GitHub Repository (2 minutes)

1. Go to https://github.com/new
2. Repository name: `jeevan-portfolio`
3. Select "Public"
4. Click "Create repository"

### Step 2: Upload Files to GitHub

**Option A - Using Git (Recommended)**
```bash
# Download and install Git: https://git-scm.com/downloads

# Open Terminal/Command Prompt in your project folder

git init
git add .
git commit -m "Initial portfolio commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/jeevan-portfolio.git
git push -u origin main
```

**Option B - Upload via GitHub Web Interface**
1. Open your GitHub repository
2. Click "Add file" → "Upload files"
3. Drag and drop all files (except .git folder)
4. Click "Commit changes"

### Step 3: Deploy to Render (2 minutes)

1. Go to https://render.com
2. Click "Sign Up" (or "Sign In" if you have account)
3. Choose "Continue with GitHub"
4. Authorize GitHub
5. Click "New +" → "Web Service"
6. Click "Connect" next to your `jeevan-portfolio` repository
7. Fill in these settings:
   - **Name**: jeevan-portfolio
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free (recommended to start)
8. Click "Create Web Service"

### Step 4: Wait for Deployment (2-3 minutes)

- Render will build and deploy your app
- You'll see a green checkmark when done
- Your URL: `https://jeevan-portfolio-xxxxx.onrender.com`

### ✅ Done! Your portfolio is LIVE!

---

## Files Checklist

Make sure these files are in your GitHub repository:

```
✅ app.py
✅ requirements.txt
✅ templates/index.html
✅ .gitignore
✅ README.md
✅ DEPLOYMENT_GUIDE.md
```

---

## Test Your Live Portfolio

1. Visit your Render URL
2. Check:
   - [ ] Page loads quickly
   - [ ] Theme toggle works
   - [ ] All sections visible
   - [ ] Resume download works
   - [ ] Social links open correct pages
   - [ ] Contact form shows success message
   - [ ] Mobile responsive

---

## Share Your Portfolio

Once deployed, share your URL:
- LinkedIn: Add to profile
- Resume: Add to contact section
- Email: jeevanbhat33@gmail.com
- GitHub Bio: Add link

---

## Need Help?

**Common Issues:**

| Issue | Solution |
|-------|----------|
| 404 Error | Wait 2-3 minutes for build to complete |
| Page not loading | Check Render dashboard for errors |
| Form not working | Internet connection required |
| Dark theme not saved | Browser localStorage enabled? |

**Quick Links:**
- Render Support: https://render.com/docs
- View Logs: Render Dashboard → Logs tab
- Redeploy: Render Dashboard → "Manual Deploy"

---

## Future Updates

**To update your portfolio later:**

```bash
# Make changes to files
# Then:
git add .
git commit -m "Update portfolio"
git push

# Render auto-deploys! (1-2 minutes)
```

---

## Custom Domain (Optional)

After 7 days, you can add a custom domain:
1. Render Dashboard → Settings
2. "Custom Domains"
3. Add your domain
4. Update DNS at domain provider

Example: `portfolio.jeevan-bhat.com`

---

**Your portfolio is now live! 🎉**

Visit your URL and share it everywhere!
