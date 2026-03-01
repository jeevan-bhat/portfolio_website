#!/bin/bash

echo "🚀 Starting deployment to GitHub & Render..."
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install Git first:"
    echo "   https://git-scm.com/downloads"
    exit 1
fi

# Initialize git if needed
if [ ! -d ".git" ]; then
    echo "📦 Initializing Git repository..."
    git init
    echo "✅ Git repository initialized"
fi

# Check if remote exists
if ! git remote | grep -q origin; then
    echo "🔗 Adding GitHub remote..."
    git remote add origin https://github.com/jeevan-bhat/portfolio_website.git
    echo "✅ GitHub remote added"
else
    echo "✅ GitHub remote already exists"
fi

# Add all files
echo "📝 Adding all files..."
git add .
echo "✅ Files added"

# Commit
echo "💾 Creating commit..."
git commit -m "Deploy portfolio website - Dark theme, animations, contact form, resume download"
echo "✅ Commit created"

# Set main branch
echo "🌳 Setting main branch..."
git branch -M main
echo "✅ Main branch set"

# Push to GitHub
echo "📤 Pushing to GitHub..."
git push -u origin main
echo "✅ Pushed to GitHub!"

echo ""
echo "🎉 Deployment complete!"
echo ""
echo "Next steps:"
echo "1. Go to https://render.com/dashboard"
echo "2. Your service 'portfolio_website-jeevan_bhat' will auto-deploy"
echo "3. Wait 2-3 minutes for deployment"
echo "4. Visit your live URL!"
echo ""
echo "For updates in future:"
echo "  git add ."
echo "  git commit -m 'Update description'"
echo "  git push"
