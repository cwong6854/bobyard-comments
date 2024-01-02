# comments/management/commands/load_comments.py
import json
from django.core.management.base import BaseCommand
from app.models import Comment
from datetime import datetime

class Command(BaseCommand):
    help = 'Load comments from JSON file'

    def handle(self, *args, **options):
        with open('comments/comments.json', 'r') as file:
            data = json.load(file)

            for comment_data in data['comments']:
                Comment.objects.create(
                    id=comment_data['id'],
                    author=comment_data['author'],
                    text=comment_data['text'],
                    date=datetime.strptime(comment_data['date'], '%Y-%m-%dT%H:%M:%SZ'),
                    likes=comment_data['likes'],
                    image=comment_data['image']
                )

        self.stdout.write(self.style.SUCCESS('Successfully loaded comments'))
