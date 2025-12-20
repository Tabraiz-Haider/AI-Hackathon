import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import clsx from 'clsx';
import styles from './index.module.css';
import ChapterCard from '../components/ChapterCard'; // Import the ChapterCard component

const chapters = [
  {
    title: '1: Basics of Physical AI',
    description: 'Understand the core concepts and theoretical underpinnings of Physical AI.',
    to: '/docs/my-book/chapter-1',
  },
  {
    title: '2: AI Algorithms in Robotics',
    description: 'Explore fundamental AI algorithms used in various robotic applications.',
    to: '/docs/my-book/chapter-2',
  },
  {
    title: '3: Robot Perception',
    description: 'Delve into how robots perceive their environment using various sensors.',
    to: '/docs/my-book/chapter-3',
  },
  {
    title: '4: Kinematics & Dynamics',
    description: 'Learn the mechanics of robot movement, including kinematics and dynamics.',
    to: '/docs/my-book/chapter-4',
  },
  {
    title: '5: Control Systems',
    description: 'Study the principles of control systems for precise robot manipulation.',
    to: '/docs/my-book/chapter-5',
  },
  {
    title: '6: Humanoid Robot Design',
    description: 'Discover the design principles and challenges of creating humanoid robots.',
    to: '/docs/my-book/chapter-6',
  },
  {
    title: '7: Motion Planning & Navigation',
    description: 'Understand how robots plan movements and navigate complex environments.',
    to: '/docs/my-book/chapter-7',
  },
  {
    title: '8: Applications & Case Studies',
    description: 'Explore real-world applications and detailed case studies of physical AI.',
    to: '/docs/my-book/chapter-8',
  },
  {
    title: '9: Future of Physical AI',
    description: 'A look into the future trends and ethical considerations in physical AI and robotics.',
    to: '/docs/my-book/chapter-9',
  },
  {
    title: '10: Advanced Topics',
    description: 'Dive deeper into specialized areas and cutting-edge research in the field.',
    to: '/docs/my-book/chapter-10',
  },
];

const extraTools = [
  {
    title: 'Your Journey into AI',
    description: 'A short motivational paragraph about starting your AI journey.',
    link: '/docs/motivation',
  },
  {
    title: 'Hackathon Progress Tracker',
    description: 'Track your progress and status in the hackathon.',
    link: '/hackathon-progress',
  },
  {
    title: 'Certification Path',
    description: 'Information about course completion and certification.',
    link: '/certification',
  },
];


function HomepageHeader() {
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <h1 className="hero__title">Physical AI Robotics Essential Course</h1>
        <p className="hero__subtitle">AI/Spec-Driven Textbook for Humanoid Robotics</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/my-book/introduction">
            Start Reading My Book
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home(): JSX.Element {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="Description will go into a meta tag in <head />">
      <HomepageHeader />
      <main>
        <section className={clsx('chapters-section', styles.chaptersSection)}>
          <div className="container">
            <h2 className={clsx('section-title', styles.sectionTitle)}>Textbook Chapters</h2>
            <div className={styles.chaptersFlexContainer}>
              {chapters.map((chapter, index) => (
                <ChapterCard key={index} {...chapter} />
              ))}
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}