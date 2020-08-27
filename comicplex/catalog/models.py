from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

class Genre(models.Model):
    '''Model to represent book genres'''
    name = models.CharField(
        max_length=50, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        '''string for representing the model object'''
        return self.name


class Tag(models.Model):
    '''Model to represent book genres'''
    name = models.CharField(
        max_length=50, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        '''string for representing the model object'''
        return self.name

class Publisher(models.Model):
    '''Model to represent book genres'''
    name = models.CharField(
        max_length=50, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        '''string for representing the model object'''
        return self.name


class Person(models.Model):
    '''Model to represent authors'''
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)

    class Meta:
        ordering = ['last_name','first_name']

    def get_absolute_url(self):
        '''Returns the url to access a particular author instance'''
        return reverse("person-detail", args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

class Character(models.Model):
    '''Model to represent characters and teams'''
    CHAR_TYPES = (
        ('h', 'Hero'),
        ('v','Villain'),
        ('o','Others'),
        ('H','Superhero Team'),
        ('V','Supervillain Team'),
        ('O','Other team/group'),
    )

    name = models.CharField(max_length=50, help_text= 'Enter character name')
    type = models.CharField(max_length=1,choices=CHAR_TYPES,blank=True, default = 'h', help_text='Enter if character is hero/villain/team')
    real_name = models.CharField(max_length = 100, help_text = 'Real name')
    creators = models.ManyToManyField(Person, blank=True, help_text ='Enter name of creators')
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, help_text='Select publisher')
    team_members = models.ManyToManyField('Character', help_text='enter which characters are member of team (if team)',related_name ='part_of_teams')
    friends = models.ManyToManyField('Character', help_text='friends',related_name='family')
    enemies = models.ManyToManyField('Character', help_text='enemies',related_name='adversaries')
    teams = models.ManyToManyField('Character', help_text = 'enter which teams character is member of (if person)', related_name='members')

    def __str__(self):
        return self.name

class Comic(models.Model):
    '''Model to represent individual comic issues'''
    series = models.CharField(max_length=50, help_text='Enter name of series')
    volume = models.IntegerField(help_text='Enter Volume no')
    issue_no = models.IntegerField(help_text='Enter issue no')
    issue_suffix = models.CharField(max_length=1,help_text='Enter issue_no_suffix')
    publisher = models.ForeignKey(Publisher, null=True,on_delete=models.SET_NULL)
    imprint = models.CharField(max_length=50, help_text='Enter name of imprint')


    COMIC_FORMATS = (
        ('PB', 'Normal'),
        ('TPB', 'Trade Paperback'),
        ('HC', 'Hardcover'),
        ('OHC', 'Oversized Hardcover'),
        ('OMN','Omnibus'),
        ('ABS','Absolute'),
    )

    format = models.CharField(
        max_length=3,
        choices=COMIC_FORMATS,
        blank=True,
        default='PB',
        help_text='Enter format of comic'
    )
    cover_date = models.DateField('cover_date')

    pages = models.IntegerField(help_text='No of Pages')

    writers = models.ManyToManyField(Person, help_text='Enter name of writers',related_name='writer_comics')
    artists = models.ManyToManyField(Person, help_text='Enter name of artists',related_name='artist_comics')
    colors = models.ManyToManyField(Person, help_text='Enter name of writers',related_name='colors_comics')
    inks = models.ManyToManyField(Person, help_text='Enter name of writers',related_name='inks_comics')
    letters = models.ManyToManyField(Person, help_text='Enter name of writers',related_name='letters_comics')
    covers = models.ManyToManyField(Person, help_text='Enter name of writers',related_name='covers_comics')
    issue_name = models.CharField(max_length=50, help_text = 'Enter name of issue')
    storyarc = models.CharField(max_length=50, help_text = 'Enter story arc')
    main_character = models.ForeignKey(Character, null=True, on_delete=models.SET_NULL, help_text = 'Enter name of main character or team')

    supporting_characters = models.ManyToManyField(Character, help_text = 'Enter name of supporting characters or team',related_name='comics_supporting')
    villains = models.ManyToManyField(Character, help_text = 'Enter name of villains or team',related_name='comics_villains')
    other_characters = models.ManyToManyField(Character, help_text = 'Enter name of other characters or team',related_name='comics_others')
    
    tags = models.ManyToManyField(Tag, help_text='Enter tags')

    def __str__(self):
        if self.volume is not None:
            vol_part = ' v' + str(self.volume)
        else:
            vol_part=''
        if self.issue_no is not None:
            issue_part = '# ' + str(self.issue_no)
            if self.issue_suffix is not None and self.issue_suffix !='':
                issue_part = issue_part + '.' + self.issue_suffix
        else:
            issue_part=''   
        if self.issue_name is not None and self.issue_name !='':
            name_part = ' : ' + str(self.issue_name)
        else:
            name_part=''
        return f'{self.series}{vol_part}{issue_part}{name_part}'
    

class Collection(models.Model):
    '''Model to represent collections/events/storylines/reading orders across multiple comics'''
    name = models.TextField(max_length = 50, help_text = 'Enter name of collection')
    comics = models.ManyToManyField(Comic, through='Reading_Order',related_name='collections')
    main_character = models.ForeignKey(Character, null=True, on_delete=models.SET_NULL, help_text='Enter name of main character or team for this collection')
    tie_in_comics = models.ManyToManyField(Comic, related_name='tied_in_with')
    tie_in_collections = models.ManyToManyField('Collection',related_name='tied_in_with')

    def __str__(self):
        return self.name
    
    def get_comics(self):
        return self.comics.order_by('reading_order')

class Reading_Order(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    order_no = models.IntegerField()
    
    class Meta:
        ordering = ('order_no',)