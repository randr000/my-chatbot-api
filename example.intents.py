name = 'bot'

intents = {
    'intents': [
      {
        'tag': 'greeting',
        "patterns": [
          'Hi',
          'Hey',
          'How are you',
          'Is anyone there?',
          'Hello',
          'Good day'
        ],
        'responses': [
          ['Hey :-)'],
          ['Hello, thanks for visiting'],
          ['Hi there.", "What can I do for you?'],
          ['Hi there.", "How can I help?']
        ]
      },
      {
        'tag': 'goodbye',
        'patterns': ['Bye', 'See you later', 'Goodbye'],
        'responses': [
          ['See you later.', 'Thanks for visiting'],
          ['Have a nice day'],
          ['Bye!', 'Come back again soon.']
        ]
      },
      {
        'tag': 'name',
        'patterns': ['What is your name?'],
        'responses': [
          [f'My name is {name}']
        ]
      }
    ]
  }