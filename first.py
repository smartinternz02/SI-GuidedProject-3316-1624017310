import requests
r = requests.post(
    "https://api.deepai.org/api/summarization",
    data={
        'text': 'A hobby is considered to be a regular activity that is done for enjoyment, typically during ones leisure time, not professionally and not for pay. Hobbies include collecting themed items and objects, engaging in creative and artistic pursuits, playing sports, or pursuing other amusements. Participation in hobbies encourages acquiring substantial skills and knowledge in that area. A list of hobbies changes with renewed interests and developing fashions, making it diverse and lengthy. Hobbies tend to follow trends in society, for example stamp collecting was popular during the nineteenth and twentieth centuries as postal systems were the main means of communication, while video games are more popular nowadays following technological advances. The advancing production and technology of the nineteenth century provided workers with more availability in leisure time to engage in hobbies. Because of this, the efforts of people investing in hobbies has increased with time.',
    },
    headers={'api-key': 'a1d0cc1e-7051-48d1-81c2-c566ef074437'}
)
print(r.json())



