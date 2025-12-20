# Deployment Checklist

## Pre-Deployment Verification

### ✅ Dependencies
- [x] Frontend dependencies installed (`npm install`)
- [x] Backend dependencies installed (`pip install -r requirements.txt`)
- [x] All packages up to date
- [x] No critical security vulnerabilities

### ✅ Build Status
- [x] Frontend builds successfully (`npm run build`)
- [x] No TypeScript errors
- [x] No build warnings (only deprecation notice for Docusaurus v4)
- [x] Production build tested locally (`npm run serve`)

### ✅ Backend Status
- [x] All Python imports working
- [x] FastAPI server starts successfully
- [x] Environment variables configured (.env file)
- [x] API endpoints tested
- [x] Qdrant vector database connected
- [x] Groq LLM API working

### ✅ Code Quality
- [x] No critical diagnostics
- [x] Only one hint in vector_store.py (non-critical)
- [x] All components functional
- [x] Chatbot working with voice input
- [x] Dark mode functional

### ✅ Configuration Files
- [x] `.gitignore` updated for backend files
- [x] `vercel.json` created for frontend deployment
- [x] `backend/render.yaml` created for backend deployment
- [x] `DEPLOYMENT.md` with detailed instructions
- [x] `README.md` updated with complete information

## Deployment Steps

### Step 1: Prepare Repository

```bash
# Add all changes
git add .

# Commit
git commit -m "Prepare for deployment - Add deployment configs and documentation"

# Push to GitHub
git push origin main
```

### Step 2: Deploy Frontend to Vercel

**Option A: Via Vercel Dashboard**
1. Go to https://vercel.com
2. Click "New Project"
3. Import GitHub repository
4. Deploy (auto-detected as Docusaurus)

**Option B: Via CLI**
```bash
npm i -g vercel
vercel login
vercel --prod
```

**Expected Output:**
- Frontend URL: `https://your-project.vercel.app`
- Build time: ~4-5 minutes
- Status: Ready

### Step 3: Deploy Backend to Render

**Via Render Dashboard:**
1. Go to https://render.com
2. New → Web Service
3. Connect GitHub repository
4. Configure:
   - **Name**: physical-ai-backend
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Python Version**: 3.11.0

5. Add Environment Variables:
   ```
   GROQ_API_KEY=<from backend/.env>
   OPENROUTER_API_KEY=<from backend/.env>
   QDRANT_URL=<from backend/.env>
   QDRANT_API_KEY=<from backend/.env>
   NEON_DATABASE_URL=<from backend/.env>
   ```

6. Create Web Service

**Expected Output:**
- Backend URL: `https://physical-ai-backend.onrender.com`
- Deploy time: ~3-5 minutes
- Status: Live

### Step 4: Connect Frontend to Backend

1. Update `src/components/Chatbot/Chatbot.tsx` line 10:
```typescript
const BACKEND_URL = 'https://physical-ai-backend.onrender.com';
```

2. Rebuild and redeploy frontend:
```bash
npm run build
vercel --prod
```

### Step 5: Test Deployment

**Frontend Tests:**
- [ ] Homepage loads correctly
- [ ] All 10 chapter cards visible
- [ ] Chapter links work
- [ ] Language switcher works (English/Urdu)
- [ ] Dark mode works (site theme)
- [ ] Responsive on mobile

**Backend Tests:**
- [ ] Visit `https://your-backend-url.onrender.com/`
- [ ] Check API docs: `https://your-backend-url.onrender.com/docs`
- [ ] Test health endpoint returns welcome message

**Integration Tests:**
- [ ] Open chatbot on frontend
- [ ] Chatbot button appears
- [ ] Chatbot window opens
- [ ] Ask: "What is Physical AI?"
- [ ] Bot responds correctly
- [ ] Voice input works
- [ ] Dark mode toggle works in chatbot
- [ ] Messages display correctly

## Post-Deployment

### Update Documentation

Update the following with your deployed URLs:

1. **README.md**
   - Add live demo links
   - Update deployment status badges

2. **DEPLOYMENT.md**
   - Replace placeholder URLs with actual URLs

### Monitor

**Vercel Dashboard:**
- Check deployment status
- Monitor build logs
- View analytics

**Render Dashboard:**
- Check service status
- Monitor logs
- Check resource usage

### Optimize

**Frontend:**
- [ ] Enable caching
- [ ] Compress images
- [ ] Add CDN if needed

**Backend:**
- [ ] Monitor API response times
- [ ] Check Qdrant query performance
- [ ] Upgrade Render plan if needed

## Troubleshooting

### Frontend Issues

**Build Fails:**
```bash
npm run clear
rm -rf node_modules
npm install
npm run build
```

**404 on Routes:**
- Check `docusaurus.config.ts` routeBasePath
- Ensure `docs/` folder structure is correct

### Backend Issues

**Deployment Fails:**
- Verify Python version (3.11.0)
- Check all environment variables are set
- Review Render logs for errors

**CORS Errors:**
Update `backend/main.py`:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

**Chatbot Not Responding:**
- Check backend URL in Chatbot.tsx
- Verify environment variables on Render
- Check Qdrant connection
- Review backend logs

### Database Issues

**Qdrant Connection:**
- Verify QDRANT_URL and QDRANT_API_KEY
- Check collection exists
- Confirm data is indexed

**Neon PostgreSQL:**
- Verify NEON_DATABASE_URL
- Check database is active
- Monitor connection pool

## Security Checklist

- [ ] Environment variables secured in Render dashboard
- [ ] `.env` file in `.gitignore`
- [ ] No API keys in frontend code
- [ ] HTTPS enabled (automatic on Vercel/Render)
- [ ] CORS properly configured
- [ ] Rate limiting enabled (if needed)

## Performance Checklist

- [ ] Frontend build optimized
- [ ] Images compressed
- [ ] Lazy loading enabled
- [ ] Backend response time < 2s
- [ ] Qdrant queries optimized
- [ ] Caching enabled

## Final Verification

Before marking as complete:

1. [ ] Both services deployed successfully
2. [ ] Frontend URL accessible
3. [ ] Backend URL accessible
4. [ ] Integration working (chatbot responds)
5. [ ] All features functional
6. [ ] No console errors
7. [ ] Mobile responsive
8. [ ] Performance acceptable
9. [ ] Documentation updated
10. [ ] Ready for production use

## Deployment URLs

After deployment, record your URLs here:

- **Frontend**: `https://_____.vercel.app`
- **Backend**: `https://_____.onrender.com`
- **API Docs**: `https://_____.onrender.com/docs`

## Deployment Date

- **Initial Deployment**: ___________
- **Last Updated**: ___________

---

**Status**: ✅ Ready for Deployment

All dependencies installed, build successful, no critical errors!
