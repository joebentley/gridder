
validator = new FormValidator 'grid', [
  {
    name: 'ylines',
    rules: 'numeric|greater_than[5]|less_than[50]'
  },
]
