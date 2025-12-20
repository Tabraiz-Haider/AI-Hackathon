import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Physical AI Robotics Essential Course',
  tagline: 'AI/Spec-Driven Textbook for Humanoid Robotics',
  favicon: 'img/favicon.ico',

  url: 'https://your-docusaurus-site.example.com',
  baseUrl: '/',

  organizationName: 'Tabraiz-Haider',
  projectName: 'physical-ai-textbook',

  onBrokenLinks: 'throw',
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
        htmlLang: 'ur',
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
        editUrl: undefined,
      },
    ],
  ],

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          routeBasePath: 'docs',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/docusaurus-social-card.jpg',
    colorMode: {
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
          type: 'custom-languageSwitcher',
          position: 'right',
        },
        {
          href: 'https://www.linkedin.com/in/muhammad-shayan-99a39b2b0/',
          className: 'header-linkedin-link',
          'aria-label': 'LinkedIn profile',
          position: 'right',
        },
        {
          href: 'https://github.com/Shayan-meo',
          className: 'header-github-link',
          'aria-label': 'GitHub repository',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Links',
          items: [
            {
              label: 'Introduction',
              to: '/docs/my-book/introduction',
            },
            {
              label: 'Chapter 1: Basics of Physical AI',
              to: '/docs/my-book/chapter-1',
            },
            {
              label: 'Chapter 10: Applications',
              to: '/docs/my-book/chapter-10',
            },
            {
              label: 'Conclusion',
              to: '/docs/my-book/conclusion',
            },
          ],
        },
        {
          title: 'Hackathon & Tools',
          items: [
            {
              label: 'Panaversity',
              href: 'https://panaversity.org/',
            },
            {
              label: 'GIAIC',
              href: 'https://www.governorhouse.com.pk/',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/Shayan-meo',
            },
            {
              label: 'LinkedIn',
              href: 'https://www.linkedin.com/in/muhammad-shayan-99a39b2b0/',
            },
          ],
        },
        {
          title: 'Project Tools',
          items: [
            {
              label: 'Docusaurus',
              href: 'https://docusaurus.io/',
            },
            {
              label: 'Privacy Policy',
              to: '/privacy',
            },
            {
              label: 'Terms of Service',
              to: '/terms',
            },
            {
              label: 'WhatsApp Support',
              href: 'https://wa.me/923118716038',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Physical AI Robotics Course | Built with ❤️ for GIAIC Hackathon by Muhammad Shayan`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;

