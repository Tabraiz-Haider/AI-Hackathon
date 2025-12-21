import React, { useEffect } from 'react';
import { useLocation } from '@docusaurus/router';
import Chatbot from '../components/Chatbot/Chatbot';
import { AuthProvider } from '../contexts/AuthContext';

// This component wraps the entire app
export default function Root({children}) {
  const location = useLocation();

  useEffect(() => {
    // Check if current path is Urdu
    const isUrduPath = location.pathname.startsWith('/urdu');

    // Get html and body elements
    const htmlElement = document.documentElement;
    const bodyElement = document.body;

    if (isUrduPath) {
      // Set Urdu (RTL) styles with force
      htmlElement.setAttribute('lang', 'ur');
      htmlElement.setAttribute('dir', 'rtl');
      htmlElement.style.direction = 'rtl';
      htmlElement.classList.add('urdu-mode');

      bodyElement.setAttribute('dir', 'rtl');
      bodyElement.style.direction = 'rtl';
      bodyElement.classList.add('urdu-mode');

      // Force RTL on main wrapper
      const mainWrapper = document.querySelector('.main-wrapper');
      if (mainWrapper) {
        mainWrapper.setAttribute('dir', 'rtl');
      }

      // Force RTL on all articles
      const articles = document.querySelectorAll('article');
      articles.forEach(article => {
        article.setAttribute('dir', 'rtl');
        article.style.direction = 'rtl';
      });
    } else {
      // Set English (LTR) styles
      htmlElement.setAttribute('lang', 'en');
      htmlElement.setAttribute('dir', 'ltr');
      htmlElement.style.direction = 'ltr';
      htmlElement.classList.remove('urdu-mode');

      bodyElement.setAttribute('dir', 'ltr');
      bodyElement.style.direction = 'ltr';
      bodyElement.classList.remove('urdu-mode');

      // Reset to LTR
      const mainWrapper = document.querySelector('.main-wrapper');
      if (mainWrapper) {
        mainWrapper.setAttribute('dir', 'ltr');
      }

      const articles = document.querySelectorAll('article');
      articles.forEach(article => {
        article.setAttribute('dir', 'ltr');
        article.style.direction = 'ltr';
      });
    }
  }, [location.pathname]);

  return (
    <AuthProvider>
      {children}
      <Chatbot />
    </AuthProvider>
  );
}
