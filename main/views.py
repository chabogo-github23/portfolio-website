from django.shortcuts import render

def portfolio(request):
    context = {
        'personal_info': {
            'name': 'Caleb Nyamawi Thomas',
            'nationality': 'Kenyan',
            'languages': ['English', 'Kiswahili', 'Mijikenda'],
            'email': 'calebchabogo@gmail.com',
            'phone': '0793706728',
            'postal_address': '62-90132'
        },
        'career_objectives': [
            'To get an opportunity to sharpen my skills. I strive to associate myself with an organization where I can utilize my skills in the best possible manner, which further gives me an opportunity to grow in my career journey while contributing to the development of the organization',
            'To become a successful expert in the field of IT by channelizing my technical knowledge and skills to ensure personal and professional growth and to contribute to the prosperity of the organization.',
            'To become an IT expert to solve problems rising in today\'s world in the field of Information Systems and Computing.'
        ],
        'education': [
            {
                'qualification': 'Bachelor of Science In Software Engineering',
                'institution': 'University of Eastern Africa, Baraton',
                'period': '2021-2025',
                'grade': 'In Progress'
            },
            {
                'qualification': 'Kenya Certificate of Secondary Education (K.C.S.E)',
                'institution': 'Ribe Boys High School',
                'period': '2017-2020',
                'grade': 'B (plain)'
            },
            {
                'qualification': 'Kenya Certificate of Primary Education',
                'institution': 'Mnyalatsoni Primary School',
                'period': '2007-2015',
                'grade': '316 marks'
            }
        ],
        'experience': [
            {
                'position': 'Software Developer',
                'company': 'Taquana Limited',
                'location': 'Nairobi',
                'period': 'May - September 2024'
            }
        ],
        'technical_skills': [
            'Python Programming',
            'Java Programming', 
            'C Programming',
            'Django Framework',
            'React.js',
            'Flutter',
            'MySQL Database',
            'MongoDB',
            'HTML/CSS/JavaScript',
            'Network Device Configuration'
        ],
        'soft_skills': [
            'Teamwork',
            'Communication Skills',
            'Problem Solving',
            'Innovation',
            'Leadership',
            'Time Management',
            'Adaptability',
            'Creativity'
        ],
        'hobbies': ['Travelling', 'Learning', 'Coding', 'Hiking', 'Reading'],
        'references': [
            {
                'name': 'Mr. Omambia Andrew',
                'position': 'Department Lecturer',
                'organization': 'University of Eastern Africa, Baraton',
                'location': 'Eldoret',
                'phone': '+254723140175',
                'email': 'omambiaa@ueab.ac.ke'
            },
            {
                'name': 'Mr. Jefferson Mwatati',
                'position': 'Department Lecturer',
                'organization': 'University of Eastern Africa, Baraton',
                'location': 'Eldoret',
                'phone': '+254710719042',
                'email': ''
            },
            {
                'name': 'Mr. Paul Wekesa',
                'position': 'CEO, Founder and Full Stack Developer',
                'organization': 'Taquana Limited',
                'location': 'Nairobi',
                'phone': '+254746366069',
                'email': 'wekesa350@taquana.ke'
            }
        ]
    }
    return render(request, 'portfolio.html', context)
