var schema = {
    'uid': 'number',
    'livesIn': 'city',
    'lifeEvents': 'lifeEvents',
    'birthDate': 'restrictedDate',
    'likes': 'facebookLikes',
    'relationships': 'facebookRelationships',
    'from': 'cityCountry',
    'name': 'name',
    'gender': 'gender',
    'age': 'number',
    'posts': 'facebookPost'
};

var facebookPostSchema = {
    timestamp: 'dateRecent',
    description: 'text',
    reactions: 'facebookReactions',
    comments: 'number',
    shares: 'number'
};
