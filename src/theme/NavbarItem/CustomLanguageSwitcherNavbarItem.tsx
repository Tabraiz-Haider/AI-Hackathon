import React from 'react';
import { useLocation } from '@docusaurus/router';
import Link from '@docusaurus/Link';

export default function CustomLanguageSwitcherNavbarItem(): JSX.Element {
  const location = useLocation();
  const currentPath = location.pathname;

  // Detect current language based on path
  const isUrdu = currentPath.startsWith('/ur/') || currentPath.startsWith('/ur');
  const isEnglish = currentPath.startsWith('/docs/') || currentPath === '/' || !isUrdu;

  return (
    <div className="language-switcher-container">
      <Link
        to="/docs/my-book/introduction"
        className={`language-button english-button ${isEnglish ? 'active' : ''}`}
        aria-label="Switch to English"
      >
        English
      </Link>
      <Link
        to="/ur/my-book/introduction"
        className={`language-button urdu-button ${isUrdu ? 'active' : ''}`}
        aria-label="Switch to Urdu"
      >
        اردو
      </Link>
    </div>
  );
}
