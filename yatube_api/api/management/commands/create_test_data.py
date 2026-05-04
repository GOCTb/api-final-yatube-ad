from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from posts.models import Group, Post, Comment, Follow

User = get_user_model()


class Command(BaseCommand):
    help = 'Создаёт тестовые данные для коллекции Postman'

    def handle(self, *args, **options):
        # Пользователи
        regular_user, _ = User.objects.get_or_create(username='regular_user')
        regular_user.set_password('iWannaBeAdmin')
        regular_user.is_active = True
        regular_user.save()

        admin_user, _ = User.objects.get_or_create(username='root')
        admin_user.set_password('5eCretPaSsw0rD')
        admin_user.is_superuser = True
        admin_user.is_staff = True
        admin_user.is_active = True
        admin_user.save()

        second_user, _ = User.objects.get_or_create(username='second_user')
        second_user.set_password('iWannaBeAdmin')
        second_user.is_active = True
        second_user.save()

        # Группы
        group1, _ = Group.objects.get_or_create(
            title='Группа 1',
            slug='group_1',
            description=''
        )
        group2, _ = Group.objects.get_or_create(
            title='Группа 2',
            slug='group_2',
            description=''
        )

        # Посты
        Post.objects.get_or_create(
            text='Тестовый пост с группой (regular_user)',
            author=regular_user,
            group=group1
        )
        Post.objects.get_or_create(
            text='Тестовый пост без группы (regular_user)',
            author=regular_user
        )
        Post.objects.get_or_create(
            text='Тестовый пост администратора',
            author=admin_user,
            group=group2
        )
        Post.objects.get_or_create(
            text='Тестовый пост второго пользователя',
            author=second_user,
            group=group2
        )

        # Комментарии
        post_with_group = Post.objects.filter(
            text='Тестовый пост с группой (regular_user)'
        ).first()
        Comment.objects.get_or_create(
            post=post_with_group,
            author=regular_user,
            text='Комментарий от regular_user к своему посту'
        )
        Comment.objects.get_or_create(
            post=post_with_group,
            author=admin_user,
            text='Комментарий от root к посту regular_user'
        )

        # Подписки: полностью очищаем, чтобы тесты Postman
        # создавали их "на чистом месте"
        Follow.objects.all().delete()

        self.stdout.write(self.style.SUCCESS(
            'Тестовые данные обновлены:\n'
            '  Пользователи: regular_user, root, second_user\n'
            '  Группы: group_1, group_2\n'
            '  Посты: 4\n'
            '  Комментарии: 2\n'
            '  Подписки: отсутствуют (будут созданы тестами)'
        ))
