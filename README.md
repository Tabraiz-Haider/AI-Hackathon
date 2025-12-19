# Physical AI Robotics Essential Course

AI/Spec-Driven Textbook for Humanoid Robotics - Built for GIAIC Hackathon

## About This Project

This project is a comprehensive educational platform for Physical AI and Humanoid Robotics, featuring:
- 📚 Interactive textbook with 10 detailed chapters
- 🤖 AI-powered chatbot with RAG (Retrieval Augmented Generation)
- 🎙️ Voice-enabled interaction
- 🌙 Dark mode support
- 🌐 Multilingual support (English/Urdu)

Built with [Docusaurus](https://docusaurus.io/) for the frontend and [FastAPI](https://fastapi.tiangolo.com/) for the backend.

## Tech Stack

### Frontend
- Docusaurus 3.9.2
- React 19.0.0
- TypeScript 5.6.2
- CSS Modules

### Backend
- FastAPI
- LangChain
- Qdrant (Vector Database)
- Groq LLM (llama-3.3-70b-versatile)
- Neon PostgreSQL

## Quick Start

### Frontend Setup

```bash
# Install dependencies
npm install

# Start development server
npm start

# Build for production
npm run build

# Serve production build locally
npm run serve
```

The website will open at `http://localhost:3000`

### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment (if not exists)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file with your API keys
# See DEPLOYMENT.md for required environment variables

# Run backend server
python main.py
```

The API will be available at `http://localhost:8000`
API documentation at `http://localhost:8000/docs`

## Project Structure

```
AI-Spec-Driven-Hackathon/
├── backend/                  # FastAPI backend
│   ├── main.py              # Main API server
│   ├── vector_store.py      # Qdrant integration
│   ├── requirements.txt     # Python dependencies
│   └── .env                 # Environment variables (not in git)
├── docs/                    # Documentation content
│   └── my-book/            # Book chapters
├── src/                     # React components
│   ├── components/
│   │   ├── Chatbot/        # AI chatbot component
│   │   └── ChapterCard/    # Chapter card component
│   ├── css/                # Global styles
│   └── pages/              # Page components
├── static/                  # Static assets
├── docusaurus.config.ts    # Docusaurus configuration
├── package.json            # Node dependencies
└── DEPLOYMENT.md          # Detailed deployment guide
```

## Features

### Interactive Chatbot
- Powered by Groq's llama-3.3-70b-versatile model
- RAG implementation using Qdrant vector database
- Voice input support using Web Speech API
- Dark mode compatible
- Context-aware responses from the textbook

### Multilingual Support
- English (default)
- Urdu (اردو)
- RTL support for Urdu language

### Responsive Design
- Mobile-friendly interface
- Adaptive grid layout
- Touch-friendly controls

## Deployment

For detailed deployment instructions, see [DEPLOYMENT.md](./DEPLOYMENT.md)

### Quick Deploy

**Frontend (Vercel):**
```bash
npm i -g vercel
vercel login
vercel --prod
```

**Backend (Render):**
- Connect your GitHub repository to Render
- Use `backend/render.yaml` for automatic configuration
- Add environment variables in Render dashboard

## Environment Variables

Create a `.env` file in the `backend/` directory:

```env
GROQ_API_KEY=your_groq_api_key
OPENROUTER_API_KEY=your_openrouter_key
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key
NEON_DATABASE_URL=your_neon_database_url
```

⚠️ **Never commit `.env` files to version control!**

## Development

### Running Both Services

Terminal 1 (Frontend):
```bash
npm start
```

Terminal 2 (Backend):
```bash
cd backend
python main.py
```

### Building

```bash
# Frontend production build
npm run build

# Test production build locally
npm run serve
```

## Troubleshooting

### Port Already in Use
```bash
# Frontend (3000)
# Kill process using port 3000 and restart

# Backend (8000)
# Kill process using port 8000 and restart
```

### Build Errors
```bash
# Clear Docusaurus cache
npm run clear
npm install
npm run build
```

### Chatbot Not Responding
- Check backend is running on port 8000
- Verify CORS settings in backend/main.py
- Check API keys in .env file
- Verify Qdrant collection exists

## Contributing

This project was built for the GIAIC Hackathon. Contributions are welcome!

## Author

**Muhammad Shayan**
- GitHub: [@Shayan-meo](https://github.com/Shayan-meo)
- LinkedIn: [Muhammad Shayan](https://www.linkedin.com/in/muhammad-shayan-99a39b2b0/)
- WhatsApp: +923118716038

## License

This project is built with ❤️ for the GIAIC Hackathon.

## Acknowledgments

- Panaversity & GIAIC for the hackathon opportunity
- Docusaurus for the amazing documentation framework
- FastAPI for the powerful backend framework
- LangChain for RAG implementation
- Qdrant for vector database
- Groq for the LLM API
