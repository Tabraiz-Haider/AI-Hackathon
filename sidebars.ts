import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Physical AI & Humanoid Robotics',
      link: {
        type: 'generated-index',
        title: 'Physical AI & Humanoid Robotics',
        description: 'Complete guide to Physical AI and Humanoid Robotics',
        slug: '/category/my-book',
      },
      items: [
        {
          type: 'doc',
          id: 'my-book/introduction',
          label: 'Introduction',
        },
        {
          type: 'doc',
          id: 'my-book/chapter-1',
          label: 'Basics of Physical AI',
        },
        {
          type: 'doc',
          id: 'my-book/chapter-2',
          label: 'Robotics Fundamentals',
        },
        {
          type: 'doc',
          id: 'my-book/chapter-3',
          label: 'Sensors & Actuators',
        },
        {
          type: 'doc',
          id: 'my-book/chapter-4',
          label: 'Kinematics & Dynamics',
        },
        {
          type: 'doc',
          id: 'my-book/chapter-5',
          label: 'Control Systems',
        },
        {
          type: 'doc',
          id: 'my-book/chapter-6',
          label: 'Humanoid Robot Design',
        },
        {
          type: 'doc',
          id: 'my-book/chapter-7',
          label: 'AI Algorithms in Robotics',
        },
        {
          type: 'doc',
          id: 'my-book/chapter-8',
          label: 'Robot Perception',
        },
        {
          type: 'doc',
          id: 'my-book/chapter-9',
          label: 'Motion Planning & Navigation',
        },
        {
          type: 'doc',
          id: 'my-book/chapter-10',
          label: 'Applications & Case Studies',
        },
        {
          type: 'doc',
          id: 'my-book/conclusion',
          label: 'Conclusion',
        },
      ],
    },
  ],

  // But you can create a sidebar manually
  /*
  tutorialSidebar: [
    'intro',
    'hello',
    {
      type: 'category',
      label: 'Tutorial',
      items: ['tutorial-basics/create-a-document'],
    },
  ],
   */
};

export default sidebars;
