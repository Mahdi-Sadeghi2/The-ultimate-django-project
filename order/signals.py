from django.db.models.signals import (pre_save, 
                                      post_save, 
                                      pre_delete, 
                                      post_delete)

from django.dispatch import receiver

from django.contrib.auth.models import User


# Signal to handle pre-seve event for user model
@receiver(pre_save, sender=User, dispatch_uid="my_unique_identifier1")
def pre_save_user(sender, instance, **kwargs):
    # Add your pre-save login for user here
    print(f'Pre-save for user "{instance}".')


# Signal to handle post-seve event for user model
@receiver(post_save, sender=User, dispatch_uid="my_unique_identifier2")
def post_save_user(sender, instance, created,**kwargs):
    if created:

        # This is triggered for update to existing instance
        print(f'User "{instance}" has been created.')
    else:
        # This is triggered for update to existing instance
        print(f'User "{instance}" has been updated.')


@receiver(pre_delete, sender=User, dispatch_uid="my_unique_identifier3")
def pre_delete_user(sender, instance,**kwargs):
    # This is triggered for update to existing instance
    print(f'Pre-delete signal: User "{instance.username}" is about to be deleted.')


@receiver(post_delete, sender=User, dispatch_uid="my_unique_identifier3")
def post_delete_user(sender, instance,**kwargs):
    # This is triggered for update to existing instance
    print(f'Post-delete signal: User "{instance.username}" has been deleted.')
   