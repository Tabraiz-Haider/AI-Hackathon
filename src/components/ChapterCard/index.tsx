import React from 'react';
import Link from '@docusaurus/Link';
import clsx from 'clsx';
import styles from './styles.module.css';

interface ChapterCardProps {
  title: string;
  description: string;
  to: string;
}

export default function ChapterCard({ title, description, to }: ChapterCardProps): JSX.Element {
  return (
    <div className={clsx('card', styles.chapterCard)}>
      <h3 className={styles.chapterCardTitle}>{title}</h3>
      <p className={styles.chapterCardDescription}>{description}</p>
      <Link
        className={clsx('button button--primary', styles.chapterCardButton)}
        to={to}>
        Start Reading
      </Link>
    </div>
  );
}
