import React, { useState } from 'react';

function Footer(): JSX.Element | null {
  const [hovered, setHovered] = useState<string | null>(null);

  const styles = {
    footer: {
      backgroundColor: '#0b0b0b',
      padding: '3rem 0',
      color: '#e5e7eb',
    },
    container: {
      maxWidth: '1200px',
      margin: '0 auto',
      padding: '0 1rem',

    },
    grid: {
      display: 'grid',
      gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))',
      gap: '3rem',
      marginBottom: '2rem',
    },
    sectionTitle: {
      color: '#22d3ee',
      fontSize: '1.1rem',
      marginBottom: '0.75rem',
      fontWeight: 600,
    },
    list: {
      listStyle: 'none',
      padding: 0,
      margin: 0,
    },
    listItem: {
      marginBottom: '0.6rem',
    },
    link: {
      color: '#e5e7eb',
      textDecoration: 'none',
      fontSize: '0.95rem',
      transition: 'color 0.25s ease',
      cursor: 'pointer',
    },
    copyright: {
      borderTop: '1px solid rgba(255,255,255,0.1)',
      paddingTop: '1rem',
      textAlign: 'center' as const,
      fontSize: '0.85rem',
      color: '#9ca3af',
    },
  };

  const getLinkStyle = (id: string) => ({
    ...styles.link,
    color: hovered === id ? '#22d3ee' : '#e5e7eb',
  });

  return (
    <footer style={styles.footer}>
      <div style={styles.container}>
        <div style={styles.grid}>
          <div>
            <h3 style={styles.sectionTitle}>Links</h3>
            <ul style={styles.list}>
              <li style={styles.listItem}>
                <a
                  style={getLinkStyle('intro')}
                  onMouseEnter={() => setHovered('intro')}
                  onMouseLeave={() => setHovered(null)}
                  href="/docs/my-book/introduction"
                >
                  Introduction
                </a>
              </li>
              <li style={styles.listItem}>
                <a
                  style={getLinkStyle('doc')}
                  onMouseEnter={() => setHovered('doc')}
                  onMouseLeave={() => setHovered(null)}
                  href="/docs/intro"
                >
                  Document
                </a>
              </li>
            </ul>
          </div>

          <div>
            <h3 style={styles.sectionTitle}>Hackathon & Tools</h3>
            <ul style={styles.list}>
              <li style={styles.listItem}>
                <a
                  style={getLinkStyle('whatsapp')}
                  onMouseEnter={() => setHovered('whatsapp')}
                  onMouseLeave={() => setHovered(null)}
                  href="https://wa.me/923278448829"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  WhatsApp Contact
                </a>
              </li>
              <li style={styles.listItem}>
                <a
                  style={getLinkStyle('panaverse')}
                  onMouseEnter={() => setHovered('panaverse')}
                  onMouseLeave={() => setHovered(null)}
                  href="https://panaversity.org/"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  Panaverse Initiative
                </a>
              </li>
            </ul>
          </div>

          <div>
            <h3 style={styles.sectionTitle}>Project Tools</h3>
            <ul style={styles.list}>
              <li style={styles.listItem}>
                <a
                  style={getLinkStyle('gemini')}
                  onMouseEnter={() => setHovered('gemini')}
                  onMouseLeave={() => setHovered(null)}
                  href="https://gemini.google.com/app"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  Gemini
                </a>
              </li>
              <li style={styles.listItem}>
                <a
                  style={getLinkStyle('docusaurus')}
                  onMouseEnter={() => setHovered('docusaurus')}
                  onMouseLeave={() => setHovered(null)}
                  href="https://docusaurus.io/"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  Docusaurus
                </a>
              </li>
            </ul>
          </div>
        </div>

        <div style={styles.copyright}>
          © {new Date().getFullYear()} Physical AI Robotics Course. Built for GIAIC Hackathon.
        </div>
      </div>
    </footer>
  );
}

export default React.memo(Footer);
