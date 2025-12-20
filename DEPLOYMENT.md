# Deployment Guide - Physical AI Robotics Essential Course

This guide will help you deploy both the frontend (Docusaurus) and backend (FastAPI) of your Physical AI Robotics project.

## Project Overview

- **Frontend**: Docusaurus-based educational website
- **Backend**: FastAPI with RAG chatbot (LangChain + Qdrant + Groq)
- **Features**: Multilingual support (English/Urdu), Voice-enabled chatbot, Dark mode

## Prerequisites

Before deploying, ensure you have:
- ✅ All dependencies installed
- ✅ Frontend build successful
- ✅ Backend tested locally
- ✅ API keys configured (.env file)

## Frontend Deployment (Vercel)

### Option 1: Deploy via Vercel Dashboard

1. Go to [vercel.com](https://vercel.com) and sign in
2. Click "New Project"
3. Import your GitHub repository
4. Vercel will auto-detect Docusaurus
5. Click "Deploy"

### Option 2: Deploy via Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Deploy
vercel
```

### Frontend Environment Variables (Optional)

No environment variables needed for frontend deployment.

## Backend Deployment (Render)

### Option 1: Deploy via Render Dashboard

1. Go to [render.com](https://render.com) and sign in
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Python Version**: 3.11.0

5. Add Environment Variables:
   - `GROQ_API_KEY`: Your Groq API key
   - `OPENROUTER_API_KEY`: Your OpenRouter API key
   - `QDRANT_URL`: Your Qdrant database URL
   - `QDRANT_API_KEY`: Your Qdrant API key
   - `NEON_DATABASE_URL`: Your Neon PostgreSQL URL

6. Click "Create Web Service"

### Option 2: Deploy via Render Blueprint

```bash
# render.yaml is already configured in backend/
# Just connect your GitHub repo and Render will auto-deploy
```

### Backend Health Check

After deployment, test your backend:
```bash
curl https://your-backend-url.onrender.com/
```

## Update Frontend with Backend URL

After deploying the backend, update the frontend chatbot component:

1. Open `src/components/Chatbot/Chatbot.tsx`
2. Update line 10:
```typescript
const BACKEND_URL = 'https://your-backend-url.onrender.com';
```

3. Rebuild and redeploy frontend:
```bash
npm run build
vercel --prod
```

## Alternative Deployment Options

### Frontend Alternatives
- **Netlify**: Similar to Vercel, auto-detects Docusaurus
- **GitHub Pages**: Use `npm run deploy` (requires docusaurus.config.ts update)
- **Cloudflare Pages**: Auto-deploy from GitHub

### Backend Alternatives
- **Railway**: Similar to Render, easy Python deployment
- **Fly.io**: Good for global edge deployment
- **AWS/Azure/GCP**: More complex but highly scalable

## Environment Variables Reference

### Backend (.env)
```env
GROQ_API_KEY=your_groq_api_key
OPENROUTER_API_KEY=your_openrouter_key
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key
NEON_DATABASE_URL=your_neon_database_url
```

**⚠️ IMPORTANT**: Never commit your `.env` file to GitHub!

## Post-Deployment Testing

### Test Frontend
1. Visit your deployed frontend URL
2. Check all chapters load correctly
3. Test language switcher (English/Urdu)
4. Verify chatbot opens

### Test Backend
1. Visit `https://your-backend-url/docs` for API documentation
2. Test `/chat` endpoint with a sample question
3. Verify chatbot responds correctly

### Test Integration
1. Open chatbot on frontend
2. Ask: "What is Physical AI?"
3. Verify response from backend

## Troubleshooting

### Frontend Build Fails
```bash
# Clear cache and rebuild
npm run clear
npm install
npm run build
```

### Backend Deployment Fails
- Check Python version (should be 3.11.0)
- Verify all environment variables are set
- Check logs for missing dependencies

### Chatbot Not Working
- Verify backend URL in Chatbot.tsx
- Check CORS settings in backend/main.py
- Ensure environment variables are set correctly

### CORS Errors
If you see CORS errors, ensure backend allows your frontend domain:

```python
# In backend/main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend-url.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Performance Optimization

### Frontend
- Build is already optimized
- Static files are cached automatically
- Consider adding CDN for assets

### Backend
- Qdrant provides fast vector search
- Consider upgrading Render plan for production
- Add caching for frequent queries

## Monitoring

### Frontend (Vercel)
- Auto-monitoring included
- View analytics in Vercel dashboard

### Backend (Render)
- View logs in Render dashboard
- Set up alerts for downtime
- Monitor API usage

## Cost Estimate

### Free Tier
- **Vercel**: Free for personal projects
- **Render**: Free tier available (slower spin-up)
- **Qdrant Cloud**: Free tier (1GB)
- **Neon**: Free tier (0.5GB)
- **Groq API**: Free tier available

### Paid Tier (Recommended for Production)
- **Vercel Pro**: $20/month
- **Render Standard**: $7-25/month
- **Qdrant**: $25/month (5GB)
- **Neon**: $19/month (10GB)
- **Groq API**: Pay per usage

## Security Checklist

- ✅ Environment variables configured securely
- ✅ `.env` file in `.gitignore`
- ✅ CORS properly configured
- ✅ API keys rotated if exposed
- ✅ HTTPS enabled (automatic on Vercel/Render)
- ✅ Rate limiting enabled for production

## Support

For issues or questions:
- GitHub: [Shayan-meo](https://github.com/Shayan-meo)
- LinkedIn: [Muhammad Shayan](https://www.linkedin.com/in/muhammad-shayan-99a39b2b0/)
- WhatsApp: +923162063441

---

**Built with ❤️ for GIAIC Hackathon by Muhammad Shayan**
