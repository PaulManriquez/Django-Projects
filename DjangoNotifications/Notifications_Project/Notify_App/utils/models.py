#ContentType | Allow to create relations to any model 
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

#Timezone
from django.utils import timezone

#Document
from django.db import models 

#Models
from User.models import User

class NotificationQueryset(models.QuerySet):
    #Return all the objecs notifications where read = True
    def readed(self,include_deleted=True):
        #Return the actual notifications that have beed read in the actual QuerySet 
        if include_deleted:
            return self.filter(read = True )
        
    #Return all the objecs notifications where read = False  
    def no_readed(self,include_deleted=False):
        #Return items no read in the actual Queryset
        if include_deleted==True:
            return self.filter(read=False)

    #The goal of this method is to 
    # 1) Get all the objects notifications that havent been readed using the inner method of this class (NotificationQueryset)
    # 2) If this method gets an argument destiny that could be a particular model, get first all the corresponding models 
    #    then, read is set to true 
    # 3) Once it has all the no readed elements in  "qs = self.no_readed(True)", updates all the field read = True  
    def set_all_as_read(self,destiny=None):
        #Set all the notifications on the actual query set as read 
        qs = self.no_readed(True) #query set | qs <--- qs = self.read(True) OLD CODE 
        if destiny:
            qs = qs.filter(destiny=destiny)

        return qs.update(read=True) 

    #The goal of this method is to 
    # 1) Get all the objects notifications that have been read using the inner method of this class (NotificationQueryset)
    # 2) If this method gets an argument destiny that could be a particular model, get first all the corresponding models 
    #    then, read is set to False 
    # 3) Once it has all the read elements in  "qs = self.readed(True)", updates all the field read = False 
    def set_all_as_no_read(self,destiny=None):
        #Set all the notifications as no read in the actual QuerySet
        qs = self.readed(True)#query set | qs
        if destiny:
            qs = qs.filter(destiny=destiny)

        return qs.update(read=False)    



'''
1. AbstractNotificationManager(models.Manager):
This is a custom manager class that inherits from models.Manager.
The purpose of a manager in Django is to provide database query operations for models. By default, every model in Django has a Manager called objects, but you can create custom managers to modify or extend the default behavior.
2. get_queryset(self):
This method is overridden in the custom manager. In Django, get_queryset is a method that returns a QuerySet that the manager will operate on. When you call methods like all(), filter(), exclude(), etc., on a manager, those methods are working with the QuerySet returned by get_queryset.
By overriding get_queryset, you're customizing what QuerySet the manager will use.
3. return self.NotificationQueryset(self.Model, using=self._db):
This line attempts to return an instance of NotificationQueryset, which is presumably a custom QuerySet class you've defined elsewhere.
self.Model: Refers to the model class that this manager is attached to. In Django's Manager, this attribute is usually called self.model (with a lowercase "m"). If self.Model is used, it suggests there might be a typo or a custom implementation, but typically it should be self.model.
using=self._db: Specifies the database to use for the QuerySet. self._db refers to the database alias being used for this QuerySet. This is useful in multi-database setups where you might want to specify which database the QuerySet should query.
This custom manager is designed to return a custom QuerySet (NotificationQueryset) for a model, which allows you to extend or modify how the QuerySet is constructed and used in your application. The main purpose of this manager is to ensure that when you interact with the model through this manager, you're using the customized behavior defined in NotificationQueryset.
'''        
class AbstractNotificationManager(models.Manager):
    def get_queryset(self):
        return self.NotificationQueryset(self.model,using=self._db)        

class AbstractNotification(models.Model):

    #Levels is an inner class that inherits from models.TextChoices. 
    #It defines a set of choices for the level field.
    class Levels(models.TextChoices):
        success = 'Success', 'success',
        info = 'Info','info',
        wrong = 'Wrong', 'wrong'

    level = models.CharField(choices=Levels.choices,max_length=20,default=Levels.info)
    destiny = models.ForeignKey(User,on_delete=models.CASCADE,related_name='notifications',blank=True,null=True)
    
    #actor_content_type and object_id_actor together define a generic foreign key to any model in the database. 
    #actor_content_type stores the type of the related model (using ContentType), 
    #and object_id_actor stores the ID of the related instance.
    actor_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,related_name='notify_actor')
    object_id_actor = models.PositiveBigIntegerField()
    #actor is the actual generic foreign key that combines the two fields above to create a relation to any model.
    actor = GenericForeignKey('actor_content_type','object_id_actor') #<--- This doesnt appear in the admin panel 

    #verb: A CharField that describes the action of the notification 
    #(e.g., "liked your post", "commented on your photo"). It has a maximum length of 200 characters
    verb = models.CharField(max_length=200)

    #read: A BooleanField indicating whether the notification has been read. The default value is False
    read = models.BooleanField(default=False)
    
    #public: A BooleanField indicating if the notification is public. The default value is True.
    #deleted: A BooleanField indicating if the notification has been deleted. The default value is False.
    public = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    #timestamp: A DateTimeField that stores the time when the notification was created. 
    timestamp = models.DateTimeField(default=timezone.now,db_index=True)

    '''
    1. Custom QuerySet (NotificationQueryset):
    NotificationQueryset is a subclass of models.QuerySet where you've defined custom methods like readed, no_readed, set_all_as_read, and set_all_as_no_read.
    These methods allow you to create more specialized queries that are specific to your application's needs.
    2. Replacing the Default Manager:
    Every Django model has a default manager called objects that allows you to query the database.
    By default, this manager uses models.QuerySet, which provides standard methods like filter, exclude, all, etc.
    When you use objects = NotificationQueryset.as_manager(), you're replacing the default manager with one that uses your custom NotificationQueryset.
    3. .as_manager() Method:
    The as_manager() method converts your custom NotificationQueryset class into a manager that can be used in the same way as the default objects manager.
    This means you can now use your custom methods (readed, set_all_as_read, etc.) directly on the objects manager.
    '''
    objects = NotificationQueryset.as_manager() #<-- this doesnt appear in the admin pannel 

    #The Meta class defines model-level options.
    #abstract = True means this model is an abstract base class. 
    #Other models can inherit from it, but it will not create a database table for AbstractNotification itself.
    class Meta:
        abstract = True
