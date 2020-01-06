import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings')
django.setup()

from vinyls.models import Genre, Album, Track, Review, CustomUser


def add_objects():
    prog = Genre(name='Progressive Rock')
    jazz = Genre(name='Jazz')
    metal = Genre(name='Metal')
    indie = Genre(name='Indie')

    prog.save()
    jazz.save()
    metal.save()
    indie.save()

    red = Album(title='Red', artist='King Crimson', year='1974-01-01',
                duration='00:39:59', label='Virgin', price=50.00)
    malomiasteczkowy = Album(title='Małomiasteczkowy', artist='Dawid Podsiadło', year='2018-01-01',
                             duration='00:40:11', label='Sony', price=25.00)
    painkiller = Album(title='Painkiller', artist='Judas Priest', year='1990-01-01',
                       duration='00:46:11', label='Columbia Records', price=30.00)
    coltrane = Album(title='Blue Train', artist='John Coltrane', year='1958-01-01',
                     duration='00:41:54', label='Blue Note', price=40.00)
    discipline = Album(title='Discipline', artist='King Crimson', year='1981-01-01',
                       duration='00:37:55', label='Warner Bros.', price=45.00)

    red.save()
    malomiasteczkowy.save()
    painkiller.save()
    coltrane.save()
    discipline.save()

    red.genres.add(prog)
    malomiasteczkowy.genres.add(indie)
    painkiller.genres.add(metal)
    coltrane.genres.add(jazz)
    discipline.genres.add(prog)

    for album in Album.objects.all():
        for i in range(1, 6):
            Track.objects.create(title=f'Test{i}', order=i, duration='00:05:00', album=album)

    user1 = CustomUser.objects.create_user('user1', password='testpass')
    user2 = CustomUser.objects.create_user('user2', password='testpass')
    user3 = CustomUser.objects.create_user('user3', password='testpass')

    Review.objects.create(owner=user1, album=red, rating=5, content='Pretty Good')
    Review.objects.create(owner=user1, album=malomiasteczkowy, rating=4, content='Holy Molly')
    Review.objects.create(owner=user1, album=discipline, rating=4, content='Vibin\'')
    Review.objects.create(owner=user2, album=coltrane, rating=5, content='That\'s the best colour')
    Review.objects.create(owner=user2, album=red, rating=1, content='Aweful, Blue is so much better')
    Review.objects.create(owner=user3, album=painkiller, rating=4, content='I only listen to metal')


if __name__ == '__main__':
    add_objects()
