import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Physical AI Robotics Essential Course',
  tagline: 'AI/Spec-Driven Textbook for Humanoid Robotics',
  favicon: 'img/favicon.ico',

  // UPDATE: Yahan apni asal website ka link dalna hoga deploy hone ke baad
  url: 'https://physical-ai-robotics.vercel.app', 
  baseUrl: '/',

  organizationName: 'Tabraiz-Haider',
  projectName: 'AI-Hackathon', // Repo name ke mutabiq update kiya hai

  // Deployment safety
  onBrokenLinks: 'warn', 
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'ur'],
    localeConfigs: {
      en: {
        label: 'English',
        direction: 'ltr',
        htmlLang: 'en-US',
      },
      ur: {
        label: 'اردو',
        direction: 'rtl',
        htmlLang: 'ur-PK',
      },
    },
  },

  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'urdu-docs',
        path: 'urdu-docs',
        routeBasePath: 'ur', 
        sidebarPath: require.resolve('./sidebars-urdu.ts'),
      },
    ],
  ],

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.ts'),
          routeBasePath: 'docs',
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/docusaurus-social-card.jpg',
    colorMode: {
      defaultMode: 'dark',
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'Physical AI Robotics',
      logo: {
        alt: 'Physical AI Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Textbook Chapters',
        },
        {
          type: 'localeDropdown',
          position: 'right',
        },
        {
          href: 'https://www.linkedin.com/in/muhammad-shayan-99a39b2b0/',
          className: 'header-linkedin-link',
          'aria-label': 'LinkedIn profile',
          position: 'right',
        },
        {
          href: 'https://github.com/Tabraiz-Haider/AI-Hackathon',
          position: 'right',
          label: 'GitHub',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Chapters',
          items: [
            { label: 'Introduction', to: '/docs/my-book/introduction' },
            { label: 'Chapter 1', to: '/docs/my-book/chapter-1' },
          ],
        },
        {
          title: 'Community',
          items: [
            { label: 'Panaversity', href: 'https://panaversity.org/' },
            { label: 'WhatsApp Support', href: 'https://wa.me/923118716038' },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Physical AI Robotics Course | Built for GIAIC Hackathon by Muhammad Shayan`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
