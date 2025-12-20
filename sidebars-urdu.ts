import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  urduSidebar: [
    'intro',
    {
      type: 'category',
      label: 'فزیکل مصنوعی ذہانت اور انسان نما روبوٹکس',
      collapsed: false,
      items: [
        {
          type: 'doc',
          id: 'my-book/introduction',
          label: 'تعارف',
        },
        {
          type: 'doc',
          id: 'my-book/chapter-1',
          label: 'فزیکل مصنوعی ذہانت کی بنیادیات',
        },
        {
          type: 'doc',
          id: 'my-book/chapter-2',
          label: 'روبوٹکس کی بنیادیات',
        },
        {
          type: 'doc',
          id: 'my-book/chapter-3',
          label: 'سینسرز اور ایکچویٹرز',
        },
        {
          type: 'doc',
          id: 'my-book/chapter-4',
          label: 'حرکیات اور حرکی قوانین',
        },
        {
          type: 'doc',
          id: 'my-book/chapter-5',
          label: 'کنٹرول سسٹمز',
        },
        {
          type: 'doc',
          id: 'my-book/chapter-6',
          label: 'انسان نما روبوٹ کا ڈیزائن',
        },
        {
          type: 'doc',
          id: 'my-book/chapter-7',
          label: 'روبوٹکس میں مصنوعی ذہانت کے الگورتھم',
        },
        {
          type: 'doc',
          id: 'my-book/chapter-8',
          label: 'روبوٹ کا ادراک',
        },
        {
          type: 'doc',
          id: 'my-book/chapter-9',
          label: 'موشن پلاننگ اور نیویگیشن',
        },
        {
          type: 'doc',
          id: 'my-book/chapter-10',
          label: 'استعمالات اور کیس اسٹڈیز',
        },
        {
          type: 'doc',
          id: 'my-book/conclusion',
          label: 'اختتامیہ',
        },
      ],
    },
  ],
};

export default sidebars;
