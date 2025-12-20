import React from 'react';
import Link from '@docusaurus/Link';
import Heading from '@theme/Heading';

// Card Component
function Card({ to, title, description, buttonText }) {
  return (
    <div className="chapter-card">
      <Heading as="h3" className="card__title">{title}</Heading>
      <p className="card__description">{description}</p>
      <Link className="button button--secondary" to={to}>
        {buttonText}
      </Link>
    </div>
  );
}

// Main Component
export default function HomepageFeatures(): JSX.Element {
  return (
    <div className="chapters-section">
      <div className="container">
        <Heading as="h2" className="section-title">Explore Our Chapters</Heading>
        <div className="chapters-flex-container">

          <Card to="/docs/my-book/chapter-1" title="1: Basics of Physical AI" description="An introduction to the fundamental concepts of physical artificial intelligence." buttonText="Start Reading" />

          <Card to="/docs/my-book/chapter-2" title="2: Robotics Fundamentals" description="Learn the essential principles of robotics and their components." buttonText="Start Reading" />

          <Card to="/docs/my-book/chapter-3" title="3: Sensors & Actuators" description="Explore the hardware that allows robots to perceive and interact with the world." buttonText="Start Reading" />

          <Card to="/docs/my-book/chapter-4" title="4: Kinematics & Dynamics" description="Understand the motion of robots and the forces that govern them." buttonText="Start Reading" />

          <Card to="/docs/my-book/chapter-5" title="5: Control Systems" description="Delve into the algorithms that control robot behavior." buttonText="Start Reading" />

          <Card to="/docs/my-book/chapter-6" title="6: Humanoid Robot Design" description="Learn the principles behind designing and building humanoid robots." buttonText="Start Reading" />

          <Card to="/docs/my-book/chapter-7" title="7: AI Algorithms in Robotics" description="Discover how AI algorithms are applied to solve complex robotics problems." buttonText="Start Reading" />

          <Card to="/docs/my-book/chapter-8" title="8: Robot Perception" description="Learn how robots see, hear, and understand their environment." buttonText="Start Reading" />

          <Card to="/docs/my-book/chapter-9" title="9: Motion Planning & Navigation" description="Explore how robots plan their movements and navigate in complex spaces." buttonText="Start Reading" />

          <Card to="/docs/my-book/chapter-10" title="10: Applications & Case Studies" description="Explore real-world applications of physical AI and robotics through in-depth case studies." buttonText="Start Reading" />

        </div>
      </div>
    </div>
  );
}
